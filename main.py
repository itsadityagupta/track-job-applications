import os

from database import Database
from datamodels.job_application import JobApplication
from db_functions import DBFunctions

# import typer
#
# app = typer.Typer()
# jobs = []
#
#
# @app.command()
# def add(
#     company: str = typer.Argument(..., help="Company applied to"),
#     position: str = typer.Argument(..., help="Position applied for"),
#     date: str = typer.Argument(
#         datetime.now().strftime("%x"), help="Date applied at"
#     ),
# ):
#     """Add job application details"""
#     jobs.append([company, position, date])

if __name__ == "__main__":
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "site.db")
    obj = Database(path)
    dao = DBFunctions(obj)
    application = JobApplication(
        company="Adobe", position="SDE", status="Applied"
    )
    dao.add_job_application(application)
    # app()
