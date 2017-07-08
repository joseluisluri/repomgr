from injector import inject

from repomgr.models import Dump
from repomgr.models import System
from repomgr.services import PrintService
from repomgr.views import View


class UpdateView(View):
    @inject
    def __init__(self, print_service: PrintService):
        self._print_service = print_service
        self._print_service.echo('Generating ROM index cache:')

    def progress(self, dump: Dump, index: int, total: int):
        self._print_service.progress(index, total)

    def update(self, system: System):
        self._print_service.clear()
        self._print_service.echo('{} ({} dumps)'.format(system.name, len(system.dumps)))

    def finish(self):
        self._print_service.echo('All done. :)')
