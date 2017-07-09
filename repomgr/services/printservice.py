import sys
from math import ceil

from injector import singleton
from tabulate import tabulate

from repomgr.models import Repository, System, Dump
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

    @classmethod
    def table(cls, content: [tuple]):
        rows = []
        for entry in content:
            system, dump = entry
            rows.append([
                dump.uuid,
                dump.name,
                PrintHelper.human_size(dump.size),
                system.name
            ])

        print(tabulate(rows, headers=['Id', 'Name', 'Size', 'System']), end='\n\n')

    @classmethod
    def dump(cls, system: System, dump: Dump):
        print('Dump: %s' % dump.name)
        print('Zip: %s' % dump.zip)
        print('Contains: %d rom(s)' % len(dump.roms))
        for rom in dump.roms:
            print(' - Name: %s' % rom.name)
            print(' - System: %s' % system.name)
            print(' - Modified: %s' % str(rom.modified))
            print(' - Size: %s' % PrintHelper.human_size(rom.size))
            print(' - Crc32: %s' % rom.crc32[2:])
