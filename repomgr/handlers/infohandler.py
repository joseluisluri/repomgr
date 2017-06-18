import os

from repomgr.errors import RepomgrError
from repomgr.handlers import Handler
from repomgr.utils import CacheHelper, PrintHelper


class InfoHandler(Handler):
    def run(self, crc32: str):
        if not os.path.exists(self._config.cache.filename):
            raise RepomgrError('ROM index cache must be generated before')

        repository = CacheHelper.import_file(self._config.cache.filename)

        for system in repository:
            for rom in system.roms:
                if rom.crc32.lower()[2:] == crc32:
                    PrintHelper.detailed(system, rom)
