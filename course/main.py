from course.webshop.bot.main import bot
from flask import Flask, request, abort
from telebot.types import Update
from course.webshop.bot.config import WEBHOOK_PATH, WEBHOOK_URL


app = Flask(__name__)


@app.route(WEBHOOK_PATH, methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        abort(403)


if __name__ == '__main__':
    bot.set_webhook(
        WEBHOOK_URL,
        certificate=open('webhook_cert.pem', 'r')
    )
    app.run(debug=True)
