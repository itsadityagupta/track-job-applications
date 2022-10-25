from typing import Optional

from rich import print as rprint

from track.dao import db_service


def num_of_applications(
    start_date: Optional[str] = None, end_date: Optional[str] = None
):
    """Gets total number of applications from DB."""
    return db_service.total_applications(start_date, end_date)


def generate_report(
    start_date: Optional[str] = None, end_date: Optional[str] = None
):
    """Generate the report with default metrics."""
    rprint(
        "Total Applications: " + str(num_of_applications(start_date, end_date))
    )
