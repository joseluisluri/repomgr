import os

from repomgr.errors import RepomgrError
from repomgr.controllers import Controller
from repomgr.utils import CacheHelper, PrintHelper


class SearchController(Controller):

    def _run(self, needles: str):
        if not os.path.exists(self._config.cache.filename):
            raise RepomgrError('ROM index cache must be generated before')

        repository = CacheHelper.import_file(self._config.cache.filename)

        needles = list(map((lambda e: e.lower()), needles))

        matches = list()
        for system in repository:
            for dump in system.dumps:
                for needle in needles:
                    if needle in dump.name.lower():
                        matches.append((system, dump))
                        break

        if len(matches):
            PrintHelper.table(matches)
        else:
            PrintHelper.echo('0 results')
