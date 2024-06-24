# Знайти суму чисел списку

lst = [10, 20, 50, 100]


def get_sum(numbers):
    if not numbers:
        return 0

    return numbers[0] + get_sum(numbers[1:])


print(get_sum(lst))
