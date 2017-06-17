import os

from ..errors import RepomgrError
from ..handlers import Handler
from ..utils import CacheHelper, PrintHelper


class SearchHandler(Handler):
    def run(self, needles: str):
        if not os.path.exists(self._config.cache.filename):
            raise RepomgrError('ROM index cache must be generated before')

        repository = CacheHelper.import_file(self._config.cache.filename)

        needles = list(map((lambda e: e.lower()), needles))

        matches = list()
        for system in repository:
            for rom in system.roms:
                for needle in needles:
                    if needle in rom.name.lower():
                        matches.append((system, rom))
                        break

        if len(matches):
            PrintHelper.table(matches)
        else:
            PrintHelper.echo('0 results')
