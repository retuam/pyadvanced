from homework_09.models_for_09 import activerecord as ar


class Curator(ar.ActiveRecord):
    def __init__(self, id=None, title=None):
        super().__init__(id, title)
        self._table = 'curator'
