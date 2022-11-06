from datetime import datetime
from typing import Optional

import typer

from track import app_functions
from track.app_constants import Status
from track.database import Database
from track.job_application import JobApplication


class DBHandler:
    """Class to perform all db operations"""

    def __init__(self, db_path: str, echo: bool):
        self.__db = self.get_db(db_path, echo)

    def get_db(self, db_path: str, echo: bool):
        """Returns a Database instance"""
        return Database(db_path, echo)

    def add_job_application(self, application: JobApplication) -> int:
        """Add a job application to the database"""
        self.__db.session.add(application)
        self.__db.session.commit()
        self.__db.session.refresh(application)
        typer.secho(
            f"Job application added successfully with id {application.id}."
        )
        return application.id
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
                    self.__db.session.query(JobApplication)
                    .filter(
                        JobApplication.applied_at >= start_date,
                        JobApplication.applied_at <= end_date,
                    )
                    .count()
                )
            else:
                return (
                    self.__db.session.query(JobApplication)
                    .filter(
                        JobApplication.applied_at >= start_date,
                        JobApplication.applied_at <= end_date,
                    )
                    .all()
                )
        elif start_date is None and end_date is None:
            if get_counts:
                return self.__db.session.query(JobApplication).count()
            else:
                return self.__db.session.query(JobApplication).all()
        # TODO: Another way is to return only job ids. But check if it's feasible
        # TODO: throw relevant exception

    def delete_job_application(self, application_id: int) -> int:
        """Deletes job application with the given application id."""
        application = (
            self.__db.session.query(JobApplication)
            .filter(JobApplication.id == application_id)
            .one()
        )
        self.__db.session.delete(application)
        self.__db.session.commit()
        typer.secho(f"Job application with id {application_id} deleted.")
        return application.id

    def delete_all(
        self, start_date: Optional[str] = None, end_date: Optional[str] = None
    ) -> list[int]:
        """Deletes all the applications present in a given date range"""
        if start_date is not None and end_date is not None:
            applications = (
                self.__db.session.query(JobApplication)
                .filter(
                    JobApplication.applied_at >= start_date,
                    JobApplication.applied_at <= end_date,
                )
                .all()
            )
            for application in applications:
                self.__db.session.delete(application)
            self.__db.session.commit()
            return [application.id for application in applications]
        elif start_date is None and end_date is None:
            applications = self.__db.session.query(JobApplication).all()
            for application in applications:
                self.__db.session.delete(application)
            self.__db.session.commit()
            return [application.id for application in applications]
        return []

    def update_company(self, application_id: int, company: str):
        """Updates the company name in the application with the given ID"""
        self.__db.session.query(JobApplication).filter(
            JobApplication.id == application_id
        ).update({"company": company, "updated_at": datetime.now().date()})
        self.__db.session.commit()

    def update_position(self, application_id: int, position: str):
        """Updates the position in the application with the given ID"""
        self.__db.session.query(JobApplication).filter(
            JobApplication.id == application_id
        ).update({"position": position, "updated_at": datetime.now().date()})
        self.__db.session.commit()

    def update_status(self, application_id: int, status: str):
        """Updates the status of the application with the given ID"""
        status = Status.from_string(status)
        self.__db.session.query(JobApplication).filter(
            JobApplication.id == application_id
        ).update({"status": status.value, "updated_at": datetime.now().date()})
        self.__db.session.commit()

    def update_applied_at(self, application_id: int, applied_at: str):
        """Updates the applied_at date in the application with the given ID"""
        applied_at = app_functions.parse_date(applied_at)
        self.__db.session.query(JobApplication).filter(
            JobApplication.id == application_id
        ).update(
            {"applied_at": applied_at, "updated_at": datetime.now().date()}
        )
        self.__db.session.commit()

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
                    self.__db.session.query(JobApplication)
                    .filter(
                        JobApplication.status == status.value,
                        start_date <= JobApplication.applied_at,
                        JobApplication.applied_at <= end_date,
                    )
                    .count()
                )
            else:
                return (
                    self.__db.session.query(JobApplication)
                    .filter(
                        JobApplication.status == status.value,
                        start_date <= JobApplication.applied_at,
                        JobApplication.applied_at <= end_date,
                    )
                    .all()
                )
        elif start_date is None and end_date is None:
            if get_counts:
                return (
                    self.__db.session.query(JobApplication)
                    .filter(JobApplication.status == status.value)
                    .count()
                )
            else:
                return (
                    self.__db.session.query(JobApplication)
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
                    self.__db.session.query(JobApplication)
                    .filter(
                        JobApplication.status != Status.REJECTED.value,
                        JobApplication.status != Status.APPLIED.value,
                        JobApplication.applied_at >= start_date,
                        JobApplication.applied_at <= end_date,
                    )
                    .count()
                )
            else:
                return (
                    self.__db.session.query(JobApplication)
                    .filter(
                        JobApplication.status != Status.REJECTED.value,
                        JobApplication.status != Status.APPLIED.value,
                        JobApplication.applied_at >= start_date,
                        JobApplication.applied_at <= end_date,
                    )
                    .all()
                )
        elif start_date is None and end_date is None:
            if get_counts:
                return (
                    self.__db.session.query(JobApplication)
                    .filter(
                        JobApplication.status != Status.REJECTED.value,
                        JobApplication.status != Status.APPLIED.value,
                    )
                    .count()
                )
            else:
                return (
                    self.__db.session.query(JobApplication)
                    .filter(
                        JobApplication.status != Status.REJECTED.value,
                        JobApplication.status != Status.APPLIED.value,
                    )
                    .all()
                )

    def find_application_id(
        self,
        company: str,
        position: str,
        applied_at: str,
        status: str,
        only_ids=False,
    ):
        """Refresh the given application object from database."""
        applications = (
            self.__db.session.query(JobApplication)
            .filter(
                JobApplication.company == company,
                JobApplication.position == position,
                JobApplication.status == status,
                JobApplication.applied_at == applied_at,
            )
            .all()
        )
        if not only_ids:
            return applications
        return [application.id for application in applications]
