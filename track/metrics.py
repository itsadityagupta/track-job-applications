from rich.console import Console
from rich.table import Table

from track.dao import db_service


def num_of_applications():
    """Gets total number of applications from DB."""
    return db_service.total_applications()


def generate_report():
    """Generate the report with default metrics."""
    console = Console()

    table = Table(title="Report", style="yellow")
    table.add_column("Metrics")
    table.add_column("Value")

    table.add_row("Total Applications", str(num_of_applications()))

    console.print(table)
