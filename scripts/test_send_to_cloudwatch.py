import pytest
from send_to_cloud_watch import *
from freezegun import freeze_time
import localstack_client.session

# log stream "something_stream" exists
# log group "something" exists


@pytest.fixture(autouse=True)
def boto3_localstack_patch(monkeypatch):
    session_ls = localstack_client.session.Session()
    monkeypatch.setattr(boto3, "client", session_ls.client)
    monkeypatch.setattr(boto3, "resource", session_ls.resource)


class TestParamsValid:
    def test_missing_params(self):
        """Expect an ValueError when params are missing"""
        log_group = ""
        log_stream = "foo"
        message = "bar"
        with pytest.raises(ValueError):
            send_to_cloud_watch(log_group, log_stream, message)

        log_group = "foo"
        log_stream = ""
        message = "bar"
        with pytest.raises(ValueError):
            send_to_cloud_watch(log_group, log_stream, message)

        log_group = "foo"
        log_stream = "bar"
        message = ""
        with pytest.raises(ValueError):
            send_to_cloud_watch(log_group, log_stream, message)

        log_group = ""
        log_stream = ""
        message = ""
        with pytest.raises(ValueError):
            send_to_cloud_watch(log_group, log_stream, message)


class TestLogGroupExists:
    def test_log_group_exists_does_not_exist(self):
        log_group = "this_group_does_not_exist"

        assert log_group_exists(log_group) == False

    def test_log_group_exists_does_exist(self):
        log_group = "something"

        assert log_group_exists(log_group) == True


class TestSendToCloudWatch:
    """Send some text and expect it back"""

    def test_send_to_cloud_watch_success(self):
        log_group = "something"
        log_stream = "something_stream"
        message = "this is the message"
        send_to_cloud_watch(log_group, log_stream, message)

    @freeze_time("2023-01-01")
    def test_send_to_cloud_watch_invalid_time_too_old(self):
        """Messages with an invalid timestamp will fail"""
        log_group = "something"
        log_stream = "something_stream"
        message = "this is the message"
        with pytest.raises(RuntimeError):
            send_to_cloud_watch(log_group, log_stream, message)

    def test_send_to_cloud_watch_log_stream_not_exist(self):
        log_group = "something"
        log_stream = "doesn_not_exist"
        message = "this is the message"
        with pytest.raises(RuntimeError):
            send_to_cloud_watch(log_group, log_stream, message)

    def test_send_to_cloud_watch_log_group_not_exist(self):
        log_group = "doesn_not_exist"
        log_stream = "something_stream"
        message = "this is the message"
        with pytest.raises(RuntimeError):
            send_to_cloud_watch(log_group, log_stream, message)
