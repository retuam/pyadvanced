# Написать контекстный менеджер для работы с SQLite DB.
import sqlite3


class DataConn:

    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        if exc_type == ValueError:
            print("ValueError exception db")


if __name__ == '__main__':
    db = 'students.db'

    with DataConn(db) as conn:
        cursor = conn.cursor()
