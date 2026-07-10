import pandas as pd
import numpy as np


NASA_MISSING_VALUES = {
    "speed": 99999.9,
    "density": 999.99,
    "temperature": 9999999.0
}


def clean_dataset(df):

    df = df.copy()

    # Replace NASA placeholder values
    for column, value in NASA_MISSING_VALUES.items():
        df[column] = df[column].replace(value, np.nan)

    # Proton Flux has multiple missing markers
    df["proton_flux"] = df["proton_flux"].replace(
        [99999.99, 999999.0],
        np.nan
    )

    # Convert everything to numeric
    df = df.apply(pd.to_numeric, errors="coerce")

    # Remove rows containing missing values
    df = df.dropna()

    # Reset index
    df = df.reset_index(drop=True)

    return df


def save_clean_dataset(df, path):
    df.to_csv(path, index=False)