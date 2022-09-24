from datetime import datetime

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class JobApplication(Base):
    """Data Model/Table Schema to store job applications"""

    __tablename__ = "job_applications"
    id = Column(Integer(), primary_key=True)
    company = Column(String(), nullable=False)
    position = Column(String(), nullable=False)
    status = Column(String(), nullable=False)
    applied_at = Column(
        String(), nullable=False, default=datetime.now().strftime("%x")
    )
    created_at = Column(
        String(), nullable=False, default=datetime.now().strftime("%x")
    )
    updated_at = Column(
        String(), nullable=False, default=datetime.now().strftime("%x")
    )
