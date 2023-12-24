from typing import Optional


def username_validator(username: Optional[str]) -> bool:
    return username and (3 <= len(username) <= 32)


def password_validator(password: Optional[str]) -> bool:
    return password and (6 <= len(password) <= 64)
