# AI Voice Assistance System

A **modular, offline-first voice assistant** built in Python that supports **multi-language** and **accent-adaptive** commands, IoT integration, and basic computer vision.  
Designed with **edge computing** for privacy — all processing happens locally.

#  Features
- **Multi-language Voice Recognition** (English, Hindi, Marathi) using [Vosk ASR](https://alphacephei.com/vosk/).
- **Accent-Adaptive NLP** for better understanding of varied speech patterns.
- **Offline Processing** — works without internet for most tasks.
- **IoT Device Control** via MQTT (lights, appliances, etc.).
- **Text-to-Speech (TTS)** with language-specific voice selection.
- **Computer Vision** for face detection before responding.
- **Privacy-first** — all audio stays on-device (GDPR-aligned).
  
# Tech Stack
- **Python**
- **Speech Recognition (ASR):** [Vosk](https://alphacephei.com/vosk/)
- **NLP:** Custom keyword-based intent detection
- **TTS:** [pyttsx3](https://pyttsx3.readthedocs.io/)
- **IoT Control:** [paho-mqtt](https://pypi.org/project/paho-mqtt/)
- **Computer Vision:** [OpenCV](https://opencv.org/)
