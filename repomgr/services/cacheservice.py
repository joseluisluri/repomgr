from injector import inject

from repomgr.constants import CONF_CACHE_SECTION
from repomgr.services import ConfigService
from repomgr.services import Service


class CacheService(Service):
    @inject
    def __init__(self, config_service: ConfigService):
        self._filename = config_service.section(CONF_CACHE_SECTION).get('filename')

    @property
    def filename(self) -> str:
        return self._filename
