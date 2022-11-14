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
    sess_mock = MagicMock()
    sess_mock.configure_mock(
        **{
            "add.return_value": None,
            "commit.return_value": None,
            "refresh.return_value": None,
        }
    )
    db_mock = MagicMock()
    db_mock.session = sess_mock
    db_path = get_mock_db_path
    mocker.patch("track.db_handler.DBHandler.get_db", return_value=db_mock)

    handler = DBHandler(db_path, False)
    application: JobApplication = get_mock_applications[0]
    application.id = 6

    app_id = handler.add_job_application(application)
    out, err = capsys.readouterr()

    assert app_id == 6
    assert "Job application added with id 6.\n" == out


def test_get_all_applications_counts_no_date(mocker, get_mock_db_path):
    """Test get_all_function with retrieving application counts for all the applications."""
    query_mock = MagicMock()
    query_mock.configure_mock(**{"count.return_value": 5})
    sess_mock = MagicMock()
    sess_mock.configure_mock(**{"query.return_value": query_mock})
    db_mock = MagicMock()
    db_mock.session = sess_mock
    db_path = get_mock_db_path
    mocker.patch("track.db_handler.DBHandler.get_db", return_value=db_mock)

    handler = DBHandler(db_path, False)
    result = handler.get_all_applications(get_counts=True)

    assert result == 5


def test_get_all_applications_no_date(
    mocker, get_mock_db_path, get_mock_applications
):
    """Test get_all_function with retrieving all the applications."""
    applications: list[JobApplication] = get_mock_applications
    order_mock = MagicMock()
    order_mock.configure_mock(**{"all.return_value": applications})
    query_mock = MagicMock()
    query_mock.configure_mock(**{"order_by.return_value": order_mock})
    sess_mock = MagicMock()
    sess_mock.configure_mock(**{"query.return_value": query_mock})
    db_mock = MagicMock()
    db_mock.session = sess_mock
    db_path = get_mock_db_path
    mocker.patch("track.db_handler.DBHandler.get_db", return_value=db_mock)

    handler = DBHandler(db_path, False)
    result = handler.get_all_applications()

    assert result == applications


def test_get_all_applications_counts_date_range(mocker, get_mock_db_path):
    """Test get_all_function with retrieving application counts for applications in the specified date range."""
    filter_mock = MagicMock()
    filter_mock.configure_mock(**{"count.return_value": 5})
    query_mock = MagicMock()
    query_mock.configure_mock(**{"filter.return_value": filter_mock})
    sess_mock = MagicMock()
    sess_mock.configure_mock(**{"query.return_value": query_mock})
    db_mock = MagicMock()
    db_mock.session = sess_mock
    db_path = get_mock_db_path
    mocker.patch("track.db_handler.DBHandler.get_db", return_value=db_mock)

    handler = DBHandler(db_path, False)
    result = handler.get_all_applications(
        start_date="2022-10-10", end_date="2022-11-11", get_counts=True
    )

    assert result == 5


def test_get_all_applications_date_range(
    mocker, get_mock_db_path, get_mock_applications
):
    """Test get_all_function with retrieving applications in a given date range."""
    applications: list[JobApplication] = get_mock_applications
    order_mock = MagicMock()
    order_mock.configure_mock(**{"all.return_value": applications})
    filter_mock = MagicMock()
    filter_mock.configure_mock(**{"order_by.return_value": order_mock})
    query_mock = MagicMock()
    query_mock.configure_mock(**{"filter.return_value": filter_mock})
    sess_mock = MagicMock()
    sess_mock.configure_mock(**{"query.return_value": query_mock})
    db_mock = MagicMock()
    db_mock.session = sess_mock
    db_path = get_mock_db_path
    mocker.patch("track.db_handler.DBHandler.get_db", return_value=db_mock)

    handler = DBHandler(db_path, False)
    result = handler.get_all_applications(
        start_date="2022-10-10", end_date="2022-11-11"
    )

    assert result == applications
