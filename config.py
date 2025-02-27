# filepath: /Arabic-2-English-Transformer/config.py

MODEL_PATH = "models/trained_model.h5"
MAX_INPUT_LENGTH = 100
LANGUAGE = "Arabic to English"
SUPPORTED_LANGUAGES = ["Arabic", "English"]
API_URL = "http://localhost:5000/translate"  # Example API endpoint for translation service
DEBUG_MODE = True  # Set to False in production