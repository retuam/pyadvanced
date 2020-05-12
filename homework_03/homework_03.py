import time
from random import randint


def recursive_some_decorator(quantity=1):

    def my_some_decorator(func):

        def wrapper(*args, **kwargs):

            start_time = time.time()

            for i in range(quantity):
                start_func = time.time()
                res = func(*args, **kwargs)
                end_func = time.time()
                print(f'Function: {func.__name__} with result: {res} end time for execute: {end_func - start_func}')

            end_time = time.time()
            print(f'Functions {func.__name__} executing quantity {quantity} with common time {end_time - start_time}')

            return func(*args, **kwargs)

        return wrapper

    return my_some_decorator


@recursive_some_decorator(quantity=10)
def div(a, b):
    return a / b

@recursive_some_decorator(quantity=10)
def rand():
    return randint(1, 10)

@recursive_some_decorator(quantity=10)
def my_text():
    return 'Street, ' + str(randint(1, 10))

result = div(10, 30)
print(result)

result = rand()
print(result)

result = my_text()
print(result)