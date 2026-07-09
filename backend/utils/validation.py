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


def validate_input(data):

    if data is None:
        return False, "No JSON data received."

    for field in REQUIRED_FIELDS:

        if field not in data:
            return False, f"Missing field: {field}"

    numeric_fields = [
        "energy",
        "imf",
        "bx",
        "by",
        "bz",
        "speed",
        "density",
        "temperature"
    ]

    for field in numeric_fields:

        try:
            data[field] = float(data[field])

        except (ValueError, TypeError):

            return False, f"{field} must be numeric."

    return True, data