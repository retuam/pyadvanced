# 1) Создать свою структуру данных Список, которая поддерживает
# индексацию. Методы pop, append, insert, remove, clear. Перегрузить
# операцию сложения для списков, которая возвращает новый расширенный
# объект.


class MyList:

    def __init__(self, *args):
        self._current = 0
        self._len = 0
        for _ in args:
            self._len += 1
        self._structure = [0] * self._len
        for value in enumerate(args):
            self[value[0]] = value[1]

    def __str__(self):
        return f'MyList = {self._structure}'

    def __iter__(self):
        self._current = 0
        return self

    def __next__(self):
        if self._current == self._len:
            raise StopIteration
        current = self._current
        self._current += 1
        return self[current]

    def __getitem__(self, item):
        return self._structure[item]

    def __setitem__(self, key, value):
        self._structure[key] = value

    def __add__(self, other):
        _structure = self._structure + other.get_structure()
        return MyList(*_structure)

    def get_structure(self):
        return self._structure

    def pop(self, key=None):
        if key is None:
            del self._structure[self._len - 1]
        else:
            del self._structure[key]
        self._len -= 1

    def append(self, value):
        self._len += 1
        self[self._len] = value

    def insert(self, key, value):
        self._structure = self._structure[:key] + [value] + self._structure[key:]

    def remove(self, value):
        i = 0
        while i < self._len:
            if value == self._structure[i]:
                del self._structure[i]
                break
            i += 1
        if i == self._len:
            raise ValueError("ValueError exception thrown")
        else:
            self._len -= 1

    def clear(self):
        self._structure = []
        self._len = 0


if __name__ == '__main__':
    obj = MyList(0, 10, 20, 30, 40)
    print(obj[0])
    print(obj[4])
    print(obj)
    obj.insert(2, 70)
    print(obj)
    obj.pop(2)
    print(obj)
    obj.remove(30)
    print(obj)
    obj.clear()
    print(obj)

    obj1 = MyList(0, 11, 21, 31, 41)
    obj2 = MyList(0, 12, 22, 32, 42)
    obj3 = obj1 + obj2
    print(obj3)



