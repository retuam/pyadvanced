# Написать бота-консультанта, который будет собирать информацию с
# пользователя (его ФИО, номер телефона, почта, адрес, пожелания).
# Записывать сформированную заявку в БД (по желанию SQl/NOSQL).
from telebot import TeleBot
from homework_11.application.models import User
from homework_11.application.schemas import UserSchema
from marshmallow import ValidationError


bot = TeleBot("1116314719:AAGmn_YjFsl0k8acvd1FBL2f_E_HNe6Cdds")

answers = {
    1: ['Ваше имя', 'А какая Ваша фамилия?'],
    2: ['Ваша фамилия', 'А какое Ваше отчество?'],
    3: ['Ваше отчество', 'Скажите пожалуйста свой номер телефона?'],
    4: ['Ваш телефон', 'Укажите свой email'],
    5: ['Ваш email', 'Укажите свой адрес'],
    6: ['Ваш адрес', 'Есть ли у Вас пожелания?'],
    7: ['Ваше пожелание', 'Спасибо'],
    8: ['Информация', 'собрана. Достаточно.']
}


def validbot(name, message):
    try:
        UserSchema(only=[name]).load({name: message.text})
        result = True
    except ValidationError as err:
        bot.send_message(message.chat.id, f'{err.messages}')
        result = False
    return result


@bot.message_handler(commands=['start'])
def hello(message):
    user = User.objects(chat_id=message.chat.id).first()
    if user:
        bot.send_message(message.chat.id, '''Здравствуйте, я Бот-консультант, предыдущие данные о Вас очищены. 
        Как Ваше имя?''')
        User.objects(chat_id=message.chat.id).delete()
    else:
        bot.send_message(message.chat.id, 'Здравствуйте, я Бот-консультант, а как Ваше имя?')


@bot.message_handler(content_types=['text'])
def any_text(message):
    user = User.objects(chat_id=message.chat.id).first()
    result = True
    status_ = 1
    if not user:
        result = validbot('first_name', message)
        user = User(chat_id=message.chat.id, first_name=message.text, status=status_)
    else:
        status_ = user.status + 1
        if status_ == 2:
            result = validbot('last_name', message)
            user.last_name = message.text
        elif status_ == 3:
            result = validbot('parent_name', message)
            user.parent_name = message.text
        elif status_ == 4:
            result = validbot('telephone', message)
            user.telephone = message.text
        elif status_ == 5:
            result = validbot('email', message)
            user.email = message.text
        elif status_ == 6:
            result = validbot('address', message)
            user.address = message.text
        elif status_ == 7:
            result = validbot('comment', message)
            user.comment = message.text
        else:
            message.text = user.first_name
            status_ = 8

        if result:
            user.status = status_

    if result:
        user.save()
        bot.send_message(message.chat.id, f'{answers[status_][0]} {message.text} {answers[status_][1]}')
    else:
        bot.send_message(message.chat.id, f'Введите еще раз')


bot.polling()
