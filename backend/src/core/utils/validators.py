import re


def is_valid_password(password: str) -> bool:
    """
    Validates whether the password is secure.

    A secure password must contain:
    - At least 8 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one number
    - At least one special character
    """
    password_regex = (
        r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    )
    return bool(re.fullmatch(password_regex, password))
