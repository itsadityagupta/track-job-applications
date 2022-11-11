import typer

from track.job_tracker import JobTracker

app = typer.Typer()


def get_tracker():
    """Returns an instance of the JobTracker class."""
    return JobTracker()


@app.command()
def company(
    application_id: int = typer.Argument(
        ..., help="ID for job application you want to update"
    ),
    company: str = typer.Argument(..., help="Company name"),
):
    """
    Updates the company name in the application with the given ID.

    Args:
        application_id: Application ID for which to update company name.
        company: New company name to be updated.

    Examples:
        >>>track-job update company 1 newCompany
    """
    get_tracker().update_company(application_id, company)


@app.command()
def position(
    application_id: int = typer.Argument(
        ..., help="ID for job application you want to update"
    ),
    position: str = typer.Argument(..., help="Position applied for"),
):
    """
    Updates the position in the application with the given ID.

    Args:
        application_id: Application ID for which to update the position.
        position: New position to be updated.

    Examples:
        >>>track-job update position 1 SDE-3
    """
    get_tracker().update_position(application_id, position)


@app.command()
def status(
    application_id: int = typer.Argument(
        ..., help="ID for job application you want to update"
    ),
    status: str = typer.Argument(..., help="Status of the application"),
):
    """
    Updates the status of the application with the given ID.

    Args:
        application_id: Application ID for which to update the status.
        status: Status to be updated.

    Examples:
        >>>track-job update status 1 offer
    """
    get_tracker().update_status(application_id, status)


@app.command()
def applied_at(
    application_id: int = typer.Argument(
        ..., help="ID for job application you want to update"
    ),
    date: str = typer.Argument(
        ..., help="Date at which applied for the application"
    ),
):
    """
    Updates the applied_at date in the application with the given ID.

    Args:
        application_id: Application ID for which to update the `applied_at` date.
        date: New `applied_at` date value.

    Examples:
        >>>track-job update applied_at 1 2022-11-10
    """
    get_tracker().update_applied_at(application_id, date)
