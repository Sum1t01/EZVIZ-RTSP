import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

CAMERA_USERNAME=os.getenv("CAMERA_USERNAME")
CAMERA_PASSWORD=os.getenv("CAMERA_PASSWORD")

DEVICE_SERIAL=os.getenv("DEVICE_SERIAL")

REGION = os.getenv("REGION", "np")

JSON_FILE = Path(__file__).parent / "devices.json"