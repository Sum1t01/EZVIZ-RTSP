import cv2
from device_info import get_device_info, get_cam_key
import config
from urllib.parse import quote
from face_detection import detect_faces



def start_streaming():
    serial = config.DEVICE_SERIAL
    camera_info = get_device_info(serial)

    ip = camera_info["ip"]

    cam_key = get_cam_key(serial)

    if not cam_key:
        print("Unable to retrieve camera key.")
        return

    username = quote(config.CAMERA_USERNAME, safe="")
    password = quote(cam_key, safe="")

    rtsp_url = (
        f"rtsp://{username}:{password}"
        f"@{ip}:554/ch1/main"
    )

    print(f"Connecting to {camera_info['name']}...")
    print(f"Camera IP: {ip}")

    detector = cv2.FaceDetectorYN.create(
        config.DETECTOR_MODEL,
        "",
        (320, 320),
        0.8,
        0.3,
        5000
    )

    cap = cv2.VideoCapture(rtsp_url, cv2.CAP_FFMPEG)

    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

    if not cap.isOpened():
        print("Unable to open RTSP stream.")
        return

    print("Video stream connected!")

    frame_count = 0
    cached_faces = []

    try:
        while True:

            success, frame = cap.read()

            if not success:
                print("Video frame unavailable.")
                break

            frame_count += 1

            if frame_count%100 == 0:
                print("Frame Count", frame_count)

            if frame_count % 3 == 0:
                cached_faces = detect_faces(frame, detector)


            for x1, y1, x2, y2 in cached_faces:
                cv2.rectangle(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    (0, 255, 0),
                    2
                )

                cv2.putText(
                    frame,
                    "Face Detected",
                    (x1, max(20, y1 - 10)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 0),
                    2
                )

            cv2.imshow("EZVIZ H6c - Live Video", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    finally:
        cap.release()
        cv2.destroyAllWindows()


