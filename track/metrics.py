from typing import Optional

from rich import print as rprint

from track.app_constants import Status
from track.dao import db_service


def num_of_applications(
    start_date: Optional[str] = None, end_date: Optional[str] = None
):
    """Gets total number of applications from DB."""
    return db_service.total_applications(start_date, end_date)


def applications_by_status_count(
    status: str,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
):
    """Get the number of applications for the given status, in a given time range"""
    return db_service.get_applications_by_status(
        Status.from_string(status), start_date, end_date
    )


def generate_report(
    start_date: Optional[str] = None, end_date: Optional[str] = None
):
    """Generate the report with default metrics."""
    rprint(
        "# of applications: " + str(num_of_applications(start_date, end_date))
    )
    rprint(
        "# of applications rejected: "
        + str(
            db_service.get_applications_by_status(
                Status.REJECTED, start_date, end_date
            )
        )
    )
