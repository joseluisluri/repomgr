from injector import inject

from repomgr.controllers import Controller
from repomgr.models import Repository
from repomgr.services import CacheService
from repomgr.views import SearchView


class SearchController(Controller):
    @inject
    def __init__(self, cache_service: CacheService, view: SearchView):
        self._cache_service: CacheService = cache_service
        self._view: SearchView = view

    def run(self, args: dict):
        if self._cache_service.cache_exists:
            needles: [str] = list(map((lambda s: s.lower()), args.get('seed')))
            matches: [tuple] = []
            repository: Repository = self._cache_service.import_cache()

            for system in repository.systems:
                for dump in system.dumps:
                    for needle in needles:
                        if needle in dump.name.lower():
                            matches.append((system, dump))
                            break

            self._view.update(matches)
        else:
            self._view.nocache()
