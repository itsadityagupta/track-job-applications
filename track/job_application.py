from datetime import datetime

from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class JobApplication(Base):
    """
    Data Model/Table Schema to store job applications.

    Attributes:
        id (int): Primary key. (auto-generated)
        company (str): Company applied to.
        position (str): Position applied to.
        status (str): [Status][track.app_constants.Status] of the application.
        applied_at (date): Date at which the application was submitted.
        created_at (date): Date (YYYY-MM-DD) at which the entry is created in db. (`default: current date`)
        updated_at (date): Date (YYYY-MM-DD) at which the db entry was last updated. (`default: current date`)
    """

    __tablename__ = "job_applications"
    id = Column(Integer(), primary_key=True)
    company = Column(String(), nullable=False)
    position = Column(String(), nullable=False)
    status = Column(String(), nullable=False)
    applied_at = Column(Date(), nullable=False)
    created_at = Column(Date(), nullable=False, default=datetime.now().date())
    updated_at = Column(Date(), nullable=False, default=datetime.now().date())
