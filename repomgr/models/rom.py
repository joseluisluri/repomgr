from datetime import datetime


class Rom:
    def __init__(self, name: str, modified: datetime, size: int, crc32: str, zip: str):
        self.name: str = name
        self.modified: datetime = modified
        self.size: int = size
        self.crc32: str = crc32
        self.zip: str = zip

    def __str__(self):
        return str(self.__dict__)
