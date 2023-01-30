#!/usr/bin/env python3
"""
Sends a named file to a specified CloudWatch log group stream as one or more
log events. The number of log events is determined by the size of the file and
the specified maximum message size.
"""
import argparse
import time
import boto3
import logging

logger = logging.getLogger(__name__)
client = boto3.client("logs")
LOG_LEVEL_DETAIL = 15


def send_log_event(message: str, log_group_name: str, log_stream_name: str):
    """
    Create a new CloudWatch log event with the `message` in log stream
    `log_group_stream` in log group `log_group_name`.

    :param message: The message to be sent
    :param log_group_name: The CloudWatch log group name
    :param log_stream_name: The CloudWatch log stream name
    :return: None
    """
    logger.info(
        "send_log_event log_group_name=%s log_stream_name=%s",
        log_group_name,
        log_stream_name,
    )

    log_message = [{"timestamp": round(time.time() * 1000), "message": message}]

    logger.debug("log_message=%s", log_message)
    response = client.put_log_events(
        logGroupName=log_group_name,
        logStreamName=log_stream_name,
        logEvents=log_message,
    )

    logger.log(LOG_LEVEL_DETAIL, "response=%s", response)


def send_log_events(
    file_name: str, log_group_name: str, log_stream_name: str, max_message_size: int
):
    """
    Send `file_name` to CloudWatch, creating one or more log events in
    `log_stream_name` in `log_group_name. If `log_file` size exceeds
    `max_message_size` the file is sent as multiple events. If the
    length of a single line exceeds `max_message_size` an error is raised.

    :param file_name: The name of the file to send
    :param log_group_name: The CloudWatch log group name
    :param log_stream_name: The CloudWatch log stream name
    :param max_message_size: The maximum size of a single log event message
    :return: None
    """
    logger.info(
        "send_log_events: file_name=%s log_group_name=%s log_stream_name=%s max_message_size=%s",
        file_name,
        log_group_name,
        log_stream_name,
        max_message_size,
    )

    message = ""
    line_count = 0
    log_event_count = 1
    with open(file_name) as f:
        for line in f:
            line_count += 1
            if len(message) + len(line) > max_message_size:
                # Can't send current line in current log event (too long)
                if len(message) == 0:
                    # There was no preceding data, this line is too big
                    raise ValueError(
                        f"Line length > {max_message_size} at line {line_count} of file {file_name}"
                    )

                # Send current log message (without current line)
                send_log_event(
                    message=message,
                    log_group_name=log_group_name,
                    log_stream_name=log_stream_name,
                )

                message = line  # try to send current line in next event
                log_event_count += 1
            else:
                message += line  # send line in current event message
        if len(message) > 0:
            # Send final (or only) log event
            send_log_event(
                message=message,
                log_group_name=log_group_name,
                log_stream_name=log_stream_name,
            )

    logger.info(
        "send_log_events completed OK: log_event_count=%s line_count=%s",
        log_event_count,
        line_count,
    )


def parse_cli_arguments():
    """
    Parse CLI input arguments.
    :return: Parsed input arguments and values.
    """
    parser = argparse.ArgumentParser(description="Send file to CloudWatch")
    parser.add_argument(
        "--log_group", type=str, required=True, help="CloudWatch log group name"
    )
    parser.add_argument(
        "--log_stream", type=str, required=True, help="CloudWatch log stream name"
    )
    parser.add_argument(
        "--max_message_size",
        type=int,
        default=65536,
        help="Maximum size of log event message",
    )
    parser.add_argument(
        "--debug",
        type=int,
        default=0,
        help="Log level number, default is 0: 0=off 10=DEBUG 15=DETAIL 20=INFO",
    )
    parser.add_argument("file", type=str, help="Name of file to be sent to CloudWatch")
    return parser.parse_args()


if __name__ == "__main__":
    """
    Runs if script executed; does not run if script imported.
    """
    args = parse_cli_arguments()

    # Enable log level, unless 0: https://docs.python.org/3/library/logging.html#logging-levels
    if args.debug > 0:
        log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        logging.basicConfig(level=args.debug, format=log_format)

    # Run using CLI arguments
    send_log_events(
        file_name=args.file,
        max_message_size=args.max_message_size,
        log_group_name=args.log_group,
        log_stream_name=args.log_stream,
    )
