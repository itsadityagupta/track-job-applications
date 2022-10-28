from typing import Optional

import typer
from rich import print as rprint

from track import metrics

app = typer.Typer()


@app.callback(invoke_without_command=True)
def default(
    ctx: typer.Context,
    start_date: Optional[str] = typer.Option(None, help="start date"),
    end_date: Optional[str] = typer.Option(None, help="end date"),
):
    """Default report"""
    if ctx.invoked_subcommand is not None:
        return
    metrics.generate_report(start_date, end_date)


@app.command()
def total(
    start_date: Optional[str] = typer.Argument(
        None, help="Start counting the applications from this date"
    ),
    end_date: Optional[str] = typer.Argument(
        None, help="Count the applications made till this date"
    ),
):
    """Get the total number of applications within a given date range"""
    rprint(
        f"# of applications: {metrics.num_of_applications(start_date, end_date)}"
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
    rprint(
        f"# of applications with status '{status}': {metrics.applications_by_status_count(status, start_date, end_date)}"
    )


@app.command()
def ratios(
    start_date: Optional[str] = typer.Argument(None, help="Start date"),
    end_date: Optional[str] = typer.Argument(None, help="End date"),
):
    """Displays all the ratios"""
    ratio_jobs_rejected = metrics.jobs_applied_to_jobs_rejected(
        start_date, end_date
    )
    if ratio_jobs_rejected != "-1":
        rprint("jobs applied : jobs rejected = " + ratio_jobs_rejected)
    else:
        rprint(
            "[green]jobs applied : jobs rejected = N/A since no application is rejected[/green]"
        )
