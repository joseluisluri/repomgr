import io
import json
import time
from datetime import datetime

from repomgr.errors import FileFormatError
from repomgr.models import Rom, System


class CacheHelper:

    @staticmethod
    def _rom_mapper(rom: Rom) -> dict:
        dct = {}
        dct.update({'name': rom.name})
        dct.update({'modified': time.mktime(rom.modified.timetuple())})
        dct.update({'size': rom.size})
        dct.update({'crc32': rom.crc32})
        dct.update({'zip': rom.zip})
        return dct

    @classmethod
    def _system_mapper(cls, system: System) -> dict:
        dct = {}
        dct.update({'name': system.name})
        dct.update({'tag': system.tag})
        dct.update({'path': system.path})

        roms: [Rom] = []
        for rom in system.roms:
            roms.append(cls._rom_mapper(rom))

        dct.update({'roms': roms})
        return dct

    @classmethod
    def _repository_mapper(cls, repository: [System]) -> list:
        lst = []
        for system in repository:
            lst.append(cls._system_mapper(system))
        return lst

    @classmethod
    def encode(cls, repository: [System]) -> str:
        return json.dumps(cls._repository_mapper(repository))

    @classmethod
    def decode(cls, data: str) -> [System]:
        try:
            repository: [System] = []
            lst = json.loads(data)
            for system in lst:
                roms: [Rom] = []
                for rom in system['roms']:
                    e: Rom = Rom(name=rom["name"],
                                 modified= datetime.fromtimestamp(rom['modified']),
                                 size=int(rom['size']),
                                 crc32=rom['crc32'],
                                 zip=rom['zip'])
                    roms.append(e)
                e = System(system['name'], system['tag'], system['path'], roms)
                repository.append(e)
            return repository
        except KeyError as e:
            raise FileFormatError('Cache is corrupted and cannot be decoded')

    @classmethod
    def import_file(cls, path: str) -> list:
        with io.open(path, 'r', encoding='utf-8') as f:
            return cls.decode(f.read())

    @classmethod
    def export_file(cls, repository: [System], path: str):
        with io.open(path, 'w', encoding='utf-8') as f:
            f.write(cls.encode(repository))
