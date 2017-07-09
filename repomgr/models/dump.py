from repomgr.models import Rom


class Dump:
    def __init__(self, uuid: str, name: str, zipfile: str, roms: [Rom] = list()):
        self.uuid: str = uuid
        self.name: str = name
        self.zip: str = zipfile
        self.roms: [Rom] = roms

    @property
    def size(self) -> int:
        acc: int = 0
        for rom in self.roms:
            acc += rom.size
        return acc

    def __str__(self):
        return str(self.as_dict())

    def as_dict(self) -> dict:
        roms: [dict] = []
        for rom in self.roms:
            roms.append(rom.as_dict())

        dct: dict = {}
        dct.update({'uuid': self.uuid})
        dct.update({'name': self.name})
        dct.update({'zip': self.zip})
        dct.update({'roms': roms})
        return dct
