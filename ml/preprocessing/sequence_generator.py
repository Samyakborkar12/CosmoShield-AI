import numpy as np


def create_sequences(X, y, sequence_length=12):

    X_sequences = []
    y_sequences = []

    for i in range(len(X) - sequence_length):

        X_sequences.append(
            X[i:i + sequence_length]
        )

        y_sequences.append(
            y.iloc[i + sequence_length]
        )

    return (
        np.array(X_sequences),
        np.array(y_sequences)
    )