class Complex:

    def __init__(self, real, imag):
        self._real = real
        self._imag = imag

    def __str__(self):
        if self._imag > 0:
            _str = f'{self._real}+{self._imag}i'
        elif self._imag < 0:
            _str = f'{self._real}{self._imag}i'
        else:
            _str = f'{self._real}'

        return _str

    def __add__(self, other):
        return Complex(self._real + other._real, self._imag + other._imag)

    def __sub__(self, other):
        return Complex(self._real - other._real, self._imag - other._imag)

    def __mul__(self, other):
        return Complex(self._real * other._real - self._imag * other._imag, self._real * other._imag + self._imag * other._real)

    def __truediv__(self, other):
        return Complex((self._real * other._real + self._imag * other._imag) / (other._real ** 2 + other._imag ** 2),
                       (other._real * self._imag - self._real * other._imag) / (other._real ** 2 + other._imag ** 2))

    def __neg__(self):
        return Complex(-self._real, -self._imag)


if __name__ == '__main__':
    num_1 = Complex(1, 2)
    num_2 = Complex(2, 3)

    print(num_1)
    print(num_2)

    print(num_1 + num_2)
    print(num_1 - num_2)
    print(num_1 * num_2)
    print(num_1 / num_2)
    print(-num_2)