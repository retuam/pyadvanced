# 1) Создать базу данных студентов (ФИО, группа, оценки, куратор
# студента, факультет). Написать CRUD ко всем полям. Описать
# методы для вывода отличников по каждому факультету. Вывести
# всех студентов определенного куратора.
from flask import Flask, request, jsonify
from homework_09.models_for_09 import student_group as sg, curator, course, faculty, mark, student


app = Flask(__name__)

@app.route('/', methods=['GET'])
def all_students():
    data = student.Student().all_format()
    return jsonify(data)


@app.route('/graduated', methods=['GET'])
def graduated():
    data = student.Student().graduated()
    return jsonify(data)


@app.route('/for-curator/<int:id>', methods=['GET'])
def student_curators(id):
    data = student.Student().curators(id)
    return jsonify(data)


@app.route('/student', methods=['GET', 'POST'])
@app.route('/student/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def api_student(id=None):
    if request.method == 'GET':
        data = student.Student().all()
        if id:
            data = student.Student(id=id).one()
        return jsonify(data)

    elif request.method == 'POST':
        data = student.Student(**request.json).create()
        return jsonify(data)

    elif request.method == 'PUT':
        data = student.Student(**request.json).update()
        return jsonify(data)

    elif request.method == 'DELETE':
        data = student.Student(id=id).delete()
        return jsonify(data)


@app.route('/mark', methods=['GET', 'POST'])
@app.route('/mark/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def api_mark(id=None):
    if request.method == 'GET':
        data = mark.Mark().all()
        if id:
            data = mark.Mark(id=id).one()
        return jsonify(data)

    elif request.method == 'POST':
        data = mark.Mark(**request.json).create()
        return jsonify(data)

    elif request.method == 'PUT':
        data = mark.Mark(**request.json).update()
        return jsonify(data)

    elif request.method == 'DELETE':
        data = mark.Mark(id=id).delete()
        return jsonify(data)


@app.route('/faculty', methods=['GET', 'POST'])
@app.route('/faculty/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def api_faculty(id=None):
    if request.method == 'GET':
        data = faculty.Faculty().all()
        if id:
            data = faculty.Faculty(id=id).one()
        return jsonify(data)

    elif request.method == 'POST':
        data = faculty.Faculty(**request.json).create()
        return jsonify(data)

    elif request.method == 'PUT':
        data = faculty.Faculty(**request.json).update()
        return jsonify(data)

    elif request.method == 'DELETE':
        data = faculty.Faculty(id=id).delete()
        return jsonify(data)


@app.route('/curator', methods=['GET', 'POST'])
@app.route('/curator/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def api_curator(id=None):
    if request.method == 'GET':
        data = curator.Curator().all()
        if id:
            data = curator.Curator(id=id).one()
        return jsonify(data)

    elif request.method == 'POST':
        data = curator.Curator(**request.json).create()
        return jsonify(data)

    elif request.method == 'PUT':
        data = curator.Curator(**request.json).create()
        return jsonify(data)

    elif request.method == 'DELETE':
        data = curator.Curator(id=id).delete()
        return jsonify(data)


@app.route('/course', methods=['GET', 'POST'])
@app.route('/course/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def api_course(id=None):
    if request.method == 'GET':
        data = course.Course().all()
        if id:
            data = course.Course(id=id).one()
        return jsonify(data)

    elif request.method == 'POST':
        data = course.Course(**request.json).create()
        return jsonify(data)

    elif request.method == 'PUT':
        data = course.Course(**request.json).create()
        return jsonify(data)

    elif request.method == 'DELETE':
        data = course.Course(id=id).delete()
        return jsonify(data)


@app.route('/student-group', methods=['GET', 'POST'])
@app.route('/student-group/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def api_group(id=None):
    if request.method == 'GET':
        data = sg.StudentGroup().all()
        if id:
            data = sg.StudentGroup(id=id).one()
        return jsonify(data)

    elif request.method == 'POST':
        data = sg.StudentGroup(**request.json).create()
        return jsonify(data)

    elif request.method == 'PUT':
        data = sg.StudentGroup(**request.json).create()
        return jsonify(data)

    elif request.method == 'DELETE':
        data = sg.StudentGroup(id=id).delete()
        return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
