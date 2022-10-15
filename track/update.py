import typer

from track.dao import db_functions

app = typer.Typer()


@app.command()
def company(
    application_id: int = typer.Argument(
        ..., help="ID for job application you want to update"
    ),
    company_name: str = typer.Argument(..., help="Company name"),
):
    """Updates the company name in the application with the given ID"""
    db_functions.update_company(application_id, company_name)


@app.command()
def position(
    application_id: int = typer.Argument(
        ..., help="ID for job application you want to update"
    ),
    position_name: str = typer.Argument(..., help="Position applied for"),
):
    """Updates the position in the application with the given ID"""
    db_functions.update_position(application_id, position_name)


@app.command()
def status(
    application_id: int = typer.Argument(
        ..., help="ID for job application you want to update"
    ),
    status_name: str = typer.Argument(..., help="Status of the application"),
):
    """Updates the status of the application with the given ID"""
    db_functions.update_status(application_id, status_name)


@app.command()
def applied_at(
    application_id: int = typer.Argument(
        ..., help="ID for job application you want to update"
    ),
    applied_at_value: str = typer.Argument(
        ..., help="Date at which applied for the application"
    ),
):
    """Updates the applied_at date in the application with the given ID"""
    db_functions.update_applied_at_date(application_id, applied_at_value)
