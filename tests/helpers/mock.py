import os

import pytest

from track.app_constants import Status
from track.db_handler import DBHandler
from track.job_application import JobApplication
from track.job_tracker import JobTracker


@pytest.fixture
def get_mock_job_tracker(
    db_path: str = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "test_site.db"
    ),
    echo: bool = False,
):
    """Returns an instance of JobTracker class."""
    return JobTracker(db_path, echo)


@pytest.fixture
def get_mock_applications(faker):
    """Returns a list of 10 mock JobApplication mock objects."""
    applications = []
    for _ in range(10):
        company: str = faker.company()
        position: str = faker.job()
        status: Status = faker.enum(Status)
        applied_at: str = faker.date()

        application = JobApplication(
            company=company,
            position=position,
            status=status.value,
            applied_at=applied_at,
        )
        applications.append(application)

    return applications


@pytest.fixture
def get_mock_db_handler(
    db_path: str = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "test_site.db"
    ),
    echo: bool = False,
):
    """Returns an instance of DBHandler class."""
    return DBHandler(db_path, echo)


@pytest.fixture
def get_mock_db_path(faker):
    """Get a mock path for database"""
    return faker.file_path(depth=5, extension="db")
