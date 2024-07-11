# Write a decorator that prints function execution time.
from time import time

from task6 import get_factorial


def print_execution_time(func):
    def inner(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} execution took {time() - start} seconds.")
        return result
    return inner


enhanced_get_factorial = print_execution_time(get_factorial)

print(enhanced_get_factorial(6))
