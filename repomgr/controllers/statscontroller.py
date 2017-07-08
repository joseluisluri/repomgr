import os

from injector import inject

from repomgr.controllers import Controller
from repomgr.errors import RepomgrError
from repomgr.models import Repository
from repomgr.services import CacheService
from repomgr.utils import CacheHelper
from repomgr.views import StatsView


class StatsController(Controller):
    @inject
    def __init__(self, cache_service: CacheService, view: StatsView):
        self._cache_service = cache_service
        self._view = view

    def run(self, args: dict):
        if not os.path.exists(self._cache_service.filename):
            raise RepomgrError('ROM index cache must be generated before')
        else:
            try:
                repository: Repository = CacheHelper.import_file(self._cache_service.filename)
                self._view.update(repository)
            except IOError:
                raise RepomgrError('error al leer el fichero')
