from ml.config import ACTIVE_MODEL


def load_model():

    if ACTIVE_MODEL == "lstm":
        return "LSTM Model Loaded"
    
    elif ACTIVE_MODEL == "transformer":
        return "Transformer Model Loded"
    
    elif ACTIVE_MODEL == "random_forest":
        return "Random Forest Model Loaded"
    
    else:
        raise ValueError("Unsupported Model")