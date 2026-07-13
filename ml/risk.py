def calculate_risk(flux):

    if flux < 0.30:
        return "LOW"

    elif flux < 0.45:
        return "MEDIUM"

    return "HIGH"