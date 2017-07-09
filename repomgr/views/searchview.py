from injector import inject

from repomgr.services import PrintService
from repomgr.views import View


class SearchView(View):
    @inject
    def __init__(self, print_service: PrintService):
        super().__init__(print_service)
        self._matches: list = None

    def update(self, matches: [tuple] = None):
        if len(matches):
            self._print_service.table(matches)
        else:
            self._print_service.echo('0 results')