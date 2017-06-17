import io

import yaml

from ..errors import RepomgrError
from ..models.config import _Logging, Config, _System, _Cache


class ConfigHelper:
    @staticmethod
    def from_file(path: str) -> Config:
        with io.open(path, 'r', encoding='utf8') as stream:
            try:
                parse = yaml.load(stream)
                cache: _Cache = _Cache(parse['cache']['filename'])
                logging: _Logging = _Logging(parse['logging']['filename'], int(parse['logging']['level']))
                systems: [_System] = []
                for item in parse['systems']:
                    systems.append(_System(item['name'], item['tag'], item['path']))
                return Config(cache, logging, systems)
            except KeyError as e:
                raise RepomgrError('A config parameter {} is not defined in {}'.format(str(e), path))
            except ValueError as e:
                raise RepomgrError('A config parameter has not a valid value')
