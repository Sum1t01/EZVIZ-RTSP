from pyezvizapi import EzvizClient
import config

class EZVIZConnection:
    _instance = None
    _client = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def connect(self):
        if self._client is not None:
            return self._client

        try:
            print("Connecting to EzViz")
            self._client = EzvizClient(
                config.USERNAME,
                config.PASSWORD
            )

            return self._client

        except Exception as error:
            self._client = None
            print("EZVIZ connection error:", error)
            return None

    def get_client(self):
        return self.connect()


ezviz = EZVIZConnection()
