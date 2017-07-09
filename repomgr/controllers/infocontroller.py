from injector import inject

from repomgr.controllers import Controller
from repomgr.models import Repository
from repomgr.services import CacheService
from repomgr.views import InfoView


class InfoController(Controller):

    @inject
    def __init__(self, cache_service: CacheService, view: InfoView):
        self._cache_service: CacheService = cache_service
        self._view: InfoView = view

    def run(self, args: dict):
        if self._cache_service.cache_exists:
            repository: Repository = self._cache_service.import_cache()
            for system in repository.systems:
                for dump in system.dumps:
                    if dump.uuid.lower() == args.get('uuid'):
                        self._view.update(system, dump)
        else:
            self._view.nocache()