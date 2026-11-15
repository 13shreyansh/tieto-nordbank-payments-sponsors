"""Format Finnish statement dates."""
def resolve(value):
    return ".".join(reversed(value.split("-")))
