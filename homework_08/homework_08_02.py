# 2) Создать страницу для администратора, через которую он может добавлять
# новые товары и категории.
from flask import Flask, request
from flask import render_template
from homework_08 import homework_08_01 as front
from homework_08 import product as prod
from homework_08 import category as cat


app = Flask(__name__)


front.menu += [
    {'url': '/add/category', 'title': 'Add category'},
    {'url': '/add/product', 'title': 'Add product'},
]


@app.route('/')
def list_category():
    return front.list_category()


@app.route('/category/<int:_id>')
def single_category(_id):
    return front.single_category(_id)


@app.route('/product/<int:_id>')
def single_product(_id):
    return front.single_product(_id)


@app.route('/add/category', methods=["GET", "POST"])
def add_category():
    cat.CategorySearch(front.db).insert(request.form)
    return render_template('add_category.html', menu=front.menu)


@app.route('/add/product', methods=["GET", "POST"])
def add_product():
    prod.ProductSearch(front.db).insert(request.form)
    categories = cat.CategorySearch(front.db).get_categories()
    return render_template('add_product.html', categories=categories, menu=front.menu)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
