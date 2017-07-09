from abc import ABCMeta
from abc import abstractmethod

from injector import inject

from repomgr.services import PrintService


class View:
    __metaclass__ = ABCMeta

    def __init__(self, print_service: PrintService):
        self._print_service: PrintService = print_service

    def nocache(self):
        self._print_service.echo('ROM index cache must be generated before')
