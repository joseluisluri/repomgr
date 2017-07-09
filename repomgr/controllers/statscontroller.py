from injector import inject

from repomgr.controllers import Controller
from repomgr.models import Repository
from repomgr.services import CacheService
from repomgr.views import StatsView


class StatsController(Controller):
    @inject
    def __init__(self, cache_service: CacheService, view: StatsView):
        self._cache_service = cache_service
        self._view = view

    def run(self, args: dict):
        if self._cache_service.cache_exists:
            repository: Repository = self._cache_service.import_cache()
            self._view.update(repository)
        else:
            self._view.nocache()
