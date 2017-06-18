NAME = 'repomgr'
DESCRIPTION = 'Command-line tool for handling ROM repository'
EPILOG = 'One Tool to rule them all, One Tool to find them'

CONF_FILENAME = 'config.yml'

LOG_FILENAME = 'output.log'
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

COMMAND_HELP = 'command help'

SEARCH_CMD_NAME = 'search'
SEARCH_CMD_HELP = 'performs a full text search on ROM index cache for the specified seed.'
SEARCH_ARG_NAME = 'seed'
SEARCH_ARG_HELP = 'words separated by spaces'

INFO_CMD_NAME = 'info'
INFO_CMD_HELP = 'display ROM information'
INFO_ARG_NAME = 'crc32'
INFO_ARG_HELP = 'rom CRC32'

UPDATE_CMD_NAME = 'update'
UPDATE_CMD_HELP = 'resynchronize the ROM index cache from their repo.'
