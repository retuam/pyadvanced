# Написать REST для блога (использовать валидацию). Реализовать
# модель Пост (название, содержание, дата публикации, автор, кол-во
# просмотров, тег). Реализовать модель тег. Реализовать модель автор (имя,
# фамилия, кол-во публикаций автора). Добавить валидацию ко всем полям.
# Реализовать модуль заполнения всех полей БД валидными (адеквадными
# данными :) ). Добавить вывод всех постов по тегу, при каждом обращении к
# конкретному посту увеличивать кол-во просмотров на 1. При обращении к
# автору, выводить все его публикации.
from flask import Flask, request, jsonify
from flask_restful import Api
from homework_10.resources import *


app = Flask(__name__)
api = Api(app)


api.add_resource(
    AuthorResource,
    '/author',
    '/author/<id>'
)

api.add_resource(
    TagResource,
    '/tag',
    '/tag/<id>'
)

api.add_resource(
    PostResource,
    '/post',
    '/post/<id>'
)

if __name__ == '__main__':
    app.run(debug=True)
