from ml.config import SEQUENCE_LENGTH
import numpy as np


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
    ]])

    X = scaler.transform(X)

    X = np.repeat(X, SEQUENCE_LENGTH, axis=0)

    X = X.reshape((1, SEQUENCE_LENGTH, 7))

    prediction = model.predict(X, verbose=0)

    radiation = float(prediction[0][0])

    risk = calculate_risk(radiation)

    return {
        "model": "LSTM",
        "radiation": radiation,
        "risk": risk
    }