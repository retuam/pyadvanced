class Shop:

    count = 0

    def __init__(self, name, sale):
        self.sale = sale
        self.name = name
        Shop.count += sale


    def __str__(self):
        output = self.name + ' - ' + str(self.sale) + '. All shops - ' + str(self.count)
        return output


    def add_sale(self, sale):
        self.sale += sale
        Shop.count += self.sale


if __name__ == '__main__':
    shop_1 = Shop('Silpo', 10)
    print(shop_1)

    shop_2 = Shop('ATB', 20)
    print(shop_2)

    shop_3 = Shop('Novus', 30)
    print(shop_3)

    shop_2.add_sale(44)
    print(shop_2)