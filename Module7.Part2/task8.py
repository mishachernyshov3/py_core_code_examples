# Chain generators.

def numbers_up_to(n):
    for i in range(1, n + 1):
        yield i


def square_each(nums):
    for num in nums:
        yield num * num


def even_numbers_up_to(n):
    yield from (x for x in range(2, n + 1, 2))


for num in square_each(numbers_up_to(5)):
    print(num)

for num in even_numbers_up_to(10):
    print(num)
