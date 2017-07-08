import io
import json
import time
from datetime import datetime

from repomgr.errors import FileFormatError
from repomgr.models import System, Rom, Dump, Repository


class CacheHelper:

    @staticmethod
    def _rom_mapper(rom: Rom) -> dict:
        dct: dict = {}
        dct.update({'name': rom.name})
        dct.update({'modified': time.mktime(rom.modified.timetuple())})
        dct.update({'size': rom.size})
        dct.update({'crc32': rom.crc32})
        return dct

    @classmethod
    def _dump_mapper(cls, dump: Dump) -> dict:
        roms: [dict] = []
        for rom in dump.roms:
            roms.append(cls._rom_mapper(rom))

        dct: dict = {}
        dct.update({'name': dump.name})
        dct.update({'zip': dump.zip})
        dct.update({'roms': roms})
        return dct

    @classmethod
    def _system_mapper(cls, system: System) -> dict:
        dumps: [dict] = []
        for dump in system.dumps:
            dumps.append(cls._dump_mapper(dump))

        dct: dict = {}
        dct.update({'name': system.name})
        dct.update({'tag': system.tag})
        dct.update({'path': system.path})
        dct.update({'dumps': dumps})
        return dct

    @classmethod
    def _repository_mapper(cls, repository: Repository) -> dict:
        systems: [dict] = []
        for system in repository.systems:
            systems.append(cls._system_mapper(system))

        dct: dict = {}
        dct.update({'size': repository.size})
        dct.update({'dumps': repository.dumps})
        dct.update({'systems': systems})
        return dct

    @classmethod
    def encode(cls, repository: Repository) -> str:
        return json.dumps(cls._repository_mapper(repository))

    @classmethod
    def decode(cls, data: str) -> Repository:
        try:
            repository: Repository = Repository()
            dct: dict = json.loads(data)
            for system in dct['systems']:
                dumps: [Dump] = []
                for dump in system['dumps']:
                    roms: [Rom] = []
                    for rom in dump['roms']:
                        e: Rom = Rom(name=rom["name"],
                                     modified=datetime.fromtimestamp(rom['modified']),
                                     size=int(rom['size']),
                                     crc32=rom['crc32'])
                        roms.append(e)
                    e: Dump = Dump(name=dump['name'],
                                   zipfile=dump['zip'],
                                   roms=roms)
                    dumps.append(e)
                e: System = System(name=system['name'],
                                   tag=system['tag'],
                                   path=system['path'],
                                   dumps=dumps)
                repository.systems.append(e)
            return repository
        except KeyError:
            raise FileFormatError('Cache is corrupted and cannot be decoded')

    @classmethod
    def import_file(cls, path: str) -> Repository:
        with io.open(path, 'r', encoding='utf-8') as f:
            return cls.decode(f.read())

    @classmethod
    def export_file(cls, repository: Repository, path: str):
        with io.open(path, 'w', encoding='utf-8') as f:
            f.write(cls.encode(repository))
