REQUIRED_FIELDS = [
    "satellite",
    "energy",
    "imf",
    "bx",
    "by",
    "bz",
    "speed",
    "density",
    "temperature"
]

NUMERIC_FIELDS = [
    "energy",
    "imf",
    "bx",
    "by",
    "bz",
    "speed",
    "density",
    "temperature"
]


def validate_input(data):

    if data is None:
        return False, "No JSON data received."

    for field in REQUIRED_FIELDS:

        if field not in data:
            return False, f"Missing field: {field}"

    if not str(data["satellite"]).strip():
        return False, "Satellite name cannot be empty."

    for field in NUMERIC_FIELDS:

        try:
            data[field] = float(data[field])

        except (ValueError, TypeError):
            return False, f"{field} must be a valid number."

    return True, data