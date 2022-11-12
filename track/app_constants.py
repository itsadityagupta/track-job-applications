from enum import Enum

DATE_FORMAT: str = "%Y-%m-%d"
PRECISION: int = 2


class Status(Enum):
    """
    Enum for application Status. It can be `APPLIED`, `OA`, `TECH_INTERVIEW`, `HR_ROUND`, `REJECTED` or `OFFER`.

    A list of possible values that user can enter for it can be seen [here][track.app_constants.from_string].
    """

    APPLIED = "APPLIED"
    OA = "ONLINE_ASSESSMENT"
    TECH_INTERVIEW = "TECH_INTERVIEW"
    HR_ROUND = "HR_ROUND"
    REJECTED = "REJECTED"
    OFFER = "OFFER"


def from_string(status: str) -> Status:
    """
    Parse the given string to the corresponding `Status` Enum value. Only the values mentioned in the source code below
    for each status will be allowed and converted to the corresponding Enum value.

    Args:
        status: Status value in `str`.

    Returns:
        Status: Corresponding Enum value for the given string
    """
    if status.upper() == "APPLIED":
        return Status.APPLIED
    elif status.upper() in [
        "ONLINE_ASSESSMENT",
        "ONLINE ASSESSMENT",
        "OA",
        "ONLINE-ASSESSMENT",
    ]:
        return Status.OA
    elif status.upper() in [
        "TECH_INTERVIEW",
        "TECH INTERVIEW",
        "TECH-INTERVIEW",
        "TECH ROUND",
        "TECH_ROUND",
        "TECH-ROUND",
        "TECH",
    ]:
        return Status.TECH_INTERVIEW
    elif status.upper() in ["HR_ROUND", "HR ROUND", "HR-ROUND"]:
        return Status.HR_ROUND
    elif status.upper() in ["REJECTED"]:
        return Status.REJECTED
    elif status.upper() in ["OFFER", "SELECTED"]:
        return Status.OFFER
    else:
        raise ValueError(f"'{status}' is not a Valid Status")
