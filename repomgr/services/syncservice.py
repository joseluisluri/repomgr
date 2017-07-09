import json

from injector import singleton, inject
from pymongo import MongoClient
from pymongo.database import Database

from repomgr.constants import CONF_SYNC_SECTION
from repomgr.models import Repository
from repomgr.services import Service, ConfigService, SerializeService


@singleton
class SyncService(Service):

    @inject
    def __init__(self, config_service: ConfigService, serialize_service: SerializeService):
        config: dict = config_service.section(CONF_SYNC_SECTION)
        self._host: str = config.get('host', 'localhost')
        self._port: int = config.get('port', 27017)
        self._database: str = config.get('database', '')
        self._collection: str = config.get('collection', '')
        self._serialize_service: SerializeService = serialize_service

    def push(self, repository: Repository):
        data: str = self._serialize_service.serialize(repository)
        client: MongoClient = MongoClient(self._host, self._port)
        database: Database = client[self._database]
        database.drop_collection(self._collection)
        collection: Database = database[self._collection]
        collection.insert_one(json.loads(data))
