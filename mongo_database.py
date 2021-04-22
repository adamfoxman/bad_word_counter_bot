import pymongo
from threading import Thread, Lock


class MongoDatabaseMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class MongoDatabase(metaclass=MongoDatabaseMeta):
    client: pymongo.MongoClient = None
    database = None

    def __init__(self, address: str) -> None:
        self.client = pymongo.MongoClient(address)
        self.database = self.client['kurwiszon_database']

    def add_user(self, guild: str, author_id: str):
        table = self.database[str(guild)]
        table.insert_one({
            'author': author_id,
            'nick': '',
            'k': 0,
            'j': 0,
            'p': 0,
            'ch': 0,
            'g': 0,
            'sz': 0,
            'xd': 0
        })

    def set_user_nick(self, guild: str,author_id: str, author_nick: str):
        table = self.database[str(guild)]
        query = {'author': author_id}
        nick = {'$set': {'nick': author_nick}}
        table.update_one(query, nick)

    def add_stats_to_user(self, guild: str, author_id: str, k: int, j: int, p: int, ch: int, g: int, sz: int, xd: int):
        table = self.database[str(guild)]
        query = {'author': author_id}
        update = {'$inc': {
            'k': k,
            'j': j,
            'p': p,
            'ch': ch,
            'g': g,
            'sz': sz,
            'xd': xd
        }}
        table.update_one(query, update)

    def drop_server_table(self, guild: str):
        self.database.drop_collection(guild)
