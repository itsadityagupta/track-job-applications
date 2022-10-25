from enum import Enum

DATE_FORMAT: str = "%Y-%m-%d"


class Status(Enum):
    """Values for Status"""

    APPLIED = "APPLIED"
    OA = "ONLINE_ASSESSMENT"
    TECH_INTERVIEW = "TECH_INTERVIEW"
    HR_ROUND = "HR_ROUND"
    REJECTED = "REJECTED"

    @staticmethod
    def from_string(status: str):
        """Parse the given string to corresponding Enum value"""

        if status.upper() == "APPLIED":
            return Status.APPLIED
        elif status.upper() == "ONLINE_ASSESSMENT":
            return Status.OA
        elif status.upper() == "TECH_INTERVIEW":
            return Status.TECH_INTERVIEW
        elif status.upper() == "HR_ROUND":
            return Status.HR_ROUND
        elif status.upper() == "REJECTED":
            return Status.REJECTED
        else:
            raise ValueError("Not a Valid Status")
