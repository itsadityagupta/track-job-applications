from datetime import datetime

import typer

app = typer.Typer()
jobs = []


@app.command()
def add(
    company: str = typer.Argument(..., help="Company applied to"),
    position: str = typer.Argument(..., help="Position applied for"),
    date: str = typer.Argument(
        datetime.now().strftime("%x"), help="Date applied at"
    ),
):
    """Add job application details"""
    jobs.append([company, position, date])


if __name__ == "__main__":
    app()
