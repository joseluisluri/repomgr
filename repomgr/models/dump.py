from repomgr.models import Rom


class Dump:
    def __init__(self, name: str, zipfile: str, roms: [Rom] = list()):
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
        return str(self.__dict__)
