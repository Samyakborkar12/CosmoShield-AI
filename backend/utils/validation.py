def validate_prediction_input(data):
    """
    Validate prediction request data.
    """

    if not data:
        return False, "Request body is empty."

    if "satellite" not in data:
        return False, "Satellite is required."

    if "energy" not in data:
        return False, "Energy is required."

    try:
        data["energy"] = float(data["energy"])
    except (ValueError, TypeError):
        return False, "Energy must be a numeric value."

    return True, data