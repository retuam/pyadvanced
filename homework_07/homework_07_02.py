# Создать базу данных студентов. У студента есть факультет,
# группа, оценки, номер студенческого билета. Написать программу,
# с двумя ролями: Администратор, Пользователь. Администратор
# может добавлять, изменять существующих студентов.
# Пользователь может получать список отличников, список всех
# студентов, искать студентов по номеру студенческого, получать
# полную информацию о конкретном студенте (включая оценки,
# факультет)
from homework_07 import homework_07_01 as cm


class Users:

    @staticmethod
    def get_login():
        return str(input('Enter your login: '))

    @staticmethod
    def get_password():
        return str(input('Enter your password: '))

    def __init__(self, login, password):
        self._login = login
        self._password = password
        self._role = None


if __name__ == '__main__':
    db = 'students.db'

    with cm.DataConn(db) as conn:
        cursor = conn.cursor()
        Users().get_login

        students = cursor.execute("SELECT * FROM students")
        for row in students:
            print(row)

