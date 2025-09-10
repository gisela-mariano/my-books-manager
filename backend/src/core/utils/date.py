from datetime import datetime


def format_date_string_to_isoformat(value: str) -> datetime:
    """Format date string to ISO format

    Args:
        value (str): Date string in ISO 8601 format (extended - YYYY-MM-DDTHH:MM:SS.sssZ or date-only YYYY-MM-DD)


    Raises:
        ValueError: Raises if the date format is invalid

    Returns:
        str: date in ISO 8601 format
    """

    if not value:
        return value

    if isinstance(value, str):
        try:
            dt = (
                datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%fZ")
                if "T" in value
                else datetime.strptime(value, "%Y-%m-%d")
            )
            return dt.isoformat()
        except ValueError:
            raise ValueError("Invalid date format. Required format: YYYY-MM-DD")
    return value
