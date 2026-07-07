from backend.utils.validation import validate_input

from backend.database.prediction_db import save_prediction

from ml.loader import load_model
from ml.predictor import predict


def predict_radiation(data):

    valid, result = validate_input(data)

    if not valid:
        return {
            "status": "error",
            "message": result
        }

    data = result

    model = load_model()

    prediction = predict(model, data)

    save_prediction(
        satellite=data["satellite"],
        energy=data["energy"],
        radiation=prediction["radiation"],
        risk=prediction["risk"]
    )

    return {
        "status": "success",
        "model": prediction["model"],
        "radiation": prediction["radiation"],
        "risk": prediction["risk"]
    }