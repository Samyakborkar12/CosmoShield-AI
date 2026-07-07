from ml.loader import load_model
from ml.predictor import predict
from database.prediction_db import save_prediction


def predict_radiation(data):

    # Load active model
    model = load_model()

    # Predict
    prediction = predict(model, data)

    # Save prediction to database
    save_prediction(
        satellite=data["satellite"],
        energy=data["energy"],
        radiation=prediction["radiation"],
        risk=prediction["risk"]
    )

    # Return API response
    return {
        "status": "success",
        "prediction": prediction,
        "received_data": data
    }