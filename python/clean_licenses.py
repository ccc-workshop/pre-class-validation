"""Small helpers for cleaning the nightly license extract."""
import csv
from datetime import date


def normalize_status(raw: str) -> str:
    """Return the status in a single consistent form, e.g. ' active ' -> 'ACTIVE'."""
    return (raw or "").strip().upper()


def is_active(row: dict) -> bool:
    """True when the license status is ACTIVE (any casing or spacing)."""
    return normalize_status(row.get("status", "")) == "ACTIVE"


def days_until_expiry(row: dict, today: date) -> int:
    """Days from today until the license expires (negative if already expired)."""
    expires = date.fromisoformat(row["expires_date"])
    return (expires - today).days


def load_licenses(path: str) -> list:
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


if __name__ == "__main__":
    rows = load_licenses("data/sample/licenses_sample.csv")
    active = [r for r in rows if is_active(r)]
    print(f"{len(active)} of {len(rows)} licenses are active")
