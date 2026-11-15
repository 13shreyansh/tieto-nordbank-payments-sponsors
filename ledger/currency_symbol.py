"""Show Nordic currency symbols."""
def resolve(value):
    return {"EUR": "€", "SEK": "kr", "NOK": "kr", "DKK": "kr", "ISK": "kr"}.get(value, value)
