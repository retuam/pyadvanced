from homework_08 import homedb as cm


class Category:

    def __init__(self, _id=None, title=None):
        self._id = _id
        self._title = title

    def __str__(self):
        return f'{self._id} -> {self._title}'

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


class CategorySearch:

    def __init__(self, db):
        self.categories = []
        self.category = None
        self.db = db

    def get_categories(self):
        with cm.DataConn(self.db) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM category WHERE 1")
            for category in cursor.fetchall():
                self.categories.append(Category(*category))

        return self.categories

    def get_category(self, _id):
        with cm.DataConn(self.db) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM category WHERE id = ?", (_id, ))
            self.category = Category(*cursor.fetchone())

        return self.category

    def insert(self, _post):
        if _post:
            category = Category(**dict(_post))
            print(category)
            with cm.DataConn(self.db) as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO category (title) VALUES (?)", (category.title, ))
                conn.commit()
