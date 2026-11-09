import cv2
from device_info import get_device_info
import config
from ezviz_client import ezviz
from urllib.parse import quote

def get_cam_key(serial):
    try:
        key = ezviz.get_client().get_cam_key(serial)

        if key:
            print(f"Camera key: {key}")
            return str(key)

    except Exception as error:
        print("Could not fetch camera key from EZVIZ:", error)

def start_streaming():
    serial = config.DEVICE_SERIAL
    camera_info = get_device_info(serial)

    ip = camera_info["ip"]

    username = quote(config.CAMERA_USERNAME, safe="")
    password = quote(get_cam_key(serial), safe="")

    rtsp_url = (
        f"rtsp://{username}:{password}"
        f"@{ip}:554/ch1/main"
    )

    print(f"Connecting to {camera_info['name']}...")
    print(f"Camera IP: {ip}")

    cap = cv2.VideoCapture(rtsp_url, cv2.CAP_FFMPEG)

    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

    if not cap.isOpened():
        print("Unable to open RTSP stream.")
        return

    print("Video stream connected!")

    try:
        while True:

            success, frame = cap.read()

            if not success:
                print("Video frame unavailable.")
                break

            cv2.imshow("EZVIZ H6c - Live Video", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    finally:
        cap.release()
        cv2.destroyAllWindows()


