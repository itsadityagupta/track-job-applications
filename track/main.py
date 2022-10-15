from datetime import datetime

import typer
from rich import print as rprint

from track import update
from track.app_functions import print_applications
from track.dao import db_functions
from track.job_application import JobApplication

app = typer.Typer()

app.add_typer(
    update.app, name="update", help="Updates the job application details"
)


@app.command()
def add(
    company: str = typer.Argument(..., help="Company applied to"),
    position: str = typer.Argument(..., help="Position applied for"),
    status: str = typer.Argument(
        "Applied", help="Current status of the application"
    ),
    applied_at: str = typer.Argument(
        datetime.now().strftime("%x"), help="Date applied at [MM/DD/YY]"
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


@app.command()
def rm(
    application_id: int = typer.Argument(
        ..., help="ID for job application you want to delete"
    )
):
    """Deletes the job application with the given id"""
    db_functions.delete_job_application(application_id)
    rprint(f"Job application [{application_id}] deleted.")


def entry():
    """Starting point for the application"""
    app()
