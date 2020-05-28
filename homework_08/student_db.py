from homework_08 import homedb as cm

class SudentDb:

    def __init__(self, _conn):
        with cm.DataConn(db) as conn:
            categories = []
            data = stdb.SudentDb(conn)
            for category in data.get_categories():
                categories.append(cat.Category(*category))

        self.conn = _conn
        self.cursor = self.conn.cursor()

    def get_categories(self):
        self.cursor.execute("SELECT * FROM category WHERE 1")
        return self.cursor.fetchall()




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