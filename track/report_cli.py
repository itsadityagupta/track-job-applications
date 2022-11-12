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
    start_date: Optional[str] = typer.Option(
        None, "--start-date", "-s", help="start date"
    ),
    end_date: Optional[str] = typer.Option(
        None, "--end-date", "-e", help="end date"
    ),
):
    """
    Generate a report for all the applications (or in the given date range). This is called implicitly when no sub-command is provided to the `report` command.

    Args:
        ctx: Typer context. Provided by typer implicitly.
        start_date: Start date to filter applications. (default: None)
        end_date: End date to filter applications. (default: None)

    Examples:
        >>>track-job report //generates report for all the applications
        >>>track-job report -s 2022-10-12 -e 2022-11-12 //for the given date range
    """
    if ctx.invoked_subcommand is not None:
        return
    get_reporter().generate_report(start_date, end_date)


@app.command()
def counts(
    start_date: Optional[str] = typer.Option(
        None,
        "--start-date",
        "-s",
        help="Start counting the applications from this date",
    ),
    end_date: Optional[str] = typer.Option(
        None,
        "--end-date",
        "-e",
        help="Count the applications made till this date",
    ),
):
    """
    Get the total number of applications, or within a given date range.

    Args:
        start_date: Start date to count applications. (default: None)
        end_date: End date to count applications. (default: None)

    Examples:
        >>>track-job report counts //count of all the applications present
        >>>track-job report counts -s 2022-10-12 -e 2022-11-12
    """
    typer.secho(
        f"Total Applications: {get_reporter().total_counts(start_date, end_date)}"
    )


@app.command()
def status(
    status: str = typer.Argument(..., help="Status of the application"),
    start_date: Optional[str] = typer.Option(
        None,
        "--start-date",
        "-s",
        help="Start counting the applications from this date",
    ),
    end_date: Optional[str] = typer.Option(
        None,
        "--end-date",
        "-e",
        help="Count the applications made till this date",
    ),
):
    """
    Get the counts of application for the given status in the given time range. By default, it'll count all the applications with the given status.

    Args:
        status: The Status for which to calculate the application counts. See [Status][track.app_constants.Status] for possible valyes.
        start_date: Start date to count applications. (default: None)
        end_date: End date to count applications. (default: None)

    Examples:
        >>>track-job report status applied
        >>>track-job report status tech-interview -s 2022-10-12 -e 2022-11-12
    """
    typer.secho(
        f"Applications with status '{status}' = {get_reporter().status_counts(start_date, end_date)}"
    )


@app.command()
def shortlisted(
    start_date: Optional[str] = typer.Option(
        None,
        "--start-date",
        "-s",
        help="Start counting the applications from this date",
    ),
    end_date: Optional[str] = typer.Option(
        None,
        "--end-date",
        "-e",
        help="Count the applications made till this date.",
    ),
):
    """
    Gets the number of shortlisted applications within a given time range.

    Args:
        start_date: Start date to count applications. (default: None)
        end_date: End date to count applications. (default: None)

    Examples:
        >>>track-job report shortlisted
        >>>track-job report shortlisted -s 2022-10-12 -e 2022-11-12

    Notes:
        Any application which has a status other than `Applied` and `Rejected` will be considered as shortlisted.
    """
    typer.secho(
        f"Shortlisted Applications = {get_reporter().shortlisted_counts(start_date, end_date)}"
    )


@app.command()
def ratios(
    start_date: Optional[str] = typer.Option(
        None, "--start-date", "-s", help="Start date"
    ),
    end_date: Optional[str] = typer.Option(
        None, "--end-date", "-e", help="End date"
    ),
):
    """
    Displays all the ratios.

    Args:
        start_date: Start date to count applications. (default: None)
        end_date: End date to count applications. (default: None)

    Examples:
        >>>track-job report ratios
        >>>track-job report ratios -s 2022-10-12 -e 2022-11-12
    """
    rejected_ratio, shortlisted_ratio = get_reporter().ratios(
        start_date, end_date
    )
    if rejected_ratio != "-1":
        typer.secho("jobs rejected : jobs applied = " + rejected_ratio)
    else:
        typer.secho(
            "jobs rejected : jobs applied = UNDEFINED [No applications found]",
            fg="red",
        )
    if shortlisted_ratio != "-1":
        typer.secho("jobs shortlisted : jobs applied = " + shortlisted_ratio)
    else:
        typer.secho(
            "jobs shortlisted : jobs applied = UNDEFINED [No applications found]",
            fg="red",
        )
