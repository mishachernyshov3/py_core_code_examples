# Compare execution speed of ordinal factorial function and the one with caching.
import sys
from time import time


def get_factorial_calculator():
    computed_factorials = {0: 1, 1: 1}

    def inner(number):
        max_calculated_factorial_number = max(computed_factorials.keys())

        for i in range(max_calculated_factorial_number, number + 1):
            computed_factorials[i] = computed_factorials[i - 1] * i
        return computed_factorials[number]

    return inner


def get_factorial(number):
    if number == 0:
        return 1

    result = 1
    for i in range(1, number + 1):
        result *= i

    return result


if __name__ == '__main__':
    sys.set_int_max_str_digits(0)

    start_time = time()
    factorial_calculator = get_factorial_calculator()
    for k in range(5000):
        factorial_calculator(k)
    print(f'Cached time: {time() - start_time}')

    start_time = time()
    for k in range(5000):
        get_factorial(k)
    print(f'Raw time: {time() - start_time}')
