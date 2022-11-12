import os
from typing import Optional

import typer

from track import app_constants
from track.app_constants import Status
from track.db_handler import DBHandler


class Reporter:
    """A class that calculates all the supported metrics and generates a report on it."""

    def __init__(
        self,
        db_path: str = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "site.db"
        ),
        echo: bool = False,
    ):
        self.db_handler = DBHandler(db_path, echo)

    def total_counts(
        self, start_date: Optional[str] = None, end_date: Optional[str] = None
    ):
        """Fetches the total number of application in a given date range"""
        return self.db_handler.get_all_applications(
            start_date, end_date, get_counts=True
        )

    def status_counts(
        self,
        status: str,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ):
        """Fetches the number of applications for a given status within a given date range"""
        return self.db_handler.get_applications_by_status(
            status=status,
            start_date=start_date,
            end_date=end_date,
            get_counts=True,
        )

    def shortlisted_counts(
        self, start_date: Optional[str], end_date: Optional[str] = None
    ):
        """Fetches the number of shortlisted applications within a given date range"""
        return self.db_handler.get_shortlisted(
            start_date, end_date, get_counts=True
        )

    def jobs_rejected_to_jobs_applied(
        self, start_date: Optional[str] = None, end_date: Optional[str] = None
    ):
        """Calculates the ratio of number of jobs applied to the number of jobs rejected"""
        jobs_applied = self.db_handler.get_all_applications(
            start_date, end_date, get_counts=True
        )
        if jobs_applied == 0:
            return "-1"

        jobs_rejected = self.db_handler.get_applications_by_status(
            status=Status.REJECTED.value(),
            start_date=start_date,
            end_date=end_date,
            get_counts=True,
        )
        return str(
            round(jobs_rejected / jobs_applied, app_constants.PRECISION)
        )

    def jobs_shortlisted_to_jobs_applied(
        self, start_date: Optional[str] = None, end_date: Optional[str] = None
    ):
        """Calculates the ratio of number of jobs applied to the number of jobs shortlisted"""
        jobs_applied = self.db_handler.get_all_applications(
            start_date, end_date, get_counts=True
        )
        if jobs_applied == 0:
            return "-1"

        jobs_shortlisted = self.db_handler.get_shortlisted(
            start_date, end_date, get_counts=True
        )
        return str(
            round(jobs_shortlisted / jobs_applied, app_constants.PRECISION)
        )

    def ratios(
        self, start_date: Optional[str] = None, end_date: Optional[str] = None
    ):
        """Calculates all the available ratios"""
        return [
            self.jobs_rejected_to_jobs_applied(start_date, end_date),
            self.jobs_shortlisted_to_jobs_applied(start_date, end_date),
        ]

    def generate_report(
        self, start_date: Optional[str] = None, end_date: Optional[str] = None
    ):
        """Generates a report of all the metrics available."""
        ratios = self.ratios(start_date, end_date)

        typer.secho(
            f"Total Applications = {self.total_counts(start_date, end_date)}"
        )
        typer.secho(
            f"Rejected Applications = {self.status_counts(Status.REJECTED.value(), start_date, end_date)}"
        )
        typer.secho(
            f"Shortlisted Applications = {self.shortlisted_counts(start_date, end_date)}"
        )
        if ratios[0] != "-1":
            typer.secho("jobs rejected : jobs applied = " + ratios[0])
        else:
            typer.secho(
                "jobs rejected : jobs applied = UNDEFINED [No applications found]",
                fg="red",
            )
        if ratios[1] != "-1":
            typer.secho("jobs shortlisted : jobs applied = " + ratios[1])
        else:
            typer.secho(
                "jobs shortlisted : jobs applied = UNDEFINED [No applications found]",
                fg="red",
            )
