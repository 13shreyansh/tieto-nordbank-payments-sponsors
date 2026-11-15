from decimal import Decimal, ROUND_HALF_UP

def capped_fee(amount_cents):
    return max(50, int((Decimal(amount_cents) * Decimal("0.002")).quantize(Decimal("1"), rounding=ROUND_HALF_UP)))
