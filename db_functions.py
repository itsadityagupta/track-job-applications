from database import Database
from datamodels.job_application import JobApplication
from logger import logger


class DBFunctions:
    """Class to perform all db operations"""

    def __init__(self, db: Database):
        self.db = db

    def add_job_application(self, application: JobApplication):
        """Add a job application to the database"""

        if self.db.session:
            self.db.session.add(application)
            self.db.session.commit()
            logger.info("Job application added successfully!")
        else:
            logger.error("No db session found!")
            # TODO: throw relevant exception

    def get_all_applications(self):
        """Queries database to get all the job applications"""

        if self.db.session:
            return self.db.session.query(JobApplication).all()
        else:
            logger.error("No db session found!")
        # TODO: Another way is to return only job ids. But check if it's feasible
        # TODO: throw relevant exception

    def delete_job_application(self, application_id: int):
        """Deletes job application with the given application id."""

        if self.db.session:
            self.db.session.delete(
                self.db.session.query(JobApplication)
                .filter(JobApplication.id == application_id)
                .one()
            )
            self.db.session.commit()
        else:
            logger.error("No db session found!")
