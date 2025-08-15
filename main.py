# main.py
import os
import subprocess
from config import (
    VOSK_MODELS, DEFAULT_LANG, SAMPLE_RATE, WAKE_WORDS,
    INTENT_KEYWORDS, TTS_VOICE_HINTS, TTS_RATE,
    MQTT_ENABLED, MQTT_BROKER, MQTT_PORT, MQTT_TOPIC_LIGHT,
    VISION_ENABLED, FACE_CASCADE_PATH
)
from modules.asr import ASR
from modules.nlp import detect_intent, handle_intent, normalize
from modules.tts import TTS
from modules.iot import IOT
from modules.vision import Vision

def has_wake_word(text: str, lang: str) -> bool:
    t = normalize(text)
    return any(ww in t for ww in WAKE_WORDS.get(lang, []))

def run_command_open_app(text: str):
    # very basic demo: open calculator or notepad on Windows/macOS/Linux
    t = text.lower()
    try:
        if "notepad" in t or "editor" in t:
            if os.name == "nt":
                subprocess.Popen(["notepad"])
            else:
                subprocess.Popen(["gedit"])
        elif "calculator" in t or "calc" in t:
            if os.name == "nt":
                subprocess.Popen(["calc.exe"])
            elif sys.platform == "darwin":
                subprocess.Popen(["open", "-a", "Calculator"])
            else:
                subprocess.Popen(["gnome-calculator"])
    except Exception:
        pass

def main():
    lang = DEFAULT_LANG
    model_path = VOSK_MODELS[lang]
    asr = ASR(model_path=model_path, sample_rate=SAMPLE_RATE)
    tts = TTS(lang_hint=TTS_VOICE_HINTS.get(lang), rate=TTS_RATE)
    iot = IOT(enabled=MQTT_ENABLED, broker=MQTT_BROKER, port=MQTT_PORT)
    vision = Vision(FACE_CASCADE_PATH) if VISION_ENABLED else None

    tts.say({
        "en": "Assistant ready. Say the wake word to begin.",
        "hi": "सहायक तैयार है। शुरू करने के लिए वेक शब्द बोलें।",
        "mr": "सहाय्यक तयार आहे. सुरुवात करण्यासाठी वेक शब्द बोला.",
    }.get(lang, "Assistant ready."))

    while True:
        heard = asr.listen_once(prompt_seconds=4)
        if not heard:
            continue

        if has_wake_word(heard, lang):
            # Optional: face presence check for personalization / privacy
            if VISION_ENABLED and vision and not vision.detect_face():
                tts.say("I don't see anyone. For privacy, I won't respond.")
                continue

            tts.say({
                "en": "I'm listening.",
                "hi": "जी, बोलिए।",
                "mr": "हो, सांगा.",
            }.get(lang, "I'm listening."))

            # Capture the actual command
            cmd = asr.listen_once(prompt_seconds=6)
            if not cmd:
                tts.say("I didn't catch that.")
                continue

            intent = detect_intent(cmd, INTENT_KEYWORDS.get(lang, {}))
            response = handle_intent(intent, cmd, lang)

            # Side-effects (IoT / open app)
            if intent == "lights_on":
                ok = iot.publish(MQTT_TOPIC_LIGHT, "ON") or iot.mock_toggle("light", "ON")
                if ok: response = ({"en": "Turning lights on.",
                                    "hi": "लाइट चालू कर रहा हूँ।",
                                    "mr": "लाईट चालू करत आहे."}).get(lang, response)
            elif intent == "lights_off":
                ok = iot.publish(MQTT_TOPIC_LIGHT, "OFF") or iot.mock_toggle("light", "OFF")
                if ok: response = ({"en": "Turning lights off.",
                                    "hi": "लाइट बंद कर रहा हूँ।",
                                    "mr": "लाईट बंद करत आहे."}).get(lang, response)
            elif intent == "open":
                run_command_open_app(cmd)

            tts.say(response)

            if intent == "exit":
                break

if __name__ == "__main__":
    main()
