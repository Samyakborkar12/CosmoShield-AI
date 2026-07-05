def predict_radiation(data):
    """
    Temporary prediction.
    Later this function will call the LSTM model.
    """

    return {
        "status": "success",
        "model": "Dummy Model",
        "radiation":5.72,
        "risk": "Medium",
        "received_data": data
    }