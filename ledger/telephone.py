"""Normalize Finnish telephone numbers."""
def resolve(value):
    return "+358" + value[1:] if value.startswith("0") else value
