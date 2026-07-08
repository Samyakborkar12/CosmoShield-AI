import pandas as pd

COLUMNS = [
    "year",
    "day",
    "hour",
    "minute",
    "imf",
    "bx",
    "by",
    "bz",
    "speed",
    "density",
    "temperature",
    "proton_flux"
]


def load_dataset(path):
    df = pd.read_csv(
        path,
        sep=r"\s+",
        names=COLUMNS,
        engine="python"
    )

    return df