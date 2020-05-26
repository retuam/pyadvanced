class Product:

    def __init__(self, _id=None, title=None, insale=None, instock=None, category_id=None, price=None, qty=None,
                 description=None):
        self._id = _id
        self._title = title
        self._insale = insale
        self._instock = instock
        self._category_id = category_id
        self._price = price
        self._qty = qty
        self._description = description

    def __str__(self):
        return f'{self._id} -> {self._category_id}:{self._title}'

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

    def get_insale(self):
        return self._insale

    def set_insale(self, value):
        self._insale = value

    insale = property(get_insale, set_insale)

    def get_instock(self):
        return self._instock

    def set_instock(self, value):
        self._instock = value

    instock = property(get_instock, set_instock)

    def get_category_id(self):
        return self._category_id

    def set_category_id(self, value):
        self._category_id = value

    category_id = property(get_category_id, set_category_id)

    def get_price(self):
        return self._price

    def set_price(self, value):
        self._price = value

    price = property(get_price, set_price)

    def get_qty(self):
        return self._qty

    def set_qty(self, value):
        self._qty = value

    qty = property(get_qty, set_qty)

    def get_description(self):
        return self._description

    def set_description(self, value):
        self._description = value

    description = property(get_description, set_description)