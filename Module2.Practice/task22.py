# Створити функцію, що повертає більше із двох значень і у глобальній змінній зберігає кількість викликів
# Заборонити виклик більше 3 разів

count_value = 0


def get_bigger_value(a, b):
    global count_value

    if count_value > 3:
        raise Exception("Too many calls")
    count_value += 1

    return a if a >= b else b


print(get_bigger_value(1, 3))
