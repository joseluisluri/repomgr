import os

from repomgr.errors import RepomgrError
from repomgr.controllers import Controller
from repomgr.utils import CacheHelper, PrintHelper


class InfoController(Controller):

    def _run(self, crc32: str):
        if not os.path.exists(self._config.cache.filename):
            raise RepomgrError('ROM index cache must be generated before')

        repository = CacheHelper.import_file(self._config.cache.filename)

        for system in repository:
            for dump in system.dump:
                if dump.crc32.lower()[2:] == crc32:
                    PrintHelper.detailed(system, dump)
