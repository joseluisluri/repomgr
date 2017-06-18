import logging
import argparse
import sys

from repomgr.constants import *
from repomgr.errors import RepomgrError
from repomgr.handlers import UpdateHandler, InfoHandler, SearchHandler
from repomgr.models import Config
from repomgr.utils import ConfigHelper, PrintHelper


def get_parser_args():
    parser: argparse.ArgumentParser = argparse.ArgumentParser(prog=NAME, description=DESCRIPTION, epilog=EPILOG)
    subparsers: any = parser.add_subparsers(dest='cmd', help=COMMAND_HELP)

    # search
    parser_search: any = subparsers.add_parser(SEARCH_CMD_NAME, help=SEARCH_CMD_HELP)
    parser_search.add_argument(SEARCH_ARG_NAME, nargs='*', help=SEARCH_ARG_HELP, type=str)

    # info
    parser_info: any = subparsers.add_parser(INFO_CMD_NAME, help=INFO_CMD_HELP)
    parser_info.add_argument(INFO_ARG_NAME, help=INFO_ARG_HELP, type=str)

    # update
    subparsers.add_parser(UPDATE_CMD_NAME, help=UPDATE_CMD_HELP)

    return parser


def main(argv: dict):
    try:
        # config
        config: Config = ConfigHelper.from_file(CONF_FILENAME)

        # logging
        logging.basicConfig(filename=config.logging.filename, format=LOG_FORMAT, level=config.logging.level)
        logger: logging.Logger = logging.getLogger(NAME)

        # args management
        parser: argparse.ArgumentParser = get_parser_args()
        args = parser.parse_args(argv)
        if args.cmd == SEARCH_CMD_NAME:
            SearchHandler(config, logger).run(args.seed)
        elif args.cmd == INFO_CMD_NAME:
            InfoHandler(config, logger).run(args.crc32)
        elif args.cmd == UPDATE_CMD_NAME:
            UpdateHandler(config, logger).run()
        else:
            parser.print_help()
    except RepomgrError as e:
        logging.error(str(e))
        PrintHelper.error(str(e))

if __name__ == '__main__':
    main(sys.argv[1:])