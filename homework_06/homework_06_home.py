# 1) Создать консольную программу-парсер, с выводом прогноза погоды. Дать
# возможность пользователю получить прогноз погоды в его локации ( по
# умолчанию) и в выбраной локации, на определенную пользователем дату.
# Можно реализовать, как консольную программу, так и веб страницу.
# Используемые инструменты: requests, beatifulsoup, остальное по желанию.
# На выбор можно спарсить страницу, либо же использовать какой-либо API.
import requests
from bs4 import BeautifulSoup
import datetime


def get_html(url):
    r = requests.get(url)
    r.encoding = 'utf8'
    return r.text


def get_head(html):
    soup = BeautifulSoup(html, 'lxml')
    return soup


if __name__ == '__main__':
    city = str(input('Введите город на русском языке или оставьте поле пустым для '
                     'автоматического определения местоположения: '))
    city = city.lower()
    print(city)

    date_year = input('Введите год (+/- 1 год) или оставьте поле пустым для текущего года: ')
    today_year = datetime.datetime.today().year
    if date_year:
        date_year = int(date_year)
        if not -1 <= (date_year - today_year) <= 1:
            date_year = today_year
    else:
        date_year = today_year

    date_month = input('Введите номер месяца или оставьте поле пустым для текущего месяца: ')
    today_month = datetime.datetime.today().month
    if date_month:
        date_month = int(date_month)
        if not 0 <= date_month <= 12:
            date_month = today_month
    else:
        date_month = today_month

    date_day = input('Введите число или оставьте поле пустым для текущей даты: ')
    today_day = datetime.datetime.today().day
    if date_day:
        date_day = int(date_day)
        if not 1 <= date_month <= 31:
            date_day = today_day
    else:
        date_day = today_day

    try:
        d = datetime.date(date_year, date_month, date_day)
    except ValueError:
        d = datetime.date.today()

    print(d)

    url = 'https://sinoptik.ua/'
    if d == datetime.date.today() and city:
        url = 'https://sinoptik.ua/погода-' + city
    elif d != datetime.date.today() and city:
        url = 'https://sinoptik.ua/погода-' + city + '/' + str(d)

    print(url)

    page = get_html(url)
    soup = get_head(page)

    data = {}
    block = soup.find('div', class_='main loaded')
    data['day'] = block.find('p', class_='day-link').string
    data['date'] = block.find('p', class_='date').string
    data['month'] = block.find('p', class_='month').string
    data['today_temp'] = soup.find('p', class_='today-temp').string
    data['today_time'] = soup.find('p', class_='today-time').string
    data['weather'] = block.find('div', class_='weatherIco').get('title')
    temperature = block.find('div', class_='temperature')
    data['temperature_min'] = temperature.find('div', class_='min').find('span').string
    data['temperature_max'] = temperature.find('div', class_='max').find('span').string
    # data['info'] = soup.find('div', class_='rSide').find('table', class_='weatherDetails')
    for key, value in data.items():
        print(f'{key} is: {value}')

    weather = {
        'time': [],
        'info': {},
    }

    data['info_time'] = soup.find('table', class_='weatherDetails').find('tr', class_='gray time').findAll('td')
    for _html in data['info_time']:
        key = _html.string.replace(' ', '')
        weather['time'].append(key)
        weather['info'][key] = {
            'temperature': '',
            'pressure': '',
            'humidity': '',
            'wind': '',
        }

    i = 0
    data['info_temperature'] = soup.find('table', class_='weatherDetails').find('tr', class_='temperature').findAll('td')
    for _html in data['info_temperature']:
        weather['info'][weather['time'][i]]['temperature'] = _html.string
        i += 1

    i = 0
    data['info_pressure'] = soup.find('table', class_='weatherDetails').findAll('tr', class_='gray')[1].findAll('td')
    for _html in data['info_pressure']:
        weather['info'][weather['time'][i]]['pressure'] = _html.string
        i += 1

    i = 0
    data['info_humidity'] = soup.find('table', class_='weatherDetails').findAll('tr')[6].findAll('td')
    for _html in data['info_humidity']:
        weather['info'][weather['time'][i]]['humidity'] = _html.string
        i += 1

    i = 0
    data['info_wind'] = soup.find('table', class_='weatherDetails').findAll('tr')[7].findAll('td')
    for _html in data['info_wind']:
        weather['info'][weather['time'][i]]['wind'] = _html.find('div').get('data-tooltip')
        i += 1

    for key, value in weather['info'].items():
        print(key)
        [print(f' {k}: {v}') for k, v in value.items()]
