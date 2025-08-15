# modules/iot.py
try:
    import paho.mqtt.client as mqtt
except Exception:
    mqtt = None

class IOT:
    def __init__(self, enabled=False, broker="localhost", port=1883):
        self.enabled = enabled and mqtt is not None
        self.client = None
        if self.enabled:
            self.client = mqtt.Client()
            self.client.connect(broker, port, 60)

    def publish(self, topic: str, payload: str):
        if self.enabled and self.client:
            self.client.publish(topic, payload)
            return True
        return False

    def mock_toggle(self, device: str, state: str):
        # Fallback simulation for when MQTT not enabled
        print(f"[IOT-SIM] {device} -> {state}")
        return True
