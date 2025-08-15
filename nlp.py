# modules/nlp.py
import re
from datetime import datetime

def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower()).strip()

def detect_intent(text: str, keywords_map: dict) -> str:
    n = normalize(text)
    for intent, kws in keywords_map.items():
        for kw in kws:
            if kw in n:
                return intent
    return "unknown"

def handle_intent(intent: str, text: str, lang: str):
    now = datetime.now()
    if intent == "greet":
        return {
            "en": "Hello! How can I help?",
            "hi": "नमस्ते! मैं आपकी कैसे मदद कर सकता हूँ?",
            "mr": "नमस्कार! मी कशी मदत करू?",
        }.get(lang, "Hello! How can I help?")
    if intent == "time":
        return now.strftime("Time is %I:%M %p")
    if intent == "date":
        return now.strftime("Today is %A, %d %B %Y")
    if intent == "weather":
        return "For weather, please open your weather app or integrate an API."
    if intent in ("lights_on", "lights_off"):
        # Actual on/off is performed in main via iot module
        return "Okay."
    if intent == "open":
        return "Opening requested app (demo)."
    if intent == "exit":
        return "Goodbye!"
    return "Sorry, I didn't understand. Please rephrase."
