import traceback
from datetime import datetime

import typer
from rich import print as rprint
from rich.console import Console
from rich.table import Table

from track.app_constants import DATE_FORMAT


def get_conn_string(db_path: str):
    """Generate a connection string for the database"""
    return "sqlite:///" + db_path


def parse_date(date: str):
    """Parse the given string to a date object"""
    try:
        return datetime.strptime(date, DATE_FORMAT).date()
    except ValueError:
        rprint(
            "[red]Date is invalid or was not specified in the expected format[/red][yellow] YYYY-MM-DD.[/yellow]"
        )
        raise typer.Exit(1)
    except Exception:
        rprint(
            f"[red]Something went wrong while parsing the date: {date}[/red]: {traceback.print_exc()}"  # traceback.print_exc will print the stack trace of the last exception occurred.
        )
        raise typer.Exit(1)


def validate_dates(start_date, end_date):
    """Validate the start and the end date."""
    if end_date < start_date:
        typer.secho(
            f"Start date {start_date} is greater than the end date {end_date}.",
            fg=typer.colors.BRIGHT_RED,
        )
        raise typer.Exit(1)
    return True


def print_applications(applications):
    """Use rich to print applications in table format"""

    console = Console()

    table = Table(title="Job Applications", style="yellow")
    table.add_column("ID", style="cyan")
    table.add_column("Company", style="magenta")
    table.add_column("Position")
    table.add_column("Status")
    table.add_column("Applied at")
    table.add_column("Updated at")

    for application in applications:
        table.add_row(
            str(application.id),  # int can't be rendered in rich
            application.company,
            application.position,
            application.status,
            str(application.applied_at),  # date can't be rendered in rich
            str(application.updated_at),
        )

    console.print(table)
