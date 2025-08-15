# modules/asr.py
import json
import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer

class ASR:
    def __init__(self, model_path: str, sample_rate: int = 16000):
        self.model = Model(model_path)
        self.sample_rate = sample_rate
        self.rec = KaldiRecognizer(self.model, sample_rate)
        self.q = queue.Queue()

    def _callback(self, indata, frames, time, status):
        if status:
            # You may log status if needed
            pass
        self.q.put(bytes(indata))

    def listen_once(self, prompt_seconds: int = 6) -> str:
        """Capture mic audio for ~prompt_seconds and return recognized text."""
        with sd.RawInputStream(samplerate=self.sample_rate, blocksize=8000, dtype='int16',
                               channels=1, callback=self._callback):
            sd.sleep(int(prompt_seconds * 1000))
            text = []
            try:
                while True:
                    data = self.q.get_nowait()
                    if self.rec.AcceptWaveform(data):
                        res = json.loads(self.rec.Result())
                        if res.get("text"):
                            text.append(res["text"])
                    else:
                        # partial = json.loads(self.rec.PartialResult())
                        pass
            except queue.Empty:
                # finalize
                res_final = json.loads(self.rec.FinalResult())
                if res_final.get("text"):
                    text.append(res_final["text"])
            return " ".join(t for t in text if t).strip()
