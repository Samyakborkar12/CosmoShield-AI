import numpy as np

from ml.config import SEQUENCE_LENGTH
from ml.loader import load_ml_assets
from ml.risk import calculate_risk


def predict(data):

    model, scaler = load_ml_assets()

    X = np.array([[
        data["imf"],
        data["bx"],
        data["by"],
        data["bz"],
        data["speed"],
        data["density"],
        data["temperature"]
    ]], dtype=float)

    print("\n========== INPUT ==========")
    print(X)

    X = scaler.transform(X)

    print("\n===== AFTER SCALING =====")
    print(X)

    X = np.repeat(X, SEQUENCE_LENGTH, axis=0)

    X = X.reshape((1, SEQUENCE_LENGTH, 7))

    print("\n===== MODEL INPUT SHAPE =====")
    print(X.shape)

    prediction = model.predict(X, verbose=0)

    print("\n===== RAW MODEL OUTPUT =====")
    print(prediction)

    radiation = float(prediction[0][0])

    print("\n===== FINAL RADIATION =====")
    print(radiation)

    risk = calculate_risk(radiation)

    return {
        "model": "LSTM",
        "radiation": radiation,
        "risk": risk
    }