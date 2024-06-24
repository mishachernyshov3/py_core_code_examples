# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, ...  <-- Фібоначі

def get_fibonacci_number(number):
    if number <= 1:
        return number

    return get_fibonacci_number(number - 1) + get_fibonacci_number(number - 2)


print(get_fibonacci_number(10))
