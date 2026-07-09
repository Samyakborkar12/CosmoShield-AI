from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout, Input
from tensorflow.keras.optimizers import Adam

from ml.config import LEARNING_RATE


def build_lstm_model(input_shape):

    model = Sequential([
        Input(shape=input_shape),

        LSTM(
            64,
            return_sequences=True
        ),

        Dropout(0.2),

        LSTM(32),

        Dropout(0.2),

        Dense(
            16,
            activation="relu"
        ),

        Dense(1)
    ])

    model.compile(
        optimizer=Adam(
            learning_rate=LEARNING_RATE
        ),
        loss="mse",
        metrics=["mae"]
    )

    return model