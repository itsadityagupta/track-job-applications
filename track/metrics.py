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


def jobs_rejected_counts(
    start_date: Optional[str] = None, end_date: Optional[str] = None
):
    """Get the number of rejected applications."""
    return db_service.get_applications_by_status(
        Status.REJECTED, start_date, end_date
    )


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
    jobs_rejected = jobs_rejected_counts(start_date, end_date)
    if jobs_rejected == 0:
        return "-1"
    return str(round(jobs_applied / jobs_rejected, app_constants.PRECISION))


def get_shortlisted_applications(
    get_counts: bool,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
):
    """Gets shortlisted applications from DB"""
    return db_service.get_shortlisted(start_date, end_date, get_counts)


def jobs_applied_to_jobs_shortlisted(
    counts: bool,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
):
    """Ratio of jobs applied to Jobs shortlisted"""
    jobs_applied = num_of_applications(start_date, end_date)
    jobs_shortlisted = get_shortlisted_applications(
        get_counts=counts, start_date=start_date, end_date=end_date
    )
    if jobs_shortlisted == 0:
        return "-1"
    return str(round(jobs_applied / jobs_shortlisted, app_constants.PRECISION))


def generate_report(
    start_date: Optional[str] = None, end_date: Optional[str] = None
):
    """Generate the report with default metrics."""
    rprint(
        "# of applications = " + str(num_of_applications(start_date, end_date))
    )
    rprint(
        "# of applications rejected = "
        + str(jobs_rejected_counts(start_date, end_date))
    )
    rprint(
        "# of shortlisted applications = "
        + str(
            get_shortlisted_applications(
                get_counts=True, start_date=start_date, end_date=end_date
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

    ratio_jobs_shortlisted = jobs_applied_to_jobs_shortlisted(
        start_date=start_date, end_date=end_date, counts=True
    )
    if ratio_jobs_shortlisted != "-1":
        rprint("jobs applied : jobs shortlisted = " + ratio_jobs_shortlisted)
    else:
        rprint(
            "[red]jobs applied : jobs rejected = N/A since no application is shortlisted.[/red]"
        )
