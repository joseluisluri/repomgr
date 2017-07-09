import io
import os

from injector import inject, singleton

from repomgr.errors import ServiceError
from repomgr.models import Repository

from repomgr.constants import CONF_CACHE_SECTION
from repomgr.services import ConfigService, Service, SerializeService


@singleton
class CacheService(Service):
    @inject
    def __init__(self, config_service: ConfigService, serialize_service: SerializeService):
        self._serialize_service = serialize_service
        self._filename = config_service.section(CONF_CACHE_SECTION).get('filename')

    @property
    def filename(self) -> str:
        return self._filename

    @property
    def cache_exists(self) -> bool:
        return os.path.exists(self._filename)

    def import_cache(self, filename: str = None) -> Repository:
        try:
            with io.open(filename or self._filename, 'r', encoding='utf-8') as f:
                return self._serialize_service.unserialize(f.read())
        except IOError:
            raise ServiceError('unable to read cache')

    def export_cache(self, repository: Repository, filename: str = None):
        try:
            with io.open(filename or self._filename, 'w', encoding='utf-8') as f:
                f.write(self._serialize_service.serialize(repository))
        except IOError:
            raise ServiceError('unable to write cache')
