from abc import ABCMeta
from logging import Logger

from repomgr.models import Config


class Handler:
    __metaclass__ = ABCMeta

    def __init__(self, config: Config, logger: Logger):
        self._config = config
        self._logger = logger
