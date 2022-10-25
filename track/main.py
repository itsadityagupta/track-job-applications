from datetime import date, datetime
from typing import Optional

import typer
from rich import print as rprint

from track import __app_name__, __version__, app_functions, report, update
from track.dao import db_service
from track.job_application import JobApplication

app = typer.Typer()

app.add_typer(
    update.app, name="update", help="Updates the job application details"
)

app.add_typer(report.app, name="report", help="Reporting")


def _version_callback(value: bool) -> None:
    """Callback to display application version"""
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def get_version(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    """Display application version"""
    return


@app.command()
def add(
    company: str = typer.Argument(..., help="Company applied to"),
    position: str = typer.Argument(..., help="Position applied for"),
    applied_at: str = typer.Argument(
        datetime.date(datetime.now()).isoformat(),
        help="Date applied at [YYYY-MM-DD]",
    ),
    status: str = typer.Argument(
        "Applied", help="Current status of the application"
    ),
):
    """Add job application details"""

    applied_at = app_functions.parse_date(applied_at)
    application = JobApplication(
        company=company,
        position=position,
        status=status,
        applied_at=applied_at,
    )
    db_service.add_job_application(application)


@app.command()
def ls():
    """Prints all the job applications present in the database"""
    applications = db_service.get_all_applications()
    app_functions.print_applications(applications)


@app.command()
def rm(
    application_id: int = typer.Argument(
        ..., help="ID for job application you want to delete"
    )
):
    """Deletes the job application with the given id"""
    db_service.delete_job_application(application_id)
    rprint(f"Job application [{application_id}] deleted.")


def entry():
    """Starting point for the application"""
    app()
