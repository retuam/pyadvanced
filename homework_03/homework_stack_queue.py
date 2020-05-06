class Queue:


    def __init__(self, elements):
        self._elements = []

        for i in list(elements):
            self._elements.append(i)


    def add(self, element):
        self._elements.append(element)

        return self._elements


    def remove(self):
        _element = self._elements[:1][0]
        self._elements = self._elements[1:]
        return _element


    def get_data(self):
        return self._elements


    def __str__(self):
        return str(self._elements)


class Stack(Queue):

    def remove(self):
        return self._elements.pop()


if __name__ == '__main__':
    print('Queue')
    queue = Queue((1, 2, 3))
    print(queue)
    new = queue.add(6)
    print(new)
    queue.add(7)
    print(queue)
    remove = queue.remove()
    print(remove)
    print(queue)

    print('Stack')
    stack = Stack((1, 2, 3))
    print(stack)
    new = stack.add(6)
    print(new)
    stack.add(7)
    print(stack)
    remove = stack.remove()
    print(remove)
    print(stack)