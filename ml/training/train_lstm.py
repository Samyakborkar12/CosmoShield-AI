from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

from ml.preprocessing.load_dataset import load_dataset
from ml.preprocessing.clean_data import clean_dataset
from ml.preprocessing.feature_engineering import create_features
from ml.preprocessing.scaler import scale_features, save_scaler
from ml.preprocessing.split_data import split_dataset
from ml.preprocessing.sequence_generator import create_sequences

from ml.model.lstm_model import build_lstm_model

from ml.config import (
    SEQUENCE_LENGTH,
    BATCH_SIZE,
    EPOCHS,
    MODEL_PATH,
    SCALER_PATH
)


def train():

    print("Loading dataset...")

    df = load_dataset("dataset/raw/nasa_omni_2020_2024.csv")

    print("Cleaning dataset...")

    df = clean_dataset(df)

    print("Creating features...")

    X, y = create_features(df)

    print("Scaling features...")

    X_scaled, scaler = scale_features(X)

    save_scaler(scaler, SCALER_PATH)

    print("Splitting dataset...")

    X_train, X_test, y_train, y_test = split_dataset(X_scaled, y)

    print("Generating sequences...")

    X_train, y_train = create_sequences(
        X_train,
        y_train,
        SEQUENCE_LENGTH
    )

    X_test, y_test = create_sequences(
        X_test,
        y_test,
        SEQUENCE_LENGTH
    )

    print("Building LSTM model...")

    model = build_lstm_model(
        (SEQUENCE_LENGTH, X_train.shape[2])
    )

    callbacks = [

        EarlyStopping(
            monitor="val_loss",
            patience=5,
            restore_best_weights=True
        ),

        ModelCheckpoint(
            MODEL_PATH,
            save_best_only=True,
            monitor="val_loss"
        )

    ]

    print("Training started...\n")

    history = model.fit(

        X_train,
        y_train,

        validation_data=(X_test, y_test),

        epochs=EPOCHS,

        batch_size=BATCH_SIZE,

        callbacks=callbacks,

        verbose=1

    )

    print("\nTraining Complete!")

    return history


if __name__ == "__main__":
    train()