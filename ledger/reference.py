"""Normalize payment references."""
def resolve(value):
    return "".join(value.split()).upper()
