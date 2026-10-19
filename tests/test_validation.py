"""Tests for signature validation."""

import pytest

from petitions.validation import is_valid_country_code, is_valid_email


@pytest.mark.parametrize(
    ("email", "expected"),
    [
        ("person@example.com", True),
        ("PERSON@EXAMPLE.COM", True),
        ("", False),
        ("person@example", False),
        ("person @example.com", False),
        ("person@@example.com", False),
    ],
)
def test_is_valid_email(email: str, expected: bool) -> None:
    """Email validation handles valid and invalid shapes."""
    assert is_valid_email(email) is expected


@pytest.mark.parametrize(
    ("code", "expected"),
    [
        ("AR", True),
        ("US", True),
        ("ar", False),
        ("Ar", False),
        ("ARG", False),
        ("", False),
        ("12", False),
        ("\u00d1A", False),
    ],
)
def test_is_valid_country_code(code: str, expected: bool) -> None:
    """Country code validation requires two uppercase ASCII letters."""
    assert is_valid_country_code(code) is expected
