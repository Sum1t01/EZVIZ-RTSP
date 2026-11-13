import json
import config
from device_list import get_device_list
from ezviz_client import ezviz



def get_device_info(serial):

    get_device_list()

    json_file = config.JSON_FILE

    with open(json_file, "r", encoding="utf-8") as file:
        devices = json.load(file)

    device = devices.get(serial)

    if not device:
        raise ValueError(f"Camera {serial} not found")

    info = {
        "serial": serial,
        "name": device["deviceInfos"]["name"],
        "ip": device["CONNECTION"]["localIp"],
        "port": device["CONNECTION"]["localRtspPort"],
        "firmware": device["deviceInfos"]["version"],
        "model": device["deviceInfos"]["deviceSubCategory"],
        "mac": device["deviceInfos"]["mac"],
        "ssid": device["WIFI"]["ssid"],
        "online": device["STATUS"]["optionals"]["OnlineStatus"] == 1
    }

    print(json.dumps(info, indent = 4))

    return info


def get_cam_key(serial):
    try:
        key = ezviz.get_client().get_cam_key(serial)

        if key:
            print(f"Camera key: {key}")
            return str(key)

    except Exception as error:
        print("Could not fetch camera key from EZVIZ:", error)

    return None
