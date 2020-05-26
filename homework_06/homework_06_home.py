# 1) Создать консольную программу-парсер, с выводом прогноза погоды. Дать
# возможность пользователю получить прогноз погоды в его локации ( по
# умолчанию) и в выбраной локации, на определенную пользователем дату.
# Можно реализовать, как консольную программу, так и веб страницу.
# Используемые инструменты: requests, beatifulsoup, остальное по желанию.
# На выбор можно спарсить страницу, либо же использовать какой-либо API.
import requests
from bs4 import BeautifulSoup
import datetime


def get_head(html):
    soup = BeautifulSoup(html, 'lxml')
    return soup


class SelectDay:

    def __init__(self):
        self.data = datetime.datetime.today()
        self.year = self.data.year
        self.month = self.data.month
        self.day = self.data.day

    def __year(self):
        try:
            _year = int(input('Введите год (+/- 1 год) или оставьте поле пустым для текущего года: '))
            if _year and -1 <= (_year - self.year) <= 1:
                self.year = _year
        except ValueError:
            print('Установлен текущий год')

    def __month(self):
        try:
            _month = int(input('Введите номер месяца или оставьте поле пустым для текущего месяца: '))
            if _month and 0 <= _month <= 12:
                self.month = _month
        except ValueError:
            print('Установлен текущий месяц')

    def __day(self):
        try:
            _day = int(input('Введите число или оставьте поле пустым для текущей даты: '))
            if _day and 1 <= _day <= 31:
                self.day = _day
        except ValueError:
            print('Установлен текущий день')

    def set_data(self):
        self.__year()
        self.__month()
        self.__day()
        try:
            self.data = datetime.date(self.year, self.month, self.day)
        except ValueError:
            self.data = datetime.date.today()


class Parser(SelectDay):

    def __init__(self):
        super().__init__()
        self.city = self.input_city()
        self.set_data()
        self.url = 'https://sinoptik.ua/'
        self.info = {}
        self.time = []
        if self.data and self.city:
            self.url += 'погода-' + self.city + '/' + str(self.data)
        print(self.url)

    def __str__(self):
        _output = ''
        for key, value in parser.output.items():
            _output += f'{key} is: {value}\n'

        for key, value in parser.get_info().items():
            _output += key
            for k, v in value.items():
                _output += f' {k}: {v}\n'

        return _output

    @staticmethod
    def input_city():
        return str(input('Введите город на русском языке или оставьте поле пустым для '
                         'автоматического определения местоположения: ')).lower()

    def get_html(self):
        r = requests.get(self.url)
        r.encoding = 'utf8'
        return r.text

    def set_info_item(self, key):
        self.info[key] = {
            'temperature': '',
            'pressure': '',
            'humidity': '',
            'wind': '',
        }

    def set_time_item(self, k):
        self.time.append(k)

    def get_string(self, _list, k):
        for _html in enumerate(_list):
            self.info[self.time[_html[0]]][k] = _html[1].string

    def get_tooltip(self, _list, k):
        for _html in enumerate(_list):
            self.info[self.time[_html[0]]][k] = _html[1].find('div').get('data-tooltip')

    def get_info(self):
        return self.info

    def get_output(self):
        return self._output

    def set_output(self, value):
        self._output = value

    output = property(get_output, set_output)


if __name__ == '__main__':
    parser = Parser()

    page = parser.get_html()
    soup = get_head(page)
    block = soup.find('div', class_='main loaded')
    temperature = block.find('div', class_='temperature')
    block_weather = soup.find('table', class_='weatherDetails')

    parser.output = {
        'day': block.find('p', class_='day-link').string,
        'date': block.find('p', class_='date').string,
        'month': block.find('p', class_='month').string,
        'weather': block.find('div', class_='weatherIco').get('title'),
        'min': temperature.find('div', class_='min').find('span').string,
        'max': temperature.find('div', class_='max').find('span').string,
    }

    for row in block_weather.find('tr', class_='gray time').findAll('td'):
        key = row.string.replace(' ', '')
        parser.set_time_item(key)
        parser.set_info_item(key)

    parser.get_string(block_weather.find('tr', class_='temperature').findAll('td'), 'temperature')
    parser.get_string(block_weather.findAll('tr', class_='gray')[1].findAll('td'), 'pressure')
    parser.get_string(block_weather.findAll('tr')[6].findAll('td'), 'humidity')
    parser.get_tooltip(block_weather.findAll('tr')[7].findAll('td'), 'wind')

    print(parser)
