# Create special case multiplication functions by closure and `functools.partial`.
from functools import partial


def get_multiplication(first_number, second_number):
    return first_number * second_number


get_multiplication_by_10 = partial(get_multiplication, 10)


def custom_get_multiplication_by_10(second_number):
    return get_multiplication(10, second_number)


print(get_multiplication_by_10(50))
print(custom_get_multiplication_by_10(50))
