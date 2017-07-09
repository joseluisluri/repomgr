from injector import inject

from repomgr.models import Dump, System
from repomgr.services import PrintService
from repomgr.views import View


class SyncView(View):
    @inject
    def __init__(self, print_service: PrintService):
        super().__init__(print_service)

    def before(self):
        self._print_service.echo('Synchronizing...', '')

    def after(self):
        self._print_service.echo('Done.')