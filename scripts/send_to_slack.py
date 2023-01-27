#!/usr/bin/env python3

# Simple commandline tool to send a message to slack.
# usage: send_to_slack.py [-h] -m MESSAGE [-w WEB_HOOK_URL]

# Send message to slack webhook

# optional arguments:
#   -h, --help            show this help message and exit
#   -m MESSAGE, --message MESSAGE
#                         message to send
#   -w WEB_HOOK_URL, --web-hook-url WEB_HOOK_URL
#                         webhook url, can use SLACK_WEBHOOK
import os
import sys
import argparse
from slack_sdk.webhook import WebhookClient


def send_to_slack(message: str, webhook_url: str):
    if not message:
        raise ValueError("Message was none")

    if not webhook_url:
        raise ValueError("webhook_url was none")

    webhook = WebhookClient(webhook_url)

    try:
        response = webhook.send(text=message)
    except Exception as e:
        raise RuntimeError(e)

    if response.status_code != 200 or response.body != "ok":
        raise RuntimeError(
            f"Unexpected Response: {response.status_code} Body: {response.body}"
        )


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Send message to slack webhook")
    parser.add_argument(
        "-m", "--message", help="message to send", type=str, required=True
    )

    parser.add_argument(
        "-w",
        "--web-hook-url",
        help="webhook url, can use SLACK_WEBHOOK",
        type=str,
        default=os.environ.get("SLACK_WEBHOOK"),
    )

    args = parser.parse_args()

    if not args.web_hook_url:
        parser.error("webhook not set")

    try:
        send_to_slack(args.message, args.web_hook_url)
    except ValueError as e:
        sys.exit(e)
    except RuntimeError as e:
        sys.exit(e)
