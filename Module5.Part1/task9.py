# Написати генератор квадратів чисел.

def generate_squares(min_num, max_num):
    current_number = min_num

    while current_number < max_num:
        yield current_number ** 2
        current_number += 1


for k in generate_squares(1, 6):
    print(k)


print(list(generate_squares(1, 6)))
