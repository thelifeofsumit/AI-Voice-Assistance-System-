# modules/vision.py
import cv2

class Vision:
    def __init__(self, cascade_path: str):
        self.face_cascade = cv2.CascadeClassifier(cascade_path)

    def detect_face(self, camera_index: int = 0) -> bool:
        cap = cv2.VideoCapture(camera_index)
        detected = False
        if not cap.isOpened():
            return detected
        ret, frame = cap.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
            detected = len(faces) > 0
        cap.release()
        return detected
