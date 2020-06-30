from flask import Flask, request
import random


app = Flask(__name__)


@app.route('/tg', methods=['GET', 'POST'])
def test():
    print(request)
    return str(random.randint(0, 100))


@app.route('/in', methods=['GET', 'POST'])
def test():
    print(request)
    return str(random.randint(0, 100))


@app.route('/hello')
def hello():
    return 'Hello, World!'


if __name__== '__main__':
    app.run(debug=True)

