"""Tests for signature statistics."""

from datetime import UTC, datetime, timedelta

from petitions.models import Signature
from petitions.stats import count_by_petition, deduplicate

SIGNED_AT = datetime(2026, 10, 19, 12, 0, tzinfo=UTC)


def make_signature(
    petition_id: int,
    email: str,
    *,
    signed_at: datetime = SIGNED_AT,
) -> Signature:
    """Create a signature fixture."""
    return Signature(
        petition_id=petition_id,
        email=email,
        country_code="AR",
        signed_at=signed_at,
    )


def test_count_by_petition_groups_signatures() -> None:
    """Signatures are counted independently for each petition."""
    signatures = [
        make_signature(1, "one@example.com"),
        make_signature(1, "two@example.com"),
        make_signature(2, "one@example.com"),
    ]

    assert count_by_petition(signatures) == {1: 2, 2: 1}


def test_count_by_petition_accepts_empty_iterable() -> None:
    """An empty iterable produces no counts."""
    assert count_by_petition([]) == {}


def test_deduplicate_ignores_email_case_and_keeps_first() -> None:
    """Duplicate emails within a petition keep their first signature."""
    first = make_signature(1, "Person@example.com")
    duplicate = make_signature(
        1,
        "person@EXAMPLE.COM",
        signed_at=SIGNED_AT + timedelta(minutes=1),
    )
    other_petition = make_signature(2, "PERSON@example.com")

    assert deduplicate([first, duplicate, other_petition]) == [first, other_petition]


def test_deduplicate_accepts_empty_iterable() -> None:
    """An empty iterable produces an empty list."""
    assert deduplicate([]) == []
