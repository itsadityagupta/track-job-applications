from rich.console import Console
from rich.table import Table


def get_conn_string(db_path: str):
    """Generate a connection string for the database"""
    return "sqlite:///" + db_path


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
            str(application.id),  # int is not renderable in rich
            application.company,
            application.position,
            application.status,
            application.applied_at,
            application.updated_at,
        )

    console.print(table)
