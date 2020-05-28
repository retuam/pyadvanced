# 1) Создать базу данных товаров, у товара есть: Категория (связанная
# таблица), название, есть ли товар в продаже или на складе, цена, кол-во
# единиц.Создать html страницу. На первой странице выводить ссылки на все
# категории, при переходе на категорию получать список всех товаров в
# наличии ссылками, при клике на товар выводить его цену, полное описание и
# кол-во единиц в наличии.
from flask import Flask
from flask import render_template
from homework_08 import product as prod
from homework_08 import category as cat


db = 'shop.db'

app = Flask(__name__)


menu = [
    {'url': '/', 'title': 'Home'},
]


@app.route('/')
def list_category():
    categories = cat.CategorySearch(db).get_categories()
    return render_template('index.html', categories=categories, menu=menu)


@app.route('/category/<int:_id>')
def single_category(_id):
    category = cat.CategorySearch(db).get_category(_id)
    products = prod.ProductSearch(db).get_products(_id)
    return render_template('category.html', category=category, products=products, menu=menu)


@app.route('/product/<int:_id>')
def single_product(_id):
    product = prod.ProductSearch(db).get_product(_id)
    return render_template('product.html', product=product, menu=menu)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
