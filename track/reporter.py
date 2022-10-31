import os
from typing import Optional

import typer

from track import app_constants
from track.app_constants import Status
from track.db_functions import DBFunctions


class Reporter:
    """A class that calculates all the supported metrics and generates a report on it."""

    def __init__(
        self,
        db_path: str = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "site.db"
        ),
        echo: bool = False,
    ):
        self.db_handler = DBFunctions(db_path, echo)

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

    def jobs_applied_to_jobs_rejected(
        self, start_date: Optional[str] = None, end_date: Optional[str] = None
    ):
        """Calculates the ratio of number of jobs applied to the number of jobs rejected"""
        jobs_applied = self.db_handler.get_all_applications(
            start_date, end_date, get_counts=True
        )
        jobs_rejected = self.db_handler.get_applications_by_status(
            status=Status.REJECTED.value(),
            start_date=start_date,
            end_date=end_date,
            get_counts=True,
        )
        if jobs_rejected == 0:
            return "-1"
        return str(
            round(jobs_applied / jobs_rejected, app_constants.PRECISION)
        )

    def jobs_applied_to_jobs_shortlisted(
        self, start_date: Optional[str] = None, end_date: Optional[str] = None
    ):
        """Calculates the ratio of number of jobs applied to the number of jobs shortlisted"""
        jobs_applied = self.db_handler.get_all_applications(
            start_date, end_date, get_counts=True
        )
        jobs_shortlisted = self.db_handler.get_shortlisted(
            start_date, end_date, get_counts=True
        )
        if jobs_shortlisted == 0:
            return "-1"
        return str(
            round(jobs_applied / jobs_shortlisted, app_constants.PRECISION)
        )

    def ratios(
        self, start_date: Optional[str] = None, end_date: Optional[str] = None
    ):
        """Calculates all the available ratios"""
        return [
            self.jobs_applied_to_jobs_rejected(start_date, end_date),
            self.jobs_applied_to_jobs_shortlisted(start_date, end_date),
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
            typer.secho("jobs applied : jobs rejected = " + ratios[0])
        else:
            typer.secho(
                "jobs applied : jobs rejected = N/A since no application is rejected.",
                fg="green",
            )
        if ratios[1] != "-1":
            typer.secho("jobs applied : jobs shortlisted = " + ratios[1])
        else:
            typer.secho(
                "jobs applied : jobs shortlisted = N/A since no application is shortlisted.",
                fg="red",
            )
