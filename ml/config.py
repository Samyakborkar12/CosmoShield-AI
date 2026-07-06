# Active model currently used for prediction
ACTIVE_MODEL = "lstm"

# Folder containing trained models 
MODEL_DIRECTORY = "models/"

#Supported prediction models
SUPPORTED_MODELS = [
    "lstm",
    "transformer",
    "random_forest"
]

# Minium confidence required 
CONFIDENCE_THRESHOLD = 0.80