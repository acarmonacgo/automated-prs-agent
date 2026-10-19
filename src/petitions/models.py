"""Domain models for petition signatures."""

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, slots=True)
class Signature:
    """A signature collected for a petition."""

    petition_id: int
    email: str
    country_code: str
    signed_at: datetime
