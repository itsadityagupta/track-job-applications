import os
from datetime import datetime

import typer

from app_functions import print_applications
from database import Database
from datamodels.job_application import JobApplication
from db_functions import DBFunctions

app = typer.Typer()

db_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "site.db")
db = Database(db_path)
db_functions = DBFunctions(db)


@app.command()
def add(
    company: str = typer.Argument(..., help="Company applied to"),
    position: str = typer.Argument(..., help="Position applied for"),
    applied_at: str = typer.Argument(
        datetime.now().strftime("%x"), help="Date applied at [MM/DD/YY]"
    ),
    status: str = typer.Argument(
        "Applied", help="Current status of the application"
    ),
):
    """Add job application details"""

    application = JobApplication(
        company=company,
        position=position,
        status=status,
        applied_at=applied_at,
    )
    db_functions.add_job_application(application)


@app.command()
def ls():
    """Prints all the job applications present in the database"""
    applications = db_functions.get_all_applications()
    print_applications(applications)


if __name__ == "__main__":
    app()
