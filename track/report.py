from typing import Optional

import typer
from rich import print as rprint

from track import metrics

app = typer.Typer()


@app.callback(invoke_without_command=True)
def default(
    ctx: typer.Context,
    start_date: Optional[str] = typer.Argument(None, help="start date"),
    end_date: Optional[str] = typer.Argument(None, help="end date"),
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
        f"Total Applications: {metrics.num_of_applications(start_date, end_date)}"
    )
