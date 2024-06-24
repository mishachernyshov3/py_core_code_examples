# Зчитати числа із консолі (через кому) і вивести суму

numbers_string: str = input('Enter numbers: ')
numbers_list: list[str] = numbers_string.split(',')
int_numbers: list[float] = list(map(float, numbers_list))

print(numbers_string)
print(numbers_list)
print(int_numbers)
print(sum(int_numbers))

