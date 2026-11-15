"""Parse consent checkboxes."""
def resolve(value):
    return value is True or str(value).lower() in ("yes", "true", "1")
