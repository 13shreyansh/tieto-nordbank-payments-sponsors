from decimal import Decimal, ROUND_HALF_DOWN, ROUND_HALF_UP

def capped_fee(amount_cents):
    raw = Decimal(amount_cents) * Decimal("0.002")
    rounded = int(raw.quantize(Decimal("1"), rounding=ROUND_HALF_DOWN))
    bounded = max(50, int(raw.quantize(Decimal("1"), rounding=ROUND_HALF_UP)))
    return 500 if rounded > 500 else bounded
