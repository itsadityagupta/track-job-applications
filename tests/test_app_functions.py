import datetime
from typing import Any

from _pytest.capture import CaptureFixture

from tests.helpers.mock import get_mock_db_path
from track.app_functions import get_conn_string, parse_date


def test_get_conn_string(get_mock_db_path):
    """Test the get_conn_string function"""
    db_path: str = get_mock_db_path

    assert not db_path.startswith("sqlite:///")

    conn_string = get_conn_string(db_path)

    assert conn_string.startswith("sqlite:///")


def test_parse_date_correct():
    """Test parse_date function with a correct date."""
    correct_date = "2022-10-11"
    result = parse_date(correct_date)

    assert isinstance(result, datetime.date)


def test_parse_date_wrong_format(capsys: CaptureFixture[Any]):
    """Test parse_date function with a date with wrong format."""
    wrong_date = "11-10-2022"
    _ = parse_date(wrong_date)
    out, err = capsys.readouterr()

    assert (
        "Date is invalid or was not specified in the expected format YYYY-MM-DD.\n"
        == out
    )


def test_parse_date_invalid_date(capsys: CaptureFixture[Any]):
    """Test parse_date function with an invalid date."""
    invalid_date = "12345678"
    _ = parse_date(invalid_date)
    out, err = capsys.readouterr()

    assert (
        "Date is invalid or was not specified in the expected format YYYY-MM-DD.\n"
        == out
    )
