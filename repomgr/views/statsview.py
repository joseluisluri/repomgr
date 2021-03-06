from injector import inject

from repomgr.services import PrintService
from repomgr.views import View


class StatsView(View):
    @inject
    def __init__(self, print_service: PrintService):
        super().__init__(print_service)

    def update(self, repository):
        self._print_service.stats(repository)
