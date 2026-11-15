"""Name settlement weekdays."""
def resolve(value):
    return ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")[value % 7]
