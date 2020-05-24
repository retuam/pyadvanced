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
