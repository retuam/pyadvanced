# 1) Реализовать REST интернет магазина. Модель товар (,
# доступность),
# Категория (описание, название). При обращении к конкретному товару
# увеличивать кол-во просмотров на 1. Добавить модуль для заполнения
# БД валидными данными. Реализовать подкатегории (доп. Бал). Добавить
# роут, который выводят общую стоимость товаров в магазине
import mongoengine as me
import datetime

me.connect('my_shop')


class Category(me.Document):
    title = me.StringField(min_length=3, max_length=256, required=True)

    def __str__(self):
        return f'{self.id} - {self.name}'


class Subcategory(me.Document):
    category = me.ReferenceField(Category)
    title = me.StringField(min_length=3, max_length=256, required=True)

    def __str__(self):
        return f'{self.id} - {self.title}'


class Product(me.Document):
    category = me.ReferenceField(Category)
    subcategory = me.ReferenceField(Subcategory)
    title = me.StringField(min_length=3, max_length=256, required=True)
    body = me.StringField(min_length=3, max_length=4096, required=True)
    created = me.DateTimeField(default=datetime.datetime.now())
    views = me.IntField(default=0)
    qty = me.IntField(default=0)
    price = me.FloatFieldField(default=0)
    sale = me.BooleanField(default=False)

    def add_view(self):
        self.views += 1
        self.save()

    def get_instock(self):
        if self.qty:
            self.sale = True
        return self.sale

    def __str__(self):
        return f'{self.id} - {self.title}'
