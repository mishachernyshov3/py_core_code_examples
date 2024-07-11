# Iterate a sequence of functions and call the functions from the list.

def add(first_number, second_number):
    return first_number + second_number


def subtract(first_number, second_number):
    return first_number - second_number


def multiply(first_number, second_number):
    return first_number * second_number


def divide(first_number, second_number):
    return first_number / second_number


def power(first_number, second_number):
    return first_number ** second_number


operations = (add, subtract, multiply, divide, power)
num_a = 5
num_b = 10

for operation in operations:
    print(f'"{operation.__name__}" function applying of {num_a} and {num_b}: {operation(num_a, num_b)}')
