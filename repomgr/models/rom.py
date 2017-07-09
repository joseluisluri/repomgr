import time
from datetime import datetime


class Rom:
    def __init__(self, name: str, modified: datetime, size: int, crc32: str):
        self.name: str = name
        self.modified: datetime = modified
        self.size: int = size
        self.crc32: str = crc32

    def __str__(self):
        return str(self.as_dict())

    def as_dict(self) -> dict:
        dct: dict = {}
        dct.update({'name': self.name})
        dct.update({'modified': time.mktime(self.modified.timetuple())})
        dct.update({'size': self.size})
        dct.update({'crc32': self.crc32})
        return dct
