from homework_09.models_for_09 import db


class ActiveRecord:

    _db = db.db

    def __init__(self, id=None, title=None, table=None):
        self._table = table
        if id:
            self._id = id
            row = self.one()
            try:
                self._title = row['title']
            except TypeError:
                print('No data exist by ID')
        if title:
            self._title = title

    def __str__(self):
        return f'{self._table}:{self._id} -> {self._title}'

    def get_table(self):
        return self._table

    def get_id(self):
        return self._id

    def set_id(self, value):
        self._id = value

    id = property(get_id, set_id)

    def get_title(self):
        return self._title

    def set_title(self, value):
        self._title = value

    title = property(get_title, set_title)

    def get_db(self):
        return db.DataConn(self._db)

    @staticmethod
    def get_db_factory():
        return db.dict_factory

    def one(self):
        with self.get_db() as conn:
            conn.row_factory = self.get_db_factory()
            cursor = conn.cursor()
            cursor.execute(f'SELECT * FROM {self._table} WHERE id = ?', (self._id, ))
            return cursor.fetchone()

    def all(self):
        _data = {}
        with self.get_db() as conn:
            conn.row_factory = self.get_db_factory()
            cursor = conn.cursor()
            cursor.execute(f'SELECT * FROM {self._table} WHERE 1')
            for row in cursor.fetchall():
                _data[row['id']] = row
        return _data

    def all_id(self):
        _data = []
        with self.get_db() as conn:
            conn.row_factory = self.get_db_factory()
            cursor = conn.cursor()
            cursor.execute(f'SELECT id FROM {self._table} WHERE 1')
            for row in cursor.fetchall():
                _data.append(row['id'])
        return _data

    def get_insert(self):
        return f'INSERT INTO {self._table} (title) VALUES (?)'

    def get_insert_data(self):
        return (self.title, )

    def create(self):
        with self.get_db() as conn:
            cursor = conn.cursor()
            cursor.execute(self.get_insert(), self.get_insert_data())
            conn.commit()
            conn.row_factory = self.get_db_factory()
            cursor = conn.cursor()
            cursor.execute(f'SELECT * FROM {self._table} WHERE 1 ORDER BY id DESC')
            return cursor.fetchone()

    def get_update(self):
        return f'UPDATE {self._table} SET title = ? WHERE id = ?'

    def get_update_data(self):
        return self.title, self.id

    def update(self):
        with self.get_db() as conn:
            cursor = conn.cursor()
            cursor.execute(self.get_update(), self.get_update_data())
            conn.commit()
            conn.row_factory = self.get_db_factory()
            cursor = conn.cursor()
            cursor.execute(f'SELECT * FROM {self._table} WHERE id = ?', (self.id, ))
            return cursor.fetchone()

    def delete(self):
        with self.get_db() as conn:
            cursor = conn.cursor()
            cursor.execute(f'DELETE FROM {self._table} WHERE id = ?', (self.id, ))
            conn.commit()
        return True
