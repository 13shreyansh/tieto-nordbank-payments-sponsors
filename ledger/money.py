"""Money helpers. All amounts are integer cents; never use float for money."""
from decimal import Decimal, ROUND_HALF_UP

CURRENCIES = {"EUR": "€"}


def to_cents(text: str) -> int:
    """Parse a user-entered amount like '12.34' into integer cents."""
    value = Decimal(text.strip().replace(",", "."))
    if value <= 0:
        raise ValueError("amount must be positive")
    return int((value * 100).quantize(Decimal("1"), rounding=ROUND_HALF_UP))


def format_amount(cents: int, currency: str = "EUR") -> str:
    """Format cents for display, e.g. 123456 -> '€1,234.56'."""
    if currency not in CURRENCIES:
        raise ValueError(f"unsupported currency {currency}")
    sign = "-" if cents < 0 else ""
    whole, frac = divmod(abs(cents), 100)
    return f"{sign}{CURRENCIES[currency]}{whole:,}.{frac:02d}"
