# 2) Создать страницу для администратора, через которую он может добавлять
# новые товары и категории.
from flask import Flask, request
from flask import render_template
from homework_08 import product as prod
from homework_08 import category as cat


db = 'shop.db'
app = Flask(__name__)


menu = [
    {'url': '/', 'title': 'Home'},
    {'url': '/add/category', 'title': 'Add category'},
    {'url': '/add/product', 'title': 'Add product'},
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


@app.route('/add/category', methods=["GET", "POST"])
def add_category():
    cat.CategorySearch(db).insert(request.form)
    return render_template('add_category.html', menu=menu)


@app.route('/add/product', methods=["GET", "POST"])
def add_product():
    prod.ProductSearch(db).insert(request.form)
    categories = cat.CategorySearch(db).get_categories()
    return render_template('add_product.html', categories=categories, menu=menu)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
