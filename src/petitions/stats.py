"""Aggregation helpers for petition signatures."""

from collections.abc import Iterable

from petitions.models import Signature


def count_by_petition(signatures: Iterable[Signature]) -> dict[int, int]:
    """Count signatures grouped by petition identifier."""
    counts: dict[int, int] = {}
    for signature in signatures:
        counts[signature.petition_id] = counts.get(signature.petition_id, 0) + 1
    return counts


def deduplicate(signatures: Iterable[Signature]) -> list[Signature]:
    """Keep the first signature for each petition and case-insensitive email."""
    unique: list[Signature] = []
    seen: set[tuple[int, str]] = set()

    for signature in signatures:
        key = (signature.petition_id, signature.email.casefold())
        if key not in seen:
            seen.add(key)
            unique.append(signature)

    return unique
