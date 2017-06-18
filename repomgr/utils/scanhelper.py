import os
from datetime import datetime
from zipfile import ZipFile, ZipInfo, BadZipFile

from repomgr.errors import FileFormatError
from repomgr.models import Rom


class ScanHelper:
    @staticmethod
    def scan_zip(path: str) -> Rom:
        """"Returns a ROM model for the specified compressed rom.

        Can throws: FileNotFoundError, FileFormatError
        """
        try:
            zipfile: ZipFile = ZipFile(path, 'r')
        except BadZipFile as e:
            raise FileFormatError('File is not a Zip: ' + path) from e

        if len(zipfile.infolist()) is not 1:
            raise FileFormatError('Zipfile must contain one rom: ' + path)

        entity: ZipInfo = zipfile.infolist()[0]

        if entity.is_dir():
            raise FileFormatError('ROM cannot be a directory: ' + path)
        else:
            rom: Rom = Rom(name=entity.filename,
                           modified=datetime(*entity.date_time),
                           size=entity.file_size,
                           crc32=hex(entity.CRC),
                           zip=path)
            return rom

    @staticmethod
    def scan_dir(path: str, callback: callable = None) -> [Rom]:
        """Returns a list of ROMs for the specified directory.

        callback(rom, index, total) can be use to listen the procedure progress.
        Can throws: FileNotFoundError, FileFormatError
        """
        if not os.path.exists(path):
            raise FileNotFoundError('Cannot find the path specified: ' + path)

        roms: [Rom] = []
        for (path, dirs, files) in os.walk(path):
            i: int = 0
            total: int = len(files)
            for file in sorted(files):
                rom: Rom = ScanHelper.scan_zip(os.path.join(path, file))
                roms.append(rom)
                if callback is not None:
                    callback(rom=rom, index=i, total=total)
                i += 1

        return roms
