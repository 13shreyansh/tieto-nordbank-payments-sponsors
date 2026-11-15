"""Normalize customer language."""
def resolve(value):
    return value.lower().split("-")[0] if value.lower().split("-")[0] in ("fi", "sv", "nb", "da", "en") else "en"
