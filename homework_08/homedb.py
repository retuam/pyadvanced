# Написать контекстный менеджер для работы с SQLite DB.
import sqlite3


def dict_factory(cursor, row):
    d = {}
    for i, column in enumerate(cursor.description):
        d[column[0]] = row[i]
    return d


class DataConn:

    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        if exc_type:
            raise exc_type(exc_val)
