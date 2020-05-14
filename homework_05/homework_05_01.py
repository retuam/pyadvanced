import time
from threading import Thread


def thread_decorator(my_name, my_dmn=True):

    def _thread_decorator(func):

        def wrapper(*args, **kwargs):
            t = Thread(target=func, args=args, kwargs=kwargs, daemon=my_dmn, name=my_name)
            t.start()

        return wrapper

    return _thread_decorator


@thread_decorator('thread 1', False)
def div(a, b):
    time.sleep(5)
    print(f'My function')
    return a / b


if __name__ == '__main__':
    print('Start')
    result = div(11, 12)
    print('Finish')
    print(result)