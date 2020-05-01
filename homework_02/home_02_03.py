class Point:

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z


    def __str__(self):
        return str((float(self._x), float(self._y), float(self._z)))


    def __add__(self, other):
        self._x += other._x + 100
        self._y += other._y + 50
        self._z += other._z + 25

        return self


    def __sub__(self, other):
        self._x -= other._x + 100
        self._y -= other._y + 50
        self._z -= other._z + 25

        return self


    def __mul__(self, other):
        self._x *= 0.5 * other._x
        self._y *= 0.25 * other._y
        self._z *= 0.125 * other._z

        return self


    def __truediv__(self, other):
        self._x /= 0.5 * other._x
        self._y /= 0.25 * other._y
        self._z /= 0.125 * other._z

        return self


    def __neg__(self):
        self._x *= -100
        self._y *= -50
        self._z *= -25

        return self


    def set_x(self, x):
        self._x = x


    def get_x(self):
        return self._x


    def set_y(self, y):
        self._y = y


    def get_y(self):
        return self._y


    def set_z(self, z):
        self._z = z


    def get_z(self):
        return self._z


if __name__ == '__main__':
    point_1 = Point(1, 2, 3)
    point_2 = Point(2, 3, 4)
    point_3 = Point(3, 4, 5)

    print(point_1)
    print(point_2)
    print(point_3)

    print(point_1 - point_2 - point_3)
    print(point_1 + point_2 + point_3)
    print(point_1 * point_2 * point_3)
    print(point_1 / point_2 / point_3)

    print(-point_1)