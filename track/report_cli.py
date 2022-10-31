from typing import Optional

import typer

from track.reporter import Reporter

app = typer.Typer()


def get_reporter():
    """Returns an instance of a Reporter class."""
    return Reporter()


@app.callback(invoke_without_command=True)
def default(
    ctx: typer.Context,
    start_date: Optional[str] = typer.Option(None, help="start date"),
    end_date: Optional[str] = typer.Option(None, help="end date"),
):
    """Default report"""
    if ctx.invoked_subcommand is not None:
        return
    get_reporter().generate_report(start_date, end_date)


@app.command()
def counts(
    start_date: Optional[str] = typer.Argument(
        None, help="Start counting the applications from this date"
    ),
    end_date: Optional[str] = typer.Argument(
        None, help="Count the applications made till this date"
    ),
):
    """Get the total number of applications within a given date range"""
    typer.secho(
        f"Total Applications: {get_reporter().total_counts(start_date, end_date)}"
    )


@app.command()
def status(
    status: str = typer.Argument(..., help="Status of the application"),
    start_date: Optional[str] = typer.Argument(
        None, help="Start counting the applications from this date"
    ),
    end_date: Optional[str] = typer.Argument(
        None, help="Count the applications made till this date"
    ),
):
    """Get the counts of application for the given status in the given time range"""
    typer.secho(
        f"Applications with status '{status}' = {get_reporter().status_counts(start_date, end_date)}"
    )


@app.command()
def shortlisted(
    start_date: Optional[str] = typer.Argument(
        None, help="Start counting the applications from this date"
    ),
    end_date: Optional[str] = typer.Argument(
        None, help="Count the applications made till this date"
    ),
):
    """Gets the number of shortlisted applications within a given time range"""
    typer.secho(
        f"Shortlisted Applications = {get_reporter().shortlisted_counts(start_date, end_date)}"
    )


@app.command()
def ratios(
    start_date: Optional[str] = typer.Argument(None, help="Start date"),
    end_date: Optional[str] = typer.Argument(None, help="End date"),
):
    """Displays all the ratios"""
    rejected_ratio, shortlisted_ratio = get_reporter().ratios(
        start_date, end_date
    )
    if rejected_ratio != "-1":
        typer.secho("jobs applied : jobs rejected = " + rejected_ratio)
    else:
        typer.secho(
            "jobs applied : jobs rejected = N/A since no application is rejected.",
            fg="green",
        )
    if shortlisted_ratio != "-1":
        typer.secho("jobs applied : jobs shortlisted = " + shortlisted_ratio)
    else:
        typer.secho(
            "jobs applied : jobs shortlisted = N/A since no application is shortlisted.",
            fg="red",
        )
