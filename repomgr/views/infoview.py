from injector import inject

from repomgr.models import Dump, System
from repomgr.services import PrintService
from repomgr.views import View


class InfoView(View):
    @inject
    def __init__(self, print_service: PrintService):
        super().__init__(print_service)

    def update(self, system: System, dump: Dump):
        self._print_service.dump(system, dump)