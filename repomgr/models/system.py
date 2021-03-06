from repomgr.models import Dump


class System:
    def __init__(self, name: str, tag: str, path: str, dumps: [Dump] = list()):
        self.name: str = name
        self.tag: str = tag
        self.path: str = path
        self.dumps: [Dump] = dumps

    @property
    def size(self) -> int:
        acc: int = 0
        for dump in self.dumps:
            acc += dump.size
        return acc

    def __str__(self):
        return str(self.as_dict())

    def as_dict(self) -> dict:
        dumps: [dict] = []
        for dump in self.dumps:
            dumps.append(dump.as_dict())

        dct: dict = {}
        dct.update({'name': self.name})
        dct.update({'tag': self.tag})
        dct.update({'path': self.path})
        dct.update({'dumps': dumps})
        return dct
