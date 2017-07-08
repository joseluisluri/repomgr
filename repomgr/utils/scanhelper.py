import os
from datetime import datetime
from zipfile import ZipFile, BadZipFile

from repomgr.errors import FileFormatError
from repomgr.models import Dump, Rom


class ScanHelper:
    @staticmethod
    def scan_zip(path: str) -> Dump:
        """"Returns a ROM model for the specified compressed rom.

        Can throws: FileNotFoundError, FileFormatError
        """
        try:
            zipfile: ZipFile = ZipFile(path, 'r')
        except BadZipFile as e:
            raise FileFormatError('File is not a Zip: ' + path) from e

        if len(zipfile.infolist()) is 0:
            raise FileFormatError('Zipfile is empty: ' + path)

        roms: [Rom] = []
        for entity in zipfile.infolist():
            if entity.is_dir():
                raise FileFormatError('ROM cannot be a directory: ' + path)
            else:
                rom: Rom = Rom(name=entity.filename,
                               modified=datetime(*entity.date_time),
                               size=entity.file_size,
                               crc32=hex(entity.CRC))
                roms.append(rom)

        return Dump(name=os.path.splitext(path)[0],
                    zipfile=path,
                    roms=roms)

    @staticmethod
    def scan_dir(path: str, callback: callable = None) -> [Dump]:
        """Returns a list of ROMs for the specified directory.

        callback(rom, index, total) can be use to listen the procedure progress.
        Can throws: FileNotFoundError, FileFormatError
        """
        if not os.path.exists(path):
            raise FileNotFoundError('Cannot find the path specified: ' + path)

        dumps: [Dump] = []
        for (path, dirs, files) in os.walk(path):
            i: int = 0
            total: int = len(files)
            for file in sorted(files):
                dump: Dump = ScanHelper.scan_zip(os.path.join(path, file))
                dumps.append(dump)
                if callback is not None:
                    callback(dump=dump, index=i, total=total)
                i += 1

        return dumps
