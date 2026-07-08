from sklearn.preprocessing import MinMaxScaler
import joblib


def scale_features(X):

    scaler = MinMaxScaler()

    X_scaled = scaler.fit_transform(X)

    return X_scaled, scaler


def save_scaler(scaler, path):

    joblib.dump(scaler, path)