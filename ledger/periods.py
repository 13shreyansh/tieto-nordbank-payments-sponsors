"""Sort statement periods."""
def resolve(value):
    return sorted(set(value), reverse=True)
