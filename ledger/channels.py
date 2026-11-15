"""Deduplicate notification channels."""
def resolve(value):
    return sorted(set(value) & {"email", "push", "sms"})
