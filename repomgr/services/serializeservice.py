import json
from datetime import datetime

from injector import singleton

from repomgr.errors import FileFormatError
from repomgr.models import Repository, Dump, Rom
from repomgr.models import System
from repomgr.services import Service


@singleton
class SerializeService(Service):

    @classmethod
    def serialize(cls, repository: Repository) -> str:
        return json.dumps(repository.as_dict())

    @classmethod
    def unserialize(cls, data: str) -> Repository:
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
                    e: Dump = Dump(uuid=dump['uuid'],
                                   name=dump['name'],
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
