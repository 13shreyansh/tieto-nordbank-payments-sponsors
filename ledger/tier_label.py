"""Show account tier names."""
def resolve(value):
    return {"basic": "Everyday", "premium": "Premium", "business": "Business"}.get(value, "Everyday")
