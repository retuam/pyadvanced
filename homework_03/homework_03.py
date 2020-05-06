import time

def recursive_some_decorator(quantity=1):

    start_time = time.time()

    def my_some_decorator(func):

        def wrapper(*args, **kwargs):
            _log_time = []

            for i in range(quantity):
                start_time_func = time.time()
                func(*args, **kwargs)
                _log_time.append(time.time() - start_time_func)

                _time = time.time() - start_time

            return func.__name__, _time, _log_time

        return wrapper

    return my_some_decorator


@recursive_some_decorator(quantity=10)
def div(a, b):
    return a / b

result = div(1, 3)
print(result)