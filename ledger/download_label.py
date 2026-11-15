"""Build statement download labels."""
def resolve(value):
    return "Statement · " + value.replace("-", "/")
