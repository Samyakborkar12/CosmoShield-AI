from ml.preprocessing.load_dataset import load_dataset
from ml.preprocessing.clean_data import clean_dataset
from ml.preprocessing.feature_engineering import create_features
from ml.preprocessing.scaler import scale_features
from ml.preprocessing.split_data import split_dataset
from ml.preprocessing.sequence_generator import create_sequences

# Load dataset
df = load_dataset("dataset/raw/nasa_omni_2020_2024.csv")

# Clean dataset
df = clean_dataset(df)

# Feature engineering
X, y = create_features(df)

# Scale features
X_scaled, scaler = scale_features(X)

# Split dataset
X_train, X_test, y_train, y_test = split_dataset(X_scaled, y)

# Generate sequences
X_train_seq, y_train_seq = create_sequences(
    X_train,
    y_train
)

X_test_seq, y_test_seq = create_sequences(
    X_test,
    y_test
)

print("Training Sequences:")
print(X_train_seq.shape)
print(y_train_seq.shape)

print()

print("Testing Sequences:")
print(X_test_seq.shape)
print(y_test_seq.shape)