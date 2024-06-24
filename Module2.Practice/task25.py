# Знайти суму чисел списку

lst = [10, -20, 50, -100]


def get_negative_sum(numbers):
    if not numbers:
        return 0

    first_number = numbers[0]

    if first_number < 0:
        return numbers[0] + get_negative_sum(numbers[1:])
    return get_negative_sum(numbers[1:])


print(get_negative_sum(lst))
