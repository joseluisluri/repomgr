from repomgr.models import Rom


class System:
    def __init__(self, name: str, tag: str, path: str, roms: [Rom] = list()):
        self.name: str = name
        self.tag: str = tag
        self.path: str = path
        self.roms: [Rom] = roms

    def __str__(self):
        return str(self.__dict__)
