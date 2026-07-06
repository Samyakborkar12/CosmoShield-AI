from ml.config import ACTIVE_MODEL

def load_lstm():
    return "Dummy LSTM Model"

def load_transformer():
    return "Dummy Transformer Model"

def load_random_forest():
    return "Dummy Random Forest Model"

MODELS = {
    "lstm": load_lstm,
    "transformer": load_transformer,
    "random_forest": load_random_forest
}

def load_model():
    loader = MODELS.get(ACTIVE_MODEL)

    if loader is None:
        raise ValueError("Unsupported model")

    return loader()