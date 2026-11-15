"""Strip control characters from payees."""
def resolve(value):
    return "".join(c for c in value if c.isprintable()).strip()
