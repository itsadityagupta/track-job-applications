import logging
from typing import Any
from unittest.mock import MagicMock

from _pytest.capture import CaptureFixture

from tests.helpers.mock import get_mock_applications, get_mock_db_path
from track.db_handler import DBHandler
from track.job_application import JobApplication


def test_add_application(
    mocker,
    capsys: CaptureFixture[Any],
    get_mock_db_path,
    get_mock_applications,
):
    """Tests the function to add a job application."""
    db_mock = MagicMock()
    sess_mock = MagicMock()
    sess_mock.configure_mock(
        **{
            "add.return_value": None,
            "commit.return_value": None,
            "refresh.return_value": None,
        }
    )
    db_mock.session = sess_mock
    db_path = get_mock_db_path
    mocker.patch("track.db_handler.DBHandler.get_db", return_value=db_mock)

    handler = DBHandler(db_path, False)
    application: JobApplication = get_mock_applications[0]
    application.id = 6

    app_id = handler.add_job_application(application)
    out, err = capsys.readouterr()

    assert app_id == 6
    assert "Job application added successfully with id 6.\n" == out
