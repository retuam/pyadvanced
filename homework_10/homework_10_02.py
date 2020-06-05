# 1) Реализовать REST интернет магазина. Модель товар (цена,
# доступность, кол-во доступных единиц, категория, кол-во просмотров),
# Категория (описание, название). При обращении к конкретному товару
# увеличивать кол-во просмотров на 1. Добавить модуль для заполнения
# БД валидными данными. Реализовать подкатегории (доп. Бал). Добавить
# роут, который выводят общую стоимость товаров в магазине
from flask import Flask, request, jsonify
from flask_restful import Api
from homework_10.home.resources import *


app = Flask(__name__)
api = Api(app)

api.add_resource(
    TotalResource,
    '/',
)

api.add_resource(
    ProductResource,
    '/product',
    '/product/category/<category_id>',
    '/product/subcategory/<subcategory_id>',
    '/product/<id>'
)

api.add_resource(
    CategoryResource,
    '/category',
    '/category/<id>'
)

api.add_resource(
    SubcategoryResource,
    '/subcategory',
    '/subcategory/<id>'
)

if __name__ == '__main__':
    app.run(debug=True)
