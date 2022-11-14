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
    """
    Displays application version.

    Args:
        version: -v or --version flag

    Examples:
        >>>track-job --version
        >>>track-job -v
    """
    return


@app.command()
def add(
    company: str = typer.Argument(..., help="Company applied to"),
    position: str = typer.Argument(..., help="Position applied for"),
    applied_at: str = typer.Option(
        datetime.date(datetime.now()).isoformat(),
        "--applied-at",
        "-a",
        help="Date applied at [YYYY-MM-DD]",
    ),
    status: str = typer.Option(
        "APPLIED", "--status", "-s", help="Current status of the application"
    ),
) -> None:
    """
    Adds a job application.

    Args:
        company: Company name applied to.
        position: Job Post applied to.
        applied_at: Date on which the application was submitted for the given job posting in YYYY-MM-DD format.
            (default: current date)
        status: Application status. For all possible values, check [`Status`][track.app_constants.Status]. (default: `APPLIED`)

    Examples:
        >>>track-job add Company1 Position1
        >>>track-job add Company1 Position2 --applied-at 2022-11-10 --status tech
        >>>track-job add Company1 Position2 -a 2022-11-10 -s offer
    """
    get_tracker().add(company, position, applied_at, status)


@app.command()
def ls(
    start_date: Optional[str] = typer.Option(
        None, "--start-date", "-s", help="Start date in YYYY-MM-DD"
    ),
    end_date: Optional[str] = typer.Option(
        None, "--end-date", "-e", help="End date in YYYY-MM-DD"
    ),
    status: Optional[str] = typer.Option(
        None, "--status", "-st", help="Filter applications by status"
    ),
):
    """
    Lists all the job applications present in the database. (or within a specified date range, if given)

    Args:
        start_date: Start date to display applications (default: None)
        end_date: End date to display applications (default: None)
        status: Filter the applications by status (default: None). Find possible values [here][track.app_constants.from_string]

    Examples:
        >>>track-job ls //displays all the applications
        >>>track-job ls -s 2022-10-12 -e 2022-11-12 //displays all the applications from 2022-10-12 to 2022-11-12

    Notes:
        In case the start and the end dates are given, the applications are filtered using the `applied_at` field.
    """
    get_tracker().list(start_date, end_date, status)
    # TODO: add start and end date along with the status (to filter with the given status)


@app.command()
def rm(
    application_id: int = typer.Argument(
        ..., help="ID for job application you want to delete"
    )
):
    """
    Deletes the job application with the given id.

    Args:
        application_id: ID of an application to be deleted.

    Examples:
        >>>track-job rm 1 //deletes application having ID 1

    Notes:
        The application id can be found using the [ls][track.cli.ls] command.
    """
    get_tracker().delete(application_id)


def entry():
    """Starting point for the application"""
    app()
