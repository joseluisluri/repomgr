import logging
import sys
from argparse import ArgumentParser

from injector import Injector

from repomgr.constants import *
from repomgr.controllers import Controller, SyncController, InfoController, SearchController, StatsController, \
    UpdateController
from repomgr.errors import RepomgrError, ServiceError
from repomgr.utils import PrintHelper


def get_parser_args():
    parser: ArgumentParser = ArgumentParser(prog=NAME, description=DESCRIPTION, epilog=EPILOG)
    subparsers: any = parser.add_subparsers(dest='command', help=COMMAND_HELP)

    # search
    parser_search: any = subparsers.add_parser(SEARCH_CMD_NAME, help=SEARCH_CMD_HELP)
    parser_search.add_argument(SEARCH_ARG_NAME, nargs='*', help=SEARCH_ARG_HELP, type=str)

    # info
    parser_info: any = subparsers.add_parser(INFO_CMD_NAME, help=INFO_CMD_HELP)
    parser_info.add_argument(INFO_ARG_NAME, help=INFO_ARG_HELP, type=str)

    # stats
    parser_stats: any = subparsers.add_parser(STATS_CMD_NAME, help=STATS_CMD_HELP)
    parser_stats.add_argument(STATS_ARG_NAME, nargs='?', help=STATS_ARG_HELP, type=str)

    # update
    parser_update: any = subparsers.add_parser(UPDATE_CMD_NAME, help=UPDATE_CMD_HELP)
    parser_update.add_argument(UPDATE_ARG_NAME, nargs='?', help=UPDATE_ARG_HELP, type=str)

    # sync
    subparsers.add_parser(SYNC_CMD_NAME, help=SYNC_CMD_HELP)
    return parser

def main(argv: dict):
    commands: dict = {
        SEARCH_CMD_NAME: SearchController,
        INFO_CMD_NAME: InfoController,
        STATS_CMD_NAME: StatsController,
        UPDATE_CMD_NAME: UpdateController,
        SYNC_CMD_NAME: SyncController
    }

    try:
        # dependency injection
        injector: Injector = Injector()

        # logging
        #logging.basicConfig(filename=config.logging.filename, format=LOG_FORMAT, level=config.logging.level)
        logger: logging.Logger = logging.getLogger(NAME)

        # args management
        parser: ArgumentParser = get_parser_args()
        args: any = parser.parse_args(argv)

        # load controller by reflection
        if args.command in commands.keys():
            clazz: type = commands.get(args.command)
            controller: Controller = injector.get(clazz)
            controller.run(args.__dict__)
        else:
            parser.print_help()
    except ServiceError as e:
        PrintHelper.error(str(e))
    except RepomgrError as e:
        PrintHelper.error(str(e))

if __name__ == '__main__':
    main(sys.argv[1:])