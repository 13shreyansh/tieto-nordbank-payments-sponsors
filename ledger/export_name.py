"""Keep export filenames safe."""
def resolve(value):
    return "".join(c for c in value if c.isalnum() or c in "-_") + ".csv"
