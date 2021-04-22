from tinydb import TinyDB, Query, where
from threading import Thread, Lock

from tinydb.operations import add


class TinyDBDatabaseMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class TinyDBDatabase(metaclass=TinyDBDatabaseMeta):
    database: TinyDB = None

    def __init__(self, json_file: str) -> None:
        self.database = TinyDB(json_file)
        self.database.insert({"please": "Just work."})

    def add_user(self, guild: str, author_id: str):
        table = self.database.table(guild)
        table.insert({
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
        table = self.database.table(guild)
        table.update({'nick': author_nick}, where('author') == author_id)

    def add_stats_to_user(self, guild: str, author_id: str, k: int, j: int, p: int, ch: int, g: int, sz: int, xd: int):
        table = self.database.table(guild)
        table.update_multiple([
            (add('k', k), where('author') == author_id),
            (add('j', j), where('author') == author_id),
            (add('p', p), where('author') == author_id),
            (add('ch', ch), where('author') == author_id),
            (add('g', g), where('author') == author_id),
            (add('sz', sz), where('author') == author_id),
            (add('xd', xd), where('author') == author_id)
        ])

    def drop_server_table(self, guild: str):
        self.database.drop_table(guild)
