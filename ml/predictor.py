def predict(model, data):

    energy = data["energy"]

    if energy < 3:
        radiation = 2.15
        risk = "Low"

    elif energy < 7:
        radiation = 5.72
        risk = "Medium"

    else:
        radiation = 9.84
        risk = "High"

    return {
        "model": model,
        "radiation": radiation,
        "risk": risk
    }