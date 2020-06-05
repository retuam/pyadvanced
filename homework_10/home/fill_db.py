from homework_10.home import models
from random import uniform, choice


def fill_db():
    category_list = [
        models.Category.objects.create(title='Техника'),
        models.Category.objects.create(title='Продукты питания'),
        models.Category.objects.create(title='Книги'),
    ]

    subcategory_list = [
        models.Subcategory.objects.create(title='Овощи', category=category_list[1]),
        models.Subcategory.objects.create(title='Фрукты', category=category_list[1]),
        models.Subcategory.objects.create(title='Компьютеры', category=category_list[0]),
        models.Subcategory.objects.create(title='Бытовая', category=category_list[0]),
        models.Subcategory.objects.create(title='Романы', category=category_list[2]),
        models.Subcategory.objects.create(title='Детективы', category=category_list[2]),
    ]

    product_list = {
        0: {
            'Помидоры': 'Красные и спелые',
            'Огурцы': 'Зеленые огурцы из Турции',
            'Лук': 'Крымский синий лук',
        },
        1: {
            'Лимон': 'Спелый, сочный, тонкошкурый',
            'Апельсин': 'Испанский Naranja',
            'Лайм': 'Идеальный для текилы',
        },
        2: {
            'Ноутбук ASUS': '15 дюймов, AMD, GeForce',
            'MacBook Air': 'Идеальный ноубтук для работы',
            'Видеокарта NVIDEO': 'Для тех кто знает толк в Bitcoin',
        },
        3: {
            'Стиральная машина Samsung': 'Стирает как зверь',
            'Эл.чайник Vitek': 'Самый простой и надежный чайник',
            'Холодильник Урал': 'О котором пела група Чайф',
        },
        4: {
            'Война и мир': 'Лев Николаевич Толстой. 4-томник',
            'Поднятая целина': 'Михаил Александрович Шолохов. Дед Щукарь и другие',
            'Моби Дик': 'Или как моряки за китовым жиром ходили',
        },
        5: {
            'Записки о Шерлоке Холмсе': 'Собака Баскервилей',
            'Лейтенант Коломбо': 'Одноглазый Питер Фальк',
            'Турецкий гамбит': 'О русско-турецкой войне, предательстве и любви',
        },
    }

    for key, value in product_list.items():
        for k, v in value.items():
            models.Product.objects.create(subcategory=subcategory_list[key],
                                          title=k,
                                          body=v,
                                          price=uniform(10, 100),
                                          sale=choice(True, True, False))


if __name__ == '__main__':
    fill_db()
