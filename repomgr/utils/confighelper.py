import io

import yaml

from repomgr.errors import RepomgrError
from repomgr.models.config import _Logging, Config, _System, _Cache
from repomgr.constants import CONF_FILENAME

class ConfigHelper:
    @staticmethod
    def from_file(path: str) -> Config:
            try:
                with io.open(path, 'r', encoding='utf8') as stream:
                    parse = yaml.load(stream)
                    cache: _Cache = _Cache(parse['cache']['filename'])
                    logging: _Logging = _Logging(parse['logging']['filename'], int(parse['logging']['level']))
                    systems: [_System] = []
                    for item in parse['systems']:
                        systems.append(_System(item['name'], item['tag'], item['path']))
                    config: Config = Config(cache, logging, systems)
                    return config
            except KeyError as e:
                raise RepomgrError('A config parameter {} is not defined in {}'.format(str(e), path))
            except ValueError as e:
                raise RepomgrError('A config parameter has not a valid value')
            except FileNotFoundError as e:
                raise RepomgrError('{} is missing'.format(CONF_FILENAME))
