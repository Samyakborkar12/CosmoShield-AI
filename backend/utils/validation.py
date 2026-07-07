REQUIRED_FIELDS = [
    "satellite",
    "energy"
]


def validate_input(data):

    if data is None:
        return False, "No JSON data received."

    for field in REQUIRED_FIELDS:

        if field not in data:
            return False, f"Missing field: {field}"

    try:
        data["energy"] = float(data["energy"])
    except (ValueError, TypeError):
        return False, "Energy must be a number."

    return True, data