import requests
from threading import Thread


class MyThread(Thread):

    def __init__(self, target, args, kwargs):
        super().__init__()
        self.target = target
        self.args = args
        self.kwargs = kwargs

    def run(self):
        print(f"Tread name: {self.name} started")

        self.target(*self.args, **self.kwargs)


def thread_decorator(my_name, my_dmn=True):

    def _thread_decorator(func):

        def wrapper(*args, **kwargs):
            t = MyThread(target=func, args=args, kwargs=kwargs)
            t.setName(my_name)
            t.setDaemon(my_dmn)
            t.start()

            # return t

        return wrapper

    return _thread_decorator


def my_download(url, name):
    print(f'start {url}')
    p = requests.get(url)
    filename = f"{name}.{url.split('.')[-1]}"
    with open(filename, 'wb') as fd:
        fd.write(p.content)
        print(f'finish thread name: {name}')


if __name__ == '__main__':
    thread_list = {}
    _lists = [
        'https://pm1.narvii.com/6874/3fab7145be3e10c68cbd8670afc995fbf4c5b41br1-640-494v2_hq.jpg',
        'https://pbs.twimg.com/media/EO1Lj_1WoAEQF7n.jpg',
        'https://techrocks.ru/wp-content/uploads/2019/03/1.jpg',
        'https://bugaga.ru/uploads/posts/2017-09/1504559516_kartinki-13.jpg',
        'https://bugaga.ru/uploads/posts/2018-07/1532174767_prikol-6.jpg',
        'https://pm1.narvii.com/6830/55ead55ed7a06888ce4500119fe4f6652f0205fcv2_00.jpg',
        'https://s.0512.com.ua/section/newsInternalIcon/upload/images/news/icon/000/051/898/dizajn-bez-nazvania-18_5e72322a43ac4.jpg',
        'https://ukranews.com/upload/img/2020/03/18/5e727637a6ac4-----------18.jpg',
        'https://animehub.cc/wp-content/uploads/2020/02/anime-meme-2020-jogurt-brateka.jpg',
        'https://sib.fm/storage/article/January2020/%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F%20(3)1.jpg'
    ]
    print('Start')
    for name, url in enumerate(_lists):
        thread_list[url] = thread_decorator(name, False)(my_download)(url, name)

    print('Finish')