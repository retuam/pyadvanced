# 1) Создать базу данных товаров, у товара есть: Категория (связанная
# таблица), название, есть ли товар в продаже или на складе, цена, кол-во
# единиц.Создать html страницу. На первой странице выводить ссылки на все
# категории, при переходе на категорию получать список всех товаров в
# наличии ссылками, при клике на товар выводить его цену, полное описание и
# кол-во единиц в наличии.
from flask import Flask
from flask import render_template
from homework_08 import homedb as cm
from homework_08 import product as prod
from homework_08 import category as cat


db = 'shop.db'

app = Flask(__name__)


menu = [
    {'url': '/', 'title': 'Home'},
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


if __name__ == '__main__':
    app.run(debug=True, port=8000)
