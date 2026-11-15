"""Label pending transfers."""
def resolve(value):
    return {"P": "Pending", "S": "Settled", "R": "Rejected"}.get(value, "Unknown")
