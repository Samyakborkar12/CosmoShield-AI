from ml.preprocessing.load_dataset import load_dataset

df = load_dataset("dataset/raw/nasa_omni_2020_2024.csv")

print(df.head())
print(df.shape)