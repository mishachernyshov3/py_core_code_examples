# Створити функцію, що поверне список квадратів чисел

numbers = [5, 7, 10, 15, 100]


def get_squares(lst):
    squares = []

    for num in lst:
        squares.append(num ** 2)

    return squares


print(get_squares(numbers))
