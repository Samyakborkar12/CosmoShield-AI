from ml.preprocessing.load_dataset import load_dataset
from ml.preprocessing.clean_data import clean_dataset
from ml.preprocessing.feature_engineering import create_features
from ml.preprocessing.scaler import scale_features
from ml.preprocessing.split_data import split_dataset

df = load_dataset("dataset/raw/nasa_omni_2020_2024.csv")

df = clean_dataset(df)

X, y = create_features(df)

X_scaled, scaler = scale_features(X)

X_train, X_test, y_train, y_test = split_dataset(X_scaled, y)

print(X_train.shape)
print(X_test.shape)

print(y_train.shape)
print(y_test.shape)