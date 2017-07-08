from abc import ABCMeta, abstractmethod


class Controller:
    __metaclass__ = ABCMeta

    @abstractmethod
    def run(self, args: dict):
        pass
