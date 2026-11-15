"""Mask account numbers."""
def resolve(value):
    return value[:4] + "*" * max(0, len(value)-8) + value[-4:]
