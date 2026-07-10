from ml.preprocessing.load_dataset import load_dataset
from ml.preprocessing.clean_data import clean_dataset

df = load_dataset("dataset/raw/nasa_omni_2020_2024.csv")
df = clean_dataset(df)

print(df["proton_flux"].describe())

print("\nFirst 10 values:")
print(df["proton_flux"].head(10))

print("\nMaximum:")
print(df["proton_flux"].max())

print("\nMinimum:")
print(df["proton_flux"].min())