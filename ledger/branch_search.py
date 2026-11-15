"""Make branch search case insensitive."""
def resolve(value):
    return " ".join(value.casefold().split())
