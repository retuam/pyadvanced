class Automoto:

    def __init__(self, name, price):
        self._tax = 1.1
        self.name = name
        self.price = price


    def __str__(self):
        return self.name


    def get_color(self):
        return self._color


    def set_color(self, color):
        self._color = color


    color = property(get_color, set_color)


    def get_type(self):
        return self.type


    def set_type(self, type):
        self._type = type


    type = property(get_type, set_type)


    def get_volume(self):
        return self.volume


    def set_volume(self, volume):
        self._volume = volume


    volume = property(get_volume, set_volume)


    def get_price(self):
        return self._price


    def set_price(self, price):
        self._price = price


    price = property(get_price, set_price)


    def tax(self):
        return self.price * self._tax


class Cargo(Automoto):


    def __str__(self):
        output = 'Cargo: ' + self.name + '. Price: ' + str(self.price) + '. Tax: ' + str(self.tax())

        return output


    def set_price(self, price):
        self.price = 0.9 * price


    def tax(self):
        return self.price * self._tax * 0.95


class Passanger(Automoto):


    def __str__(self):
        output = 'Passanger: ' + self.name + '. Price: ' + str(self.price) + '. Tax: ' + str(self.tax())

        return output


    def set_price(self, price):
        self.price = 1.1 * price


    def tax(self):
        return self.price * self._tax * 1.05


if __name__ == '__main__':
    auto_1 = Passanger('Toyota', 10000)
    auto_2 = Cargo('BMW', 10000)

    print(auto_1)
    print(auto_2)
