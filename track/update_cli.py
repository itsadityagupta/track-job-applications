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
    """Updates the company name in the application with the given ID"""
    get_tracker().update_company(application_id, company)


@app.command()
def position(
    application_id: int = typer.Argument(
        ..., help="ID for job application you want to update"
    ),
    position: str = typer.Argument(..., help="Position applied for"),
):
    """Updates the position in the application with the given ID"""
    get_tracker().update_position(application_id, position)


@app.command()
def status(
    application_id: int = typer.Argument(
        ..., help="ID for job application you want to update"
    ),
    status: str = typer.Argument(..., help="Status of the application"),
):
    """Updates the status of the application with the given ID"""
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
    """Updates the applied_at date in the application with the given ID"""
    get_tracker().update_applied_at(application_id, date)
