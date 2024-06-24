# Створити функцію, яка повертатиме функцію, що рахує кількість своїх викликів


def get_counter():
    count_value = 0

    def inner():
        nonlocal count_value
        count_value += 1
        return count_value

    return inner


counter1 = get_counter()
counter2 = get_counter()
