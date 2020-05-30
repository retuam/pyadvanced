from homework_09.models_for_09 import activerecord as ar


class Mark(ar.ActiveRecord):

    def __init__(self, id=None, mark=None, student_id=None, course_id=None):
        self._table = 'mark'
        if id:
            self._id = id
            row = self.one()
            self._mark = row['mark']
            self._student_id = row['student_id']
            self._course_id = row['course_id']
        if mark:
            self._mark = mark
        if student_id:
            self._student_id = student_id
        if course_id:
            self._course_id = course_id

    def __str__(self):
        return f'{self._id} -> {self._student_id}:{self._course_id}-{self._mark}'

    def get_student_id(self):
        return self._student_id

    def set_student_id(self, value):
        self._student_id = value

    student_id = property(get_student_id, set_student_id)

    def get_course_id(self):
        return self._course_id

    def set_course_id(self, value):
        self._course_id = value

    course_id = property(get_course_id, set_course_id)

    def get_mark(self):
        return self._mark

    def set_mark(self, value):
        self._mark = value

    mark = property(get_mark, set_mark)

    def get_insert(self):
        return f'INSERT INTO {self._table} (mark, student_id, course_id) VALUES (?, ?, ?)'

    def get_insert_data(self):
        return self.mark, self.student_id, self.course_id

    def get_update(self):
        return f'UPDATE {self._table} SET title = ?, student_id = ?, course_id = ? WHERE id = ?'

    def get_update_data(self):
        return self.mark, self.student_id, self.course_id, self.id
