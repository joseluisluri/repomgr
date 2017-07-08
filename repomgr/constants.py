NAME = 'repomgr'
DESCRIPTION = 'Command-line tool for handling ROM repository'
VERSION = 0.3
EPILOG = 'One tool to rule them all, One tool to find them'

CONF_FILENAME = 'config.yml'

CONF_CACHE_SECTION = 'cache'
CONF_LOGGING_SECTION = 'logging'
CONF_SYSTEMS_SECTION = 'systems'

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

STATS_CMD_NAME = 'stats'
STATS_CMD_HELP = 'display stats information.'
STATS_ARG_NAME = 'system'
STATS_ARG_HELP = 'stats'
