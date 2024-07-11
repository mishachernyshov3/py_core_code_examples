# Several decorators applying example.
import functools
from collections import deque
from time import time


def cache(cache_size=50):
    def inner(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            cache_key = args + tuple(kwargs.items())

            if cache_key in wrapper.cache:
                return wrapper.cache[cache_key]

            result = func(*args, **kwargs)

            if len(wrapper.cache) == cache_size:
                oldest_cache_key = wrapper.cache_keys_order.popleft()
                del wrapper.cache[oldest_cache_key]

            wrapper.cache[cache_key] = result
            wrapper.cache_keys_order.append(cache_key)
            return result

        wrapper.cache = {}
        wrapper.cache_keys_order = deque()

        return wrapper
    return inner


def print_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        Prints the function execution time.
        """
        start = time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} execution took {time() - start} seconds.")
        return result
    return wrapper


@cache(cache_size=2)
@print_execution_time
def get_factorial(number):
    """
    Calculates the factorial of a number.
    """
    if number == 0:
        return 1

    result = 1
    for i in range(1, number + 1):
        result *= i

    return result


print(get_factorial(6))
print(get_factorial.__doc__)
