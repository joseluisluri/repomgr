from injector import inject

from repomgr.constants import CONF_CACHE_SECTION
from repomgr.constants import CONF_SYSTEMS_SECTION
from repomgr.controllers import Controller
from repomgr.errors import FileFormatError
from repomgr.errors import RepomgrError
from repomgr.models import Dump
from repomgr.models import Repository
from repomgr.models import System
from repomgr.services import ConfigService
from repomgr.utils import CacheHelper
from repomgr.utils import ScanHelper
from repomgr.views import UpdateView


class UpdateController(Controller):
    @inject
    def __init__(self, config_service: ConfigService, view: UpdateView):
        self._config_service = config_service
        self._view = view

    def run(self, args: dict):
        try:
            repository: Repository = Repository()
            for conf_system in self._config_service.section(CONF_SYSTEMS_SECTION):
                dumps: [Dump] = ScanHelper.scan_dir(conf_system.get('path'), self._view.progress)
                system: System = System(name=conf_system.get('name'),
                                        tag=conf_system.get('tag'),
                                        path=conf_system.get('path'),
                                        dumps=dumps)
                repository.systems.append(system)
                self._view.update(system)

            # export
            CacheHelper.export_file(repository, self._config_service.section(CONF_CACHE_SECTION).get('filename'))
            self._view.finish()
        except (FileNotFoundError, FileFormatError) as e:
            raise RepomgrError(str(e))
        except IOError as e:
            raise RepomgrError(str(e))
