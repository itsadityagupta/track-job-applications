from tests.helpers.mock import get_mock_db_path
from track.app_functions import get_conn_string


def test_get_conn_string(get_mock_db_path):
    """Test the get_conn_string function"""
    db_path: str = get_mock_db_path

    assert not db_path.startswith("sqlite:///")

    conn_string = get_conn_string(db_path)

    assert conn_string.startswith("sqlite:///")
