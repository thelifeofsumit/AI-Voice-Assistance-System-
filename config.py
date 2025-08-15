# config.py
import os

# --- Audio / ASR ---
# Vosk model paths (download and set absolute/relative path)
# e.g., models from: https://alphacephei.com/vosk/models
VOSK_MODELS = {
    "en": os.environ.get("VOSK_MODEL_EN", "models/vosk-model-small-en-us-0.15"),
    "hi": os.environ.get("VOSK_MODEL_HI", "models/vosk-model-small-hi-0.22"),
    "mr": os.environ.get("VOSK_MODEL_MR", "models/vosk-model-small-mr-0.22"),
}
DEFAULT_LANG = os.environ.get("ASSISTANT_LANG", "en")
SAMPLE_RATE = 16000  # Vosk recommended

WAKE_WORDS = {
    "en": ["jarvis", "computer", "assistant"],
    "hi": ["sunaiye", "sahayak", "jarvis"],
    "mr": ["madatgar", "sahayyak", "jarvis"],
}

# --- NLP ---
# Simple keyword intents per language
INTENT_KEYWORDS = {
    "en": {
        "greet": ["hello", "hi", "hey"],
        "time": ["time", "what time"],
        "date": ["date", "what date"],
        "lights_on": ["light on", "turn on light", "lights on"],
        "lights_off": ["light off", "turn off light", "lights off"],
        "open": ["open", "launch"],
        "weather": ["weather", "temperature"],
        "exit": ["exit", "quit", "goodbye", "stop"],
    },
    "hi": {
        "greet": ["namaste", "namaskar", "hello"],
        "time": ["samay", "kitna baje", "time"],
        "date": ["tareekh", "date"],
        "lights_on": ["light on", "batti jalao"],
        "lights_off": ["light off", "batti bujhao"],
        "open": ["kholo", "app kholo"],
        "weather": ["mausam", "tapman"],
        "exit": ["band", "ruk", "goodbye"],
    },
    "mr": {
        "greet": ["namaskar", "hello"],
        "time": ["vel", "kiti vajle"],
        "date": ["tarikh", "date"],
        "lights_on": ["light on", "batti chaalu"],
        "lights_off": ["light off", "batti bandh"],
        "open": ["uघडा", "open", "app uघडा"],
        "weather": ["hava", "tapman", "mausam"],
        "exit": ["band", "thamb", "goodbye"],
    },
}

# --- TTS ---
# pyttsx3 voice selection hints (optional)
TTS_VOICE_HINTS = {
    "en": ["english", "en"],  # contains substring
    "hi": ["hindi", "hi"],
    "mr": ["marathi", "mr"],
}
TTS_RATE = 180  # words-per-minute approx

# --- IoT (MQTT) ---
MQTT_ENABLED = os.environ.get("MQTT_ENABLED", "0") == "1"
MQTT_BROKER = os.environ.get("MQTT_BROKER", "localhost")
MQTT_PORT = int(os.environ.get("MQTT_PORT", "1883"))
MQTT_TOPIC_LIGHT = os.environ.get("MQTT_TOPIC_LIGHT", "home/livingroom/light")

# --- Vision ---
VISION_ENABLED = os.environ.get("VISION_ENABLED", "0") == "1"
FACE_CASCADE_PATH = os.environ.get(
    "FACE_CASCADE_PATH",
    "haarcascade_frontalface_default.xml"
)
