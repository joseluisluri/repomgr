from injector import inject

from repomgr.controllers import Controller
from repomgr.models import Repository
from repomgr.services import CacheService, SyncService
from repomgr.views import SyncView


class SyncController(Controller):
    @inject
    def __init__(self, cache_service: CacheService, sync_service: SyncService, view: SyncView):
        self._cache_service: CacheService = cache_service
        self._sync_service: SyncService = sync_service
        self._view = view

    def run(self, args: dict):
        if self._cache_service.cache_exists:
            self._view.before()
            repository: Repository = self._cache_service.import_cache()
            self._sync_service.push(repository)
            self._view.after()
        else:
            self._view.nocache()
