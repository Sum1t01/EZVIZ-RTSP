import json
import config
from ezviz_client import ezviz

def get_device_list():

    client = ezviz.get_client()

    # Retrieve cameras
    devices = client.get_device_infos()

    json_file = config.JSON_FILE

    with open(json_file, "w", encoding="utf-8") as file:
        json.dump(
            devices,
            file,
            indent=4,
            ensure_ascii=False,
            default=str
        )

    print(f"Device JSON saved: {json_file}")


if __name__ == "__main__":
    get_device_list()