from homework_09.models_for_09 import activerecord as ar


class Student(ar.ActiveRecord):

    def __init__(self, id=None, first_name=None, last_name=None, padre_name=None, group_id=None, faculty_id=None,
                 curator_id=None):
        self._table = 'student'
        if id:
            self._id = id
            row = self.one()
            try:
                self._first_name = row['first_name']
                self._last_name = row['last_name']
                self._padre_name = row['padre_name']
                self._group_id = row['group_id']
                self._faculty_id = row['faculty_id']
                self._curator_id = row['curator_id']
            except TypeError:
                print('No data exist by ID')
        if first_name:
            self._first_name = first_name
        if last_name:
            self._last_name = last_name
        if padre_name:
            self._padre_name = padre_name
        if group_id:
            self._group_id = group_id
        if faculty_id:
            self._faculty_id = faculty_id
        if curator_id:
            self._curator_id = curator_id

    def __str__(self):
        return f'{self._id} -> {self._first_name} {self._last_name} {self._padre_name}'

    def get_group_id(self):
        return self._group_id

    def set_group_id(self, value):
        self._group_id = value

    group_id = property(get_group_id, set_group_id)

    def get_faculty_id(self):
        return self._faculty_id

    def set_faculty_id(self, value):
        self._faculty_id = value

    faculty_id = property(get_faculty_id, set_faculty_id)

    def get_curator_id(self):
        return self._curator_id

    def set_curator_id(self, value):
        self._curator_id = value

    curator_id = property(get_curator_id, set_curator_id)

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, value):
        self._first_name = value

    first_name = property(get_first_name, set_first_name)

    def get_last_name(self):
        return self._last_name

    def set_last_name(self, value):
        self._last_name = value

    last_name = property(get_last_name, set_last_name)

    def get_padre_name(self):
        return self._padre_name

    def set_padre_name(self, value):
        self._padre_name = value

    padre_name = property(get_padre_name, set_padre_name)

    def get_insert(self):
        return f'''INSERT INTO {self._table} (first_name, last_name, padre_name, faculty_id, group_id, curator_id) 
               VALUES (?, ?, ?, ?, ?, ?)'''

    def get_insert_data(self):
        return self.first_name, self.last_name, self.padre_name, self.faculty_id, self.group_id, self.curator_id

    def get_update(self):
        return f'''UPDATE {self._table} SET first_name = ?, last_name = ?, padre_name = ?, faculty_id = ?, group_id = ?,
         curator_id = ? WHERE id = ?'''

    def get_update_data(self):
        return self.first_name, self.last_name, self.padre_name, self.faculty_id, self.group_id, self.curator_id, self.id

    def graduated(self):
        _data = {}
        with self.get_db() as conn:
            conn.row_factory = self.get_db_factory()
            cursor = conn.cursor()
            cursor.execute(f'''SELECT s.*, ROUND(AVG(mark), 2) as avg_mark FROM {self._table} s 
            LEFT JOIN mark m ON m.student_id = s.id WHERE 1 GROUP BY s.id HAVING AVG(mark) > 4''')
            for row in cursor.fetchall():
                _data[row['id']] = row
        return _data

    def all_format(self):
        _data = {}
        with self.get_db() as conn:
            conn.row_factory = self.get_db_factory()
            cursor = conn.cursor()
            cursor.execute(f'''SELECT s.*, ROUND(AVG(mark), 2) as avg_mark FROM {self._table} s 
            LEFT JOIN mark m ON m.student_id = s.id WHERE 1 GROUP BY s.id''')
            for row in cursor.fetchall():
                _data[row['id']] = row
        return _data

    def curators(self, curator_id):
        _data = {}
        with self.get_db() as conn:
            conn.row_factory = self.get_db_factory()
            cursor = conn.cursor()
            cursor.execute(f'SELECT * FROM {self._table} WHERE curator_id = ?', (curator_id, ))
            for row in cursor.fetchall():
                _data[row['id']] = row
        return _data
