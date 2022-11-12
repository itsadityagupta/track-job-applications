import pytest
from typer.testing import CliRunner

import track
from tests.helpers.mock import (
    get_mock_applications,
    get_mock_db_handler,
    get_mock_job_tracker,
)
from track import __app_name__, __version__, cli
from track.db_handler import DBHandler
from track.job_application import JobApplication
from track.job_tracker import JobTracker

runner = CliRunner()


@pytest.fixture(autouse=True)
def before_and_after_tests(get_mock_db_handler):
    """Clean up the database before and after running a test."""
    handler: DBHandler = get_mock_db_handler
    handler.delete_all()
    assert handler.get_all_applications(get_counts=True) == 0

    yield

    handler.delete_all()
    assert handler.get_all_applications(get_counts=True) == 0


def test_version():
    """Test the --version command"""
    result = runner.invoke(cli.app, ["--version"])
    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}" in result.stdout


def test_add_application(mocker, get_mock_job_tracker, get_mock_applications):
    """Test the add command"""
    job_tracker: JobTracker = get_mock_job_tracker
    applications: list[JobApplication] = get_mock_applications

    mocker.patch("track.cli.get_tracker", return_value=job_tracker)

    for application in applications:
        result = runner.invoke(
            cli.app,
            [
                "add",
                application.company,
                application.position,
                application.applied_at,
                application.status,
            ],
        )
        assert result.exit_code == 0
        assert "Job application added successfully with id " in result.stdout

    assert job_tracker.db_handler.get_all_applications(get_counts=True) == 10


def test_ls(mocker, get_mock_job_tracker, get_mock_applications):
    """Test the ls command"""
    job_tracker: JobTracker = get_mock_job_tracker
    applications: list[JobApplication] = get_mock_applications

    mocker.patch("track.cli.get_tracker", return_value=job_tracker)

    for application in applications:
        result = runner.invoke(
            cli.app,
            [
                "add",
                application.company,
                application.position,
                application.applied_at,
                application.status,
            ],
        )
        assert result.exit_code == 0
        assert "Job application added successfully with id " in result.stdout

    assert job_tracker.db_handler.get_all_applications(get_counts=True) == 10

    spy = mocker.spy(track.app_functions, "print_applications")
    result = runner.invoke(cli.app, ["ls"])

    assert result.exit_code == 0
    assert spy.call_count == 1


def test_rm(mocker, get_mock_job_tracker, get_mock_applications):
    """Test the rm command"""
    job_tracker: JobTracker = get_mock_job_tracker
    applications: list[JobApplication] = get_mock_applications

    mocker.patch("track.cli.get_tracker", return_value=job_tracker)

    for application in applications:
        result = runner.invoke(
            cli.app,
            [
                "add",
                application.company,
                application.position,
                application.applied_at,
                application.status,
            ],
        )
        assert result.exit_code == 0
        assert "Job application added successfully with id " in result.stdout

    assert job_tracker.db_handler.get_all_applications(get_counts=True) == 10

    for application in applications:
        application_id: int = job_tracker.db_handler.find_application_id(
            application.company,
            application.position,
            application.applied_at,
            application.status,
            only_ids=True,
        )[0]
        result = runner.invoke(cli.app, ["rm", str(application_id)])
        assert result.exit_code == 0
        assert "deleted" in result.stdout
