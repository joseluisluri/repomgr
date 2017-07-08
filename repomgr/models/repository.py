from datetime import datetime

from repomgr.models import System


class Repository:
    def __init__(self, modified: datetime = datetime.now(), systems: [System] = list()):
        self.modified: datetime = modified
        self.systems: [System] = systems

    @property
    def size(self) -> int:
        acc: int = 0
        for system in self.systems:
            acc += system.size
        return acc

    @property
    def dumps(self) -> int:
        acc: int = 0
        for system in self.systems:
            acc += len(system.dumps)
        return acc

    @property
    def roms(self) -> int:
        acc: int = 0
        for system in self.systems:
            for dump in system.dumps:
                acc += len(dump.roms)
        return acc