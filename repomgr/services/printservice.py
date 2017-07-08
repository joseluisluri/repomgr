import sys
from math import ceil

from injector import singleton

from repomgr.models import Repository
from repomgr.services.service import Service
from repomgr.utils import PrintHelper


@singleton
class PrintService(Service):

    @staticmethod
    def echo(output: str, end: str = None):
        print(output, end=end, flush=True, file=sys.stdout)

    @staticmethod
    def error(message: str):
        print('\nAn error has occurred: %s' % str(message), file=sys.stderr)

    @staticmethod
    def progress(index: float, total: float, length: float = 20):
        print('Progress: [{completed}>{pending}] {percent}%'.format(
            completed='=' * round(length * (index / total)),
            pending=' ' * round(length - round(length * (index / total))),
            percent=str(ceil(index / total * 100))),
            end='\r'
        )

    @staticmethod
    def clear():
        print(' ' * 80, end='\r')

    @classmethod
    def stats(cls, repository: Repository):
        print('Datetime. %s' % str(repository.modified))
        print('Systems: %s' % len(repository.systems))
        print('Dumps: %s' % repository.dumps)
        print('Roms: %s' % repository.roms)
        print('Size: %s' % PrintHelper.human_size(repository.size))
