from injector import inject

from repomgr.constants import CONF_SYSTEMS_SECTION
from repomgr.controllers import Controller
from repomgr.errors import FileFormatError
from repomgr.errors import RepomgrError
from repomgr.models import Dump
from repomgr.models import Repository
from repomgr.models import System
from repomgr.services import ConfigService, CacheService
from repomgr.utils import ScanHelper
from repomgr.views import UpdateView


class UpdateController(Controller):
    @inject
    def __init__(self, cache_service: CacheService, config_service: ConfigService, view: UpdateView):
        self._cache_service: CacheService = cache_service
        self._config_service: ConfigService = config_service
        self._view = view

    def run(self, args: dict):
        try:
            if self._cache_service.cache_exists:
                repository: Repository = self._cache_service.import_cache()
            else:
                repository: Repository = Repository()

            for conf_system in self._config_service.section(CONF_SYSTEMS_SECTION):
                if args.get('system') is None or args.get('system') == conf_system.get('tag'):
                    dumps: [Dump] = ScanHelper.scan_dir(conf_system.get('path'), self._view.progress)
                    system: System = System(name=conf_system.get('name'),
                                            tag=conf_system.get('tag'),
                                            path=conf_system.get('path'),
                                            dumps=dumps)
                    repository.systems.append(system)
                    self._view.update(system)

            # export
            self._cache_service.export_cache(repository)
            self._view.finish()
        except (FileNotFoundError, FileFormatError) as e:
            raise RepomgrError(str(e))
        except IOError as e:
            raise RepomgrError(str(e))
