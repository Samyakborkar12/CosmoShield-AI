def calculate_risk(flux):

    if flux < 1:
        return "Low"

    elif flux < 10:
        return "Moderate"

    elif flux < 100:
        return "High"

    return "Extreme"