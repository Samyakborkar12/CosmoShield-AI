from tensorflow.keras.models import load_model
import joblib

from ml.config import MODEL_PATH, SCALER_PATH

model = None
scaler = None


def load_ml_assets():
    global model, scaler

    if model is None:
        print("Loading LSTM Model...")
        model = load_model(MODEL_PATH)

    if scaler is None:
        print("Loading Feature Scaler...")
        scaler = joblib.load(SCALER_PATH)

    return model, scaler