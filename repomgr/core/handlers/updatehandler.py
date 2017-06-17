from ..errors import FileFormatError, RepomgrError
from ..handlers import Handler
from ..models import Rom, System
from ..utils import CacheHelper, ScanHelper, PrintHelper


class UpdateHandler(Handler):

    def _progress(self, rom: Rom, index: int, total: int):
        percent: float = round(index / total * 100)
        PrintHelper.echo('Progress: {}%'.format(str(percent)), end='\r')
        self._logger.info('caching: ' + str(rom))

    def run(self):
        try:
            PrintHelper.echo('Generating ROM index cache:')

            # build repository model
            repository: [System] = []
            for conf_system in self._config.systems:
                roms = ScanHelper.scan_dir(conf_system.path, self._progress)
                system: System = System(conf_system.name, conf_system.tag, conf_system.path, roms)
                repository.append(system)
                PrintHelper.echo('{} ({} roms)'.format(system.name, len(system.roms)))

            # export
            CacheHelper.export_file(repository, self._config.cache.filename)
            PrintHelper.echo('All done. :)')
        except (FileNotFoundError, FileFormatError) as e:
            raise RepomgrError(str(e))
