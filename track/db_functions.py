import os
from datetime import datetime
from typing import Optional

from track import app_functions
from track.app_constants import Status
from track.database import Database
from track.job_application import JobApplication
from track.logger import logger


class DBFunctions:
    """Class to perform all db operations"""

    def __init__(self, db_path: str, echo: bool):
        self.db = Database(db_path, echo)

    def add_job_application(self, application: JobApplication):
        """Add a job application to the database"""
        self.db.session.add(application)
        self.db.session.commit()
        logger.info("Job application added successfully!")
        # TODO: throw relevant exception

    def get_all_applications(
        self,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        get_counts: bool = False,
    ):
        """Queries database to get all the job applications"""
        if start_date is not None and end_date is not None:
            if get_counts:
                return (
                    self.db.session.query(JobApplication)
                    .filter(
                        JobApplication.updated_at >= start_date,
                        JobApplication.updated_at <= end_date,
                    )
                    .count()
                )
            else:
                return (
                    self.db.session.query(JobApplication)
                    .filter(
                        JobApplication.updated_at >= start_date,
                        JobApplication.updated_at <= end_date,
                    )
                    .all()
                )
        elif start_date is None and end_date is None:
            if get_counts:
                return self.db.session.query(JobApplication).count()
            else:
                return self.db.session.query(JobApplication).all()
        # TODO: Another way is to return only job ids. But check if it's feasible
        # TODO: throw relevant exception

    def delete_job_application(self, application_id: int):
        """Deletes job application with the given application id."""
        self.db.session.delete(
            self.db.session.query(JobApplication)
            .filter(JobApplication.id == application_id)
            .one()
        )
        self.db.session.commit()

    def update_company(self, application_id: int, company: str):
        """Updates the company name in the application with the given ID"""
        self.db.session.query(JobApplication).filter(
            JobApplication.id == application_id
        ).update({"company": company, "updated_at": datetime.now().date()})
        self.db.session.commit()

    def update_position(self, application_id: int, position: str):
        """Updates the position in the application with the given ID"""
        self.db.session.query(JobApplication).filter(
            JobApplication.id == application_id
        ).update({"position": position, "updated_at": datetime.now().date()})
        self.db.session.commit()

    def update_status(self, application_id: int, status: str):
        """Updates the status of the application with the given ID"""
        status = Status.from_string(status)
        self.db.session.query(JobApplication).filter(
            JobApplication.id == application_id
        ).update({"status": status.value, "updated_at": datetime.now().date()})
        self.db.session.commit()

    def update_applied_at(self, application_id: int, applied_at: str):
        """Updates the applied_at date in the application with the given ID"""
        applied_at = app_functions.parse_date(applied_at)
        self.db.session.query(JobApplication).filter(
            JobApplication.id == application_id
        ).update(
            {"applied_at": applied_at, "updated_at": datetime.now().date()}
        )
        self.db.session.commit()

    def get_applications_by_status(
        self,
        status: str,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        get_counts: bool = False,
    ):
        """Get the application counts for the given status and given date"""
        status = Status.from_string(status)
        if start_date is not None and end_date is not None:
            start_date = app_functions.parse_date(start_date)
            end_date = app_functions.parse_date(end_date)
            if get_counts:
                return (
                    self.db.session.query(JobApplication)
                    .filter(
                        JobApplication.status == status.value,
                        start_date <= JobApplication.updated_at,
                        JobApplication.updated_at <= end_date,
                    )
                    .count()
                )
            else:
                return (
                    self.db.session.query(JobApplication)
                    .filter(
                        JobApplication.status == status.value,
                        start_date <= JobApplication.updated_at,
                        JobApplication.updated_at <= end_date,
                    )
                    .all()
                )
        elif start_date is None and end_date is None:
            if get_counts:
                return (
                    self.db.session.query(JobApplication)
                    .filter(JobApplication.status == status.value)
                    .count()
                )
            else:
                return (
                    self.db.session.query(JobApplication)
                    .filter(JobApplication.status == status.value)
                    .all()
                )

    def get_shortlisted(
        self,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        get_counts: bool = False,
    ):
        """Fetches shortlisted applications i.e. having status not equal to rejected and applied"""
        if start_date is not None and end_date is not None:
            if get_counts:
                return (
                    self.db.session.query(JobApplication)
                    .filter(
                        JobApplication.status != Status.REJECTED.value,
                        JobApplication.status != Status.APPLIED.value,
                        JobApplication.updated_at >= start_date,
                        JobApplication.updated_at <= end_date,
                    )
                    .count()
                )
            else:
                return (
                    self.db.session.query(JobApplication)
                    .filter(
                        JobApplication.status != Status.REJECTED.value,
                        JobApplication.status != Status.APPLIED.value,
                        JobApplication.updated_at >= start_date,
                        JobApplication.updated_at <= end_date,
                    )
                    .all()
                )
        elif start_date is None and end_date is None:
            if get_counts:
                return (
                    self.db.session.query(JobApplication)
                    .filter(
                        JobApplication.status != Status.REJECTED.value,
                        JobApplication.status != Status.APPLIED.value,
                    )
                    .count()
                )
            else:
                return (
                    self.db.session.query(JobApplication)
                    .filter(
                        JobApplication.status != Status.REJECTED.value,
                        JobApplication.status != Status.APPLIED.value,
                    )
                    .all()
                )
