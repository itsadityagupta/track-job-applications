from typing import Optional

from rich import print as rprint

from track import app_constants
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


def jobs_applied_to_jobs_rejected(
    start_date: Optional[str] = None, end_date: Optional[str] = None
):
    """Ratio of Jobs applied to Jobs Rejected"""
    jobs_applied = num_of_applications(start_date, end_date)
    jobs_rejected = applications_by_status_count(
        Status.REJECTED.value, start_date, end_date
    )
    if jobs_rejected == 0:
        return "-1"
    return str(round(jobs_applied / jobs_rejected, app_constants.PRECISION))


def generate_report(
    start_date: Optional[str] = None, end_date: Optional[str] = None
):
    """Generate the report with default metrics."""
    rprint(
        "# of applications = " + str(num_of_applications(start_date, end_date))
    )
    rprint(
        "# of applications rejected = "
        + str(
            db_service.get_applications_by_status(
                Status.REJECTED, start_date, end_date
            )
        )
    )
    ratio_jobs_rejected = jobs_applied_to_jobs_rejected(start_date, end_date)
    if ratio_jobs_rejected != "-1":
        rprint("jobs applied : jobs rejected = " + ratio_jobs_rejected)
    else:
        rprint(
            "[green]jobs applied : jobs rejected = N/A since no application is rejected[/green]"
        )
