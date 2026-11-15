"""Transfer fees (REQ-PAY-204)."""
from decimal import Decimal, ROUND_HALF_UP

INSTANT_RATE = Decimal("0.002")  # 0.2 %
INSTANT_MIN_CENTS = 50


def transfer_fee(amount_cents: int, kind: str) -> int:
    """Return the fee in cents for a transfer of the given kind."""
    if kind == "sepa":
        return 0
    if kind == "instant":
        fee = (Decimal(amount_cents) * INSTANT_RATE).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
        return max(int(fee), INSTANT_MIN_CENTS)
    raise ValueError(f"unknown transfer kind {kind}")
