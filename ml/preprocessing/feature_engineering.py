FEATURE_COLUMNS = [
    "imf",
    "bx",
    "by",
    "bz",
    "speed",
    "density",
    "temperature"
]

TARGET_COLUMN = "proton_flux"


def create_features(df):

    X = df[FEATURE_COLUMNS]

    y = df[TARGET_COLUMN]

    return X, y