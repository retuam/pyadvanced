from homework_09.models_for_09 import activerecord as ar


class Faculty(ar.ActiveRecord):
    def __init__(self, id=None, title=None):
        super().__init__(id, title, 'faculty')
