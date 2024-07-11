# Create a function special case by nested functions.
from typing import Callable


def get_multiplication(first_number) -> Callable[[float], float]:
    def inner(second_number: float) -> float:
        return first_number * second_number

    return inner


mult_by_10 = get_multiplication(10)

print(mult_by_10(5))
print(mult_by_10(7))
print(mult_by_10(10))


mult_by_2 = get_multiplication(2)

print(mult_by_2(5))
print(mult_by_2(7))
print(mult_by_2(10))
