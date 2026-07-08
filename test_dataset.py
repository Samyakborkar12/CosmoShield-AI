from ml.preprocessing.load_dataset import load_dataset
from ml.preprocessing.clean_data import clean_dataset
from ml.preprocessing.feature_engineering import create_features

df = load_dataset("dataset/raw/nasa_omni_2020_2024.csv")

df = clean_dataset(df)

X, y = create_features(df)

print(X.head())

print()

print(y.head())

print()

print(X.shape)

print(y.shape)