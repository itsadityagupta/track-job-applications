from datetime import datetime
from typing import Optional

import typer

from track import __app_name__, __version__, report_cli, update_cli
from track.job_tracker import JobTracker

app = typer.Typer()

app.add_typer(
    update_cli.app, name="update", help="Updates the job application details"
)

app.add_typer(report_cli.app, name="report", help="Reporting")


def get_tracker():
    """Returns an instance of the JobTracker class."""
    return JobTracker()


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
        "APPLIED", help="Current status of the application"
    ),
):
    """Add job application details"""
    get_tracker().add(company, position, applied_at, status)


@app.command()
def ls(
    start_date: Optional[str] = typer.Argument(None, help="Start date"),
    end_date: Optional[str] = typer.Argument(None, help="End date"),
):
    """Prints all the job applications present in the database"""
    get_tracker().list(start_date, end_date)
    # TODO: add start and end date along with the status (to filter with the given status)


@app.command()
def rm(
    application_id: int = typer.Argument(
        ..., help="ID for job application you want to delete"
    )
):
    """Deletes the job application with the given id"""
    get_tracker().delete(application_id)


def entry():
    """Starting point for the application"""
    app()
