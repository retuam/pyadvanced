# Создайте класс ПЕРСОНА с абстрактными методами, позволяющими
# вывести на экран информацию о персоне, а также определить ее возраст (в
# текущем году). Создайте дочерние классы: АБИТУРИЕНТ (фамилия, дата
# рождения, факультет), СТУДЕНТ (фамилия, дата рождения, факультет, курс),
# ПРЕПОДАВАТЕЛЬ (фамилия, дата рождения, факультет, должность, стаж),
# со своими методами вывода информации на экран и определения возраста.
# Создайте список из n персон, выведите полную информацию из базы на
# экран, а также организуйте поиск персон, чей возраст попадает в заданный
# диапазон.
import abc
import time


class Person(abc.ABC):

    person_list = []

    def __init__(self, name, birthday):
        self._name = name
        self._year = int(time.strftime("%Y", time.localtime()))

        self._birthday_list = birthday.split('.')
        if len(self._birthday_list) == 3:
            self._birth_year = int(self._birthday_list[2])

        self.year_old()

        Person.person_list.append(self)


    def __str__(self):
        return str((self._name, self._year_old))

    @staticmethod
    def search(year_start, year_end):
        return [row for row in Person.person_list if year_start <= row.get_year_old() <= year_end]

    @abc.abstractmethod
    def show(self):
        print(f'Person {self._name}, {self._year_old} year old')

    @abc.abstractmethod
    def year_old(self):
        self._year_old = self._year - self._birth_year

    def get_year_old(self):
        return self._year_old


class Abiturient(Person):

    def __init__(self, name, birthday, faculty):
        super().__init__(name, birthday)
        self._faculty = faculty

    def show(self):
        print(f'Abiturient {self._name}, {self._year_old} year old')

    def year_old(self):
        self._year_old = self._year - self._birth_year - 1


class Student(Abiturient):

    def __init__(self, name, birthday, faculty, course):
        super().__init__(name, birthday, faculty)
        self._course = course

    def show(self):
        print(f'Student {self._name}, {self._year_old} year old')

    def year_old(self):
        self._year_old = self._year - self._birth_year + 1


class Master(Abiturient):

    def __init__(self, name, birthday, faculty, position, experience):
        super().__init__(name, birthday, faculty)
        self._position = position
        self._experience = experience

    def show(self):
        print(f'Master {self._name}, {self._year_old} year old')

    def year_old(self):
        self._year_old = self._year - self._birth_year + 2


if __name__ == '__main__':
    persons = []

    persons.append(Abiturient('Name 1', '10.12.2003', 'Physics'))
    persons.append(Abiturient('Name 2', '05.10.2004', 'Mathematics'))
    persons.append(Abiturient('Name 3', '06.11.2003', 'History'))
    persons.append(Abiturient('Name 4', '10.12.2004', 'Philosophy'))

    persons.append(Student('Name 5', '07.04.2001', 'Physics', 2))
    persons.append(Student('Name 6', '18.08.2000', 'Mathematics', 3))
    persons.append(Student('Name 7', '21.09.2002', 'History', 1))
    persons.append(Student('Name 8', '29.10.1999', 'Philosophy', 4))

    persons.append(Master('Name 9', '15.03.1984', 'History', 'Doct.', 2))
    persons.append(Master('Name 10', '30.09.1980', 'Philosophy', 'Prof.', 13))

    for person in persons:
        person.show()

    print(Person.person_list)
    year_start = 20
    year_end = 22

    search_list = Person.search(year_start, year_end)

    for i in search_list:
        print(i)

