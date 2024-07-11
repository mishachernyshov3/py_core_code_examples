# Create multiplication function currying.

def get_multiplication(first_number):
    def inner(second_number):
        return first_number * second_number

    return inner


print(get_multiplication(10)(5))
