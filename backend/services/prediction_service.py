from ml.loader import load_model
from ml.predictor import predict

def predict_radiation(data):

    model = load_model()

    prediction = predict(model, data)

    return {
        "status": "success",
        "prediction": prediction,
        "received_data": data
    }