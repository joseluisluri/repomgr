import io

import yaml
from injector import singleton

from repomgr.constants import CONF_CACHE_SECTION
from repomgr.constants import CONF_FILENAME
from repomgr.constants import CONF_LOGGING_SECTION
from repomgr.constants import CONF_SYSTEMS_SECTION
from repomgr.errors import ServiceError
from repomgr.services.service import Service


@singleton
class ConfigService(Service):

    _mandatory_sections: dict = {
        CONF_CACHE_SECTION: dict,
        CONF_LOGGING_SECTION: dict,
        CONF_SYSTEMS_SECTION: list
    }

    def __init__(self):
        try:
            with io.open(CONF_FILENAME, 'r', encoding='utf8') as stream:
                dct: dict = yaml.load(stream)
                if type(dct) is not dict or not all(x in dct.keys() for x in self._mandatory_sections.keys()):
                    raise ServiceError('{} has a wrong format'.format(CONF_FILENAME))
                else:
                    self._config = dct
        except FileNotFoundError:
            raise ServiceError('{} is missing'.format(CONF_FILENAME))
        except IOError:
            raise ServiceError('Failed reading {}'.format(CONF_FILENAME))

    def section(self, section: str) -> any:
        if section not in self._config.keys():
            raise ServiceError('Section {} not found in {}'.format(section, CONF_FILENAME))
        else:
            return self._config.get(section)
