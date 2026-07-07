from ml.config import ACTIVE_MODEL


def load_transformer():
    return "Dummy Transformer Model"


def load_lstm():
    return "Dummy LSTM Model"


def load_random_forest():
    return "Dummy Random Forest Model"


MODELS = {
    "transformer": load_transformer,
    "lstm": load_lstm,
    "random_forest": load_random_forest
}


_loaded_model = None


def load_model():
    global _loaded_model

    if _loaded_model is None:

        loader = MODELS.get(ACTIVE_MODEL)

        if loader is None:
            raise ValueError(f"Unsupported model: {ACTIVE_MODEL}")

        _loaded_model = loader()

    return _loaded_model