# modules/tts.py
import pyttsx3

class TTS:
    def __init__(self, lang_hint=None, rate=180):
        self.engine = pyttsx3.init()
        self.set_rate(rate)
        if lang_hint:
            self.select_voice(lang_hint)

    def set_rate(self, rate):
        self.engine.setProperty("rate", rate)

    def select_voice(self, lang_hint_substrings):
        # Try to pick a voice that matches the hint substrings
        voices = self.engine.getProperty("voices")
        for v in voices:
            desc = f"{v.name} {v.id}".lower()
            if any(s.lower() in desc for s in lang_hint_substrings):
                self.engine.setProperty("voice", v.id)
                break

    def say(self, text: str):
        self.engine.say(text)
        self.engine.runAndWait()
