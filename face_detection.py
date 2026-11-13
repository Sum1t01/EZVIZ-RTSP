import cv2
import os
from datetime import datetime
import config

def detect_faces(frame, detector) -> list:

    height, width = frame.shape[:2]

    os.makedirs(config.SAVE_FACES_DIR, exist_ok=True)

    detector.setInputSize((width, height))

    _, faces = detector.detect(frame)

    cached_faces = []

    if faces is None:
        return cached_faces

    for face in faces:

        x, y, w, h = face[:4].astype(int)

        confidence = float(face[-1])

        x1 = max(0, x)
        y1 = max(0, y)
        x2 = min(width, x + w)
        y2 = min(height, y + h)

        if x2 - x1 < 40 or y2 - y1 < 40:
            continue

        face_crop = frame[y1:y2, x1:x2]

        if face_crop.size == 0:
            continue

        cached_faces.append((x1, y1, x2, y2))

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S_%f"
        )

        filename = f"face_{timestamp}_{confidence:.2f}.jpg"

        filepath = os.path.join(
            config.SAVE_FACES_DIR,
            filename
        )

        if cv2.imwrite(filepath, face_crop):
            print(
                f"Face saved: {filepath} "
                f"(Confidence: {confidence:.2f})"
            )

    return cached_faces