# 2) Создать модуль, который будет заполнять базу данных
# случайными валидными значениями (минимум 100 студентов).
from homework_09.models_for_09 import student_group as sg, curator, course, faculty, mark, student
from random import choice


class RandomStudent:

    def __init__(self):
        self.faculty = [
            'Arts',
            'Engineering',
            'Science',
            'Health',
        ]

        self.curator = [
            'Artur Pirozhkov',
            'Philip Kirkorov',
        ]

        self.group = [
            'Group A1',
            'Group A2',
            'Group A3',
        ]

        self.course = [
            'Course 1',
            'Course 2',
            'Course 3',
        ]

        self.first_name = [
            'Donald',
            'Georg',
            'Ivan',
            'Juan',
            'Pablo',
        ]

        self.last_name = [
            'Picasso',
            'Zaecev',
            'Smith',
            'Kravchenko',
            'Green',
        ]

        self.padre_name = [
            'Ivanovich',
            'Pavlovich',
            'Semenovich',
            'Anatolievich',
            'Vladimirovich',
        ]

        self.mark = [
            '1',
            '2',
            '3',
            '4',
            '5',
        ]

    def set_faculty(self):
        for row in self.faculty:
            model = faculty.Faculty(title=row)
            model.create()

    def set_course(self):
        for row in self.course:
            model = course.Course(title=row)
            model.create()

    def set_group(self):
        for row in self.group:
            model = sg.StudentGroup(title=row)
            model.create()

    def set_curator(self):
        for row in self.curator:
            model = curator.Curator(title=row)
            model.create()

    def set_students(self):
        data_faculty = faculty.Faculty().all_id()
        data_group = sg.StudentGroup().all_id()
        data_curator = curator.Curator().all_id()
        i = 0
        while i <= 100:
            faculty_id = choice(data_faculty)
            group_id = choice(data_group)
            curator_id = choice(data_curator)
            first_name = choice(self.first_name)
            last_name = choice(self.last_name)
            padre_name = choice(self.padre_name)
            model = student.Student(first_name=first_name, last_name=last_name, padre_name=padre_name, group_id=group_id,
                                    faculty_id=faculty_id, curator_id=curator_id)
            model.create()
            i += 1

    def set_marks(self):
        data_course = course.Course().all_id()
        data_student = student.Student().all_id()
        i = 0
        while i <= 500:
            course_id = choice(data_course)
            student_id = choice(data_student)
            stud_mark = choice(self.mark)
            model = mark.Mark(course_id=course_id, student_id=student_id, mark=stud_mark)
            model.create()
            i += 1


if __name__ == '__main__':
    instr = RandomStudent()
    instr.set_faculty()
    instr.set_course()
    instr.set_group()
    instr.set_curator()
    instr.set_students()
    instr.set_marks()
    # model = student.Student(id=8828, first_name='Name 33', last_name='Family 44').update()
    # print(model)
    # model = faculty.Faculty(id=1, title='Faculty 10').update()
    # print(model)
    # faculty.Faculty(id=1).one()
    # print(model)
    # flag = faculty.Faculty(id=2).delete()
    # print(flag)
    # data = faculty.Faculty().all()
    # print(data)

