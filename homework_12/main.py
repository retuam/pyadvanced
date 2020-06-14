# Создать бот для поиска статей на википедии.
# При входе, бот запрашивает пользователя ввести имя статьи. Далее бот осуществляет этот поиск на википедии,
# в случае отстутвия выводит соотвествующие сообщение, а если статья найдена выводит на экран текст.
from telebot import TeleBot
import requests
from bs4 import BeautifulSoup, Comment
import math


bot = TeleBot("1116314719:AAGmn_YjFsl0k8acvd1FBL2f_E_HNe6Cdds")


def get_head(html):
    soup = BeautifulSoup(html, 'lxml')
    return soup


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Введите название статьи')


@bot.message_handler(content_types=['text'])
def any_text(message):
    url = f'https://www.wikipedia.org/search-redirect.php?family=wikipedia&language=en&search={message.text}&language=ru&go=Go'
    r = requests.get(url)
    r.encoding = 'utf8'
    soup = get_head(r.text)
    comments = soup.findAll(text=lambda text: isinstance(text, Comment))
    [comment.extract() for comment in comments]

    exist = soup.find('p', class_='mw-search-nonefound')
    if exist:
        bot.send_message(message.chat.id, 'В Википедии нет статьи с таким названием.')
    else:
        block = soup.find('link', rel='canonical').get('href')
        bot.send_message(message.chat.id, block)
        fragment = soup.find('div', id='mw-content-text')
        all_text = ''.join(fragment.findAll(text=True))
        qty = math.ceil(len(all_text) / 4096)
        for i in range(0, qty):
            min = i * 4096
            max = (i + 1) * 4096
            bot.send_message(message.chat.id, all_text[min:max])


if __name__ == '__main__':
    bot.polling()
