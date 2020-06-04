from homework_10.practice import models
from random import choice


def fill_db():
    author_list = [
        models.Author.objects.create(name='Роберт', surname='Говард'),
        models.Author.objects.create(name='Агата', surname='Кристи'),
        models.Author.objects.create(name='Станислав', surname='Лэм'),
    ]

    tag_list = [
        models.Tag.objects.create(title='Детектив'),
        models.Tag.objects.create(title='Роман'),
        models.Tag.objects.create(title='Фэнтези'),
        models.Tag.objects.create(title='Новелла'),
    ]

    title_list = [
        'Конан варвар из Киммерии',
        'Эркюль Пуаро',
        'Солярис',
    ]

    body_list = [
        'Текст о конане варваре из Киммерии....',
        'Текст о дектективе....',
        'Текст фантастический....',
    ]

    for _ in range(10):
        models.Post.objects.create(author=choice(author_list),
                                   title=choice(title_list),
                                   body=choice(body_list),
                                   tags=[choice(tag_list), choice(tag_list)])


if __name__ == '__main__':
    fill_db()
