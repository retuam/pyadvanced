# 2) Создать свою структуру данных Словарь, которая поддерживает методы,
# get, items, keys, values. Так же перегрузить операцию сложения для
# словарей, которая возвращает новый расширенный объект.


class MyDict:

    def __init__(self, **kwargs):
        self._current = 0
        self._structure = {}
        for key in kwargs:
            self[key] = kwargs[key]
        self._len = len(kwargs)

    def __iter__(self):
        self._current = 0
        return self

    def __next__(self):
        if self._current == self._len:
            raise StopIteration
        current = self._current
        self._current += 1
        return self.keys()[current]

    def items(self):
        _items = [0] * self._len
        i = 0
        for key in self._structure:
            _items[i] = (key, self._structure[key])
            i += 1
        return _items

    def keys(self):
        _keys = [0] * self._len
        i = 0
        for key in self._structure:
            _keys[i] = key
            i += 1
        return _keys

    def values(self):
        _values = [0] * self._len
        i = 0
        for key in self._structure:
            _values[i] = self._structure[key]
            i += 1
        return _values

    def get_structure(self):
        return self._structure

    def __str__(self):
        return f'MyDict = {self._structure}'

    def __add__(self, other):
        new_obj = MyDict()
        for key, value in self.items():
            new_obj[key] = value
        for key, value in other.items():
            new_obj[key] = value
        return new_obj

    def __getitem__(self, item):
        return item, self._structure[item]

    def __setitem__(self, key, value):
        self._structure[key] = value

    def get(self, key):
        try:
            return self._structure[key]
        except KeyError:
            return None

    def pop(self, key):
        del self._structure[key]
        self._len -= 1

    def clear(self):
        self._structure = {}
        self._len = 0


if __name__ == '__main__':
    obj = MyDict(v1=10, v3=20, v5=30, v7=40)
    print(obj['v1'])
    print(obj['v5'])
    print(obj)
    for row in obj:
        print(row)
    print(obj.values())
    print(obj.keys())
    print(obj.items())
    print(obj.get('v'))
    print(obj.get('v1'))
    obj.pop('v5')
    print(obj)
    obj.clear()
    print(obj)

    obj1 = MyDict(v1=10, v3=20, v5=30, v7=40)
    obj2 = MyDict(v1=11, v2=10, v4=20, v6=30, v9=40)
    obj3 = obj1 + obj2
    print(obj3)
