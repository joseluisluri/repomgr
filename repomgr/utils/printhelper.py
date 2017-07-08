from tabulate import tabulate

from repomgr.models import System, Dump, Repository


class PrintHelper:

    @staticmethod
    def human_size(size: int) -> str:
        suffixes: [str] = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
        if size == 0:
            return '0 B'
        i: int = 0
        while size >= 1024 and i < len(suffixes) - 1:
            size /= 1024.
            i += 1
        f: float = ('%.2f' % size).rstrip('0').rstrip('.')
        return '%s %s' % (f, suffixes[i])

    @classmethod
    def summary(cls, system: System, dump: Dump):
        print('[{crc32}] {filename} - {size} - {system}'.format(filename=dump.name,
                                                                system=system.name,
                                                                size=cls.human_size(dump.size),
                                                                crc32=0))

    @classmethod
    def detailed(cls, system: System, dump: Dump):
        for rom in dump.roms:
            print('Name: %s' % rom.name)
            print('System: %s' % system.name)
            print('Modified: %s' % str(rom.modified))
            print('Size: %s' % cls.human_size(rom.size))
            print('Crc32: %s' % rom.crc32[2:])
            print('Zip: %s' % rom.zip)

    @classmethod
    def table(cls, content: [tuple]):
        rows = []
        for entry in content:
            system, dump = entry
            rows.append([
                0,  # crc
                dump.name,
                cls.human_size(dump.size),
                system.name
            ])

        print(tabulate(rows, headers=['CRC32', 'Name', 'Size', 'System']), end='\n\n')

    @classmethod
    def stats(cls, repository: Repository):
        print('Systems: %s' % len(repository.systems))
        print('Dumps: %s' % repository.dumps)
        print('Roms: %s' % repository.roms)
        print('Size: %s' % cls.human_size(repository.size))

    @staticmethod
    def echo(output: str, end: str = None):
        print(output, end=end, flush=True)

    @staticmethod
    def error(message: str):
        print('\nAn error has occurred: %s' % str(message))
