"""Bound statement page size."""
def resolve(value):
    return min(100, max(1, int(value)))
