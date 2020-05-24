# 2) Создать страницу для администратора, через которую он может добавлять
# новые товары и категории.
from flask import Flask, request
from flask import render_template
from homework_08 import homedb as cm
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
    categories = []
    with cm.DataConn(db) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM category WHERE 1")
        for category in cursor.fetchall():
            categories.append(cat.Category(*category))

    return render_template('index.html', categories=categories, menu=menu)


@app.route('/category/<int:_id>')
def single_category(_id):
    products = []
    with cm.DataConn(db) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM category WHERE id = ?", (_id, ))
        category = cat.Category(*cursor.fetchone())
        cursor.execute("SELECT * FROM product WHERE category_id = ?", (_id, ))
        for product in cursor.fetchall():
            products.append(prod.Product(*product))

    return render_template('category.html', category=category, products=products, menu=menu)


@app.route('/product/<int:_id>')
def single_product(_id):
    with cm.DataConn(db) as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT product.id AS id, product.title AS title, product.insale AS insale, 
            product.instock AS instock, category.title AS category_id, product.price AS price, product.qty AS qty,
            product.description AS description FROM product 
           LEFT JOIN category ON category.id = product.category_id WHERE product.id = ?""", (_id, ))

        _product = cursor.fetchone()
        print(_product)
        product = prod.Product(*_product)

    return render_template('product.html', product=product, menu=menu)


@app.route('/add/category', methods=["GET", "POST"])
def add_category():
    with cm.DataConn(db) as conn:
        category = cat.Category()
        cursor = conn.cursor()
        _post = dict(request.form)
        if _post:
            category.title = _post['title']
            cursor.execute("INSERT INTO category (title) VALUES (?)", (category.title, ))
            conn.commit()

    return render_template('add_category.html', menu=menu)


@app.route('/add/product', methods=["GET", "POST"])
def add_product():
    categories = []
    with cm.DataConn(db) as conn:
        product = prod.Product()
        cursor = conn.cursor()
        _post = dict(request.form)
        if _post:
            product.title = _post['title']
            product.insale = _post['insale']
            product.instock = _post['instock']
            product.price = _post['price']
            product.qty = _post['qty']
            product.category_id = _post['category_id']
            product.description = _post['description']
            cursor.execute("""INSERT INTO product (title, insale, instock, price, qty, category_id, description) 
            VALUES (?, ?, ?, ?, ?, ?, ?)""", (product.title, product.insale, product.instock, product.price,
                                              product.qty, product.category_id, product.description))
            conn.commit()

        cursor.execute("SELECT * FROM category WHERE 1")
        for category in cursor.fetchall():
            categories.append(cat.Category(*category))

    return render_template('add_product.html', categories=categories, menu=menu)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
