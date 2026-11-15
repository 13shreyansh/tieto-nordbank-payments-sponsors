"""Reject empty payment memos."""
def resolve(value):
    return value.strip()[:140] or "Payment"
