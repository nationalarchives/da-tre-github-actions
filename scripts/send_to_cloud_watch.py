#!/usr/bin/env python3
# Simple commandline helper utility to send a single message or file to Cloud Watch logs
# Expects the log stream and group to exists
# Pass the -c flag to create the log stream
# Use use environmental vars: LOG_STREAM_NAME and LOG_GROUP_NAME if set
# usage: send_to_cloud_watch.py [-h] [-g LOG_GROUP] [-s LOG_STREAM] [-c] (-f FILE | -m MESSAGE)
#
# Send entry to Cloud Watch
#
# optional arguments:
#   -h, --help            show this help message and exit
#   -g LOG_GROUP, --log-group LOG_GROUP
#                         log group to send to, can use LOG_GROUP_NAME
#   -s LOG_STREAM, --log-stream LOG_STREAM
#                         log stream name, can use LOG_STREAM_NAME
#   -c, --create-log-stream
#                         Attempt to create the log stream
#   -f FILE, --file FILE  File name to send
#   -m MESSAGE, --message MESSAGE
#                         Message to send

import boto3
import botocore
import sys
import time
import jsonpath_ng
import argparse
import os

JSON_PATH_LOG_GROUP_NAME = "$.logGroups[*].logGroupName"
JSON_PATH_HTTP_RESPONSE = "$.ResponseMetadata.HTTPStatusCode"
JSON_PATH_REJECT_LOG_EVENTS = "$.rejectedLogEventsInfo"


def log_group_exists(log_group: str) -> bool:
    client = boto3.client("logs")

    response_json = client.describe_log_groups(logGroupNamePrefix=log_group)

    # Response should be 200
    response_json_path = jsonpath_ng.parse(JSON_PATH_HTTP_RESPONSE)
    if not 200 == [_.value for _ in response_json_path.find(response_json)][0]:
        raise RuntimeError("Response was not 200")

    # Log group exists?
    log_group_name_json_path = jsonpath_ng.parse(JSON_PATH_LOG_GROUP_NAME)
    return log_group in [_.value for _ in log_group_name_json_path.find(response_json)]


def send_to_cloud_watch(
    log_group: str, log_stream: str, message: str, create_log_stream: bool = False
):
    """Send a single event to CloudWatch logs with the current timestamp"""
    if not all([log_group, log_stream, message]):
        raise ValueError("Missing parameters")

    client = boto3.client("logs")

    # create events
    log_events = [{"timestamp": int(round(time.time() * 1000)), "message": message}]

    try:
        if create_log_stream:
            client.create_log_stream(logGroupName=log_group, logStreamName=log_stream)
        response_json = client.put_log_events(
            logGroupName=log_group, logStreamName=log_stream, logEvents=log_events
        )
    except client.exceptions.ResourceNotFoundException as e:
        raise RuntimeError("Log or stream does not exist")

    except client.exceptions.ResourceAlreadyExistsException as e:
        raise RuntimeError("Log stream already exists")

    # Check rejectedLogEventsInfo dict for presence which means nothing was logged but still returned at 200
    response_rejected_json_path = jsonpath_ng.parse(JSON_PATH_REJECT_LOG_EVENTS)
    if [_.value for _ in response_rejected_json_path.find(response_json)]:
        raise RuntimeError("Rejected timestamp")

    response_json_path = jsonpath_ng.parse(JSON_PATH_HTTP_RESPONSE)
    if not 200 == [_.value for _ in response_json_path.find(response_json)][0]:
        raise RuntimeError("Response was not 200")


if __name__ == "__main__":
    # Get the args
    parser = argparse.ArgumentParser(description="Send entry to Cloud Watch")
    parser.add_argument(
        "-g",
        "--log-group",
        help="log group to send to, can use LOG_GROUP_NAME",
        type=str,
        default=os.environ.get("LOG_GROUP_NAME"),
    )
    parser.add_argument(
        "-s",
        "--log-stream",
        help="log stream name, can use LOG_STREAM_NAME",
        type=str,
        default=os.environ.get("LOG_STREAM_NAME"),
    )

    parser.add_argument(
        "-c",
        "--create-log-stream",
        help="Attempt to create the log stream",
        action="store_true",
        default=False,
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-f", "--file", help="File name to send", type=str)
    group.add_argument("-m", "--message", help="Message to send", type=str)

    args = parser.parse_args()

    # Check to make sure LOG_GROUP_NAME and LOG_STREAM_NAME were not None if found
    if not all([args.log_stream, args.log_group]):
        parser.error("log-group or log-stream was not set")

    # print(f"Got {args}")

    # If -f then dump the file to a str
    message = ""
    if args.file:
        try:
            with open(args.file) as f:
                message = f.read()
        except Exception as e:
            sys.exit(e)
    else:
        message = args.message

    try:
        send_to_cloud_watch(
            args.log_group, args.log_stream, message, args.create_log_stream
        )
    except ValueError as e:
        sys.exit(e)
    except RuntimeError as e:
        sys.exit(e)
