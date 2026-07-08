from ml.preprocessing.load_dataset import load_dataset
from ml.preprocessing.clean_data import clean_dataset

df = load_dataset("dataset/raw/nasa_omni_2020_2024.csv")

print("Before Cleaning")
print(df.shape)

clean_df = clean_dataset(df)

print("After Cleaning")
print(clean_df.shape)