"""Validation helpers for signature data."""

import re

EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def is_valid_email(email: str) -> bool:
    """Return whether an email has a basic valid shape."""
    return EMAIL_PATTERN.fullmatch(email) is not None


def is_valid_country_code(code: str) -> bool:
    """Return whether a code is ISO 3166-1 alpha-2 shaped."""
    return len(code) == 2 and code.isascii() and code.isalpha() and code.isupper()
