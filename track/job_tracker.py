import os
from typing import Optional

from track import app_functions
from track.app_constants import Status
from track.db_handler import DBHandler
from track.job_application import JobApplication


class JobTracker:
    """A class to track job applications."""

    def __init__(
        self,
        db_path: str = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "site.db"
        ),
        echo: bool = False,
    ):
        self.db_handler = DBHandler(db_path, echo)

    def add(self, company: str, position: str, applied_at: str, status: str):
        """Add job application details"""
        applied_at = app_functions.parse_date(applied_at)
        application = JobApplication(
            company=company,
            position=position,
            status=Status.from_string(
                status
            ).value,  # validate the given status
            applied_at=applied_at,
        )
        return self.db_handler.add_job_application(application)

    def list(
        self, start_date: Optional[str] = None, end_date: Optional[str] = None
    ):
        """Prints all the job applications present in the database"""
        applications = self.db_handler.get_all_applications(
            start_date, end_date
        )
        app_functions.print_applications(applications)
        return len(applications)

    def delete(self, application_id: int):
        """Deletes the job application with the given id"""
        return self.db_handler.delete_job_application(application_id)

    def update_company(self, application_id: int, company_name: str):
        """Updates the company name in the application with the given ID"""
        self.db_handler.update_company(application_id, company_name)

    def update_position(self, application_id: int, position: str):
        """Updates the position in the application with the given ID"""
        self.db_handler.update_position(application_id, position)

    def update_status(self, application_id: int, status: str):
        """Updates the status of the application with the given ID"""
        self.db_handler.update_status(application_id, status)

    def update_applied_at(self, application_id: int, applied_at: str):
        """Updates the applied_at date in the application with the given ID"""
        self.db_handler.update_applied_at(application_id, applied_at)
