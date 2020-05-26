# Создать базу данных студентов. У студента есть факультет,
# группа, оценки, номер студенческого билета. Написать программу,
# с двумя ролями: Администратор, Пользователь. Администратор
# может добавлять, изменять существующих студентов.
# Пользователь может получать список отличников, список всех
# студентов, искать студентов по номеру студенческого, получать
# полную информацию о конкретном студенте (включая оценки,
# факультет)
from homework_07 import homework_07_01 as cm


class Student:

    def __init__(self, *student):
        self._id, self._first_name, self._last_name, self._stnumber, self._faculty = student

    def __str__(self):
        return f'{self._first_name} {self._last_name} ({self._stnumber}) {self._faculty}'

    def get_id(self):
        return self._id

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

    def get_stnumber(self):
        return self._stnumber

    def set_stnumber(self, value):
        self._stnumber = value

    stnumber = property(get_stnumber, set_stnumber)

    def get_faculty(self):
        return self._faculty

    def set_faculty(self, value):
        self._faculty = value

    faculty = property(get_faculty, set_faculty)


class Users:

    def get_login(self):
        return self._login

    def set_login(self):
        self._login = str(input('Enter your login: '))

    def get_password(self):
        return self._password

    def set_password(self):
        self._password = str(input('Enter your password: '))

    def __init__(self):
        self._id = None
        self._login = None
        self._password = None
        self._role = None
        self._number = None
        self._menu = {}

    def get_id(self):
        return self._id

    def set_session(self, row):
        if row:
            self._role, self._id = row[3], row[0]

    def get_number(self):
        return self._number

    def set_number(self, value):
        self._number = value

    number = property(get_number, set_number)

    def get_menu(self):
        self._menu = {
            0: 'exit',
            1: 'all students',
            2: 'only graduated students',
            3: 'select student by id',
            4: 'view student if selected id',
        }
        if self._role == 'admin':
            self._menu[5] = 'edit student if selected id'
            self._menu[6] = 'delete student if selected id'
            self._menu[7] = 'add student'
        if self._role:
            return self._menu
        else:
            return 'No authorized user'


class StudentDb:

    def __init__(self, _conn):
        self.conn = _conn
        self.cursor = self.conn.cursor()

    def get_user(self, login, password):
        self.cursor.execute("SELECT * FROM users WHERE login = ? AND password = ?", (login, password))
        return self.cursor.fetchone()

    def get_students(self):
        self.cursor.execute("SELECT * FROM students WHERE 1")
        return self.cursor.fetchall()

    def get_students_graduated(self):
        self.cursor.execute("""SELECT students.* FROM students
                                       LEFT JOIN marks ON marks.student_id = students.id WHERE marks.mark = 5""")
        return self.cursor.fetchall()

    def get_students_by_number(self, stnumber):
        self.cursor.execute("SELECT * FROM students WHERE stnumber = ?", (stnumber, ))
        return self.cursor.fetchone()

    def get_marks(self, number):
        self.cursor.execute("SELECT * FROM marks WHERE student_id = ?", (number, ))
        return self.cursor.fetchall()

    def update_student(self, student):
        self.cursor.execute("""UPDATE students SET first_name = ?, last_name = ?, stnumber = ?, faculty = ?
                                   WHERE stnumber = ?""", (student.first_name, student.last_name, student.stnumber,
                                                     student.faculty, student.stnumber))
        self.conn.commit()

    def delete_student(self, number):
        self.cursor.execute("DELETE FROM students WHERE id = ?", (number, ))
        self.conn.commit()

    def insert_student(self, student):
        self.cursor.execute("INSERT INTO students (first_name, last_name, stnumber, faculty) VALUES (?, ?, ?, ?)",
                                   (student.first_name, student.last_name, student.stnumber, student.faculty))
        self.conn.commit()


if __name__ == '__main__':
    db = 'students_new.db'

    user = Users()
    user.set_login()
    user.set_password()

    with cm.DataConn(db) as conn:
        stdb = StudentDb(conn)
        user.set_session(stdb.get_user(user.get_login(), user.get_password()))

        while user.get_id():
            print(*[(str(key) + ' - ' + value) for key, value in user.get_menu().items()])
            action = int(input('Select action: '))
            if action in user.get_menu().keys():
                if not action:
                    user = Users()
                elif action == 1:
                    [print(row) for row in stdb.get_students()]
                elif action == 2:
                    [print(row) for row in stdb.get_students_graduated()]
                elif action == 3:
                    value = stdb.get_students_by_number(int(input("Select number: ")))
                    if value:
                        student = Student(*value)
                        user.number = student.get_id()
                        print(student)
                    else:
                        print('Wrong number')
                elif action in (4, 5, 6) and not user.number:
                    print('Not selected student number')
                elif action == 4 and user.number:
                    print(student)
                    for mark in stdb.get_marks(user.number):
                        print(f'{mark[3]}: {mark[1]}')
                elif action == 5 and user.number:
                    first_name = input('Edit first name or pass: ')
                    if first_name:
                        student.first_name = str(first_name)

                    last_name = input('Edit last name or pass: ')
                    if last_name:
                        student.last_name = str(last_name)

                    stnumber = input('Edit student number or pass: ')
                    if stnumber:
                        student.number = int(stnumber)

                    faculty = input('Edit student faculty or pass: ')
                    if faculty:
                        student.faculty = str(faculty)

                    stdb.update_student(student)
                elif action == 6 and user.number:
                    stdb.delete_student(user.number)
                    del student
                    user.number = None
                elif action == 7:
                    student = Student(None, str(input('Edit first name: ')), str(input('Edit last name: ')),
                                      int(input('Edit student number: ')), str(input('Edit student faculty: ')))
                    stdb.insert_student(student)
            else:
                print('Unknown action')



