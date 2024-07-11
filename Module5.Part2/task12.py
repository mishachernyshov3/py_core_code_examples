# Comprehensions examples
nums = [1, 2, 2, 4, 7, 10, 7, 10, 11, 12, 16, 19, 21, 100]

set_comprehension = {i for i in nums if i % 2 == 0}
list_comprehension = [i for i in nums if i % 2 == 0]
generator_expression = (i for i in nums if i % 2 == 0)
dict_comprehension = {i: ("even" if i % 2 == 0 else "odd") for i in nums if i > 10}

print(dict_comprehension)

fruits = [
    ["apple", "banana", "cherry"],
    ["date", "fig", "grape"],
    ["kiwi", "lemon", "mango"],
]

capitalized_fruits = [[fruit.capitalize() for fruit in row] for row in fruits]

print(capitalized_fruits)

str_nums = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
]
print([
    int_num
    for row in str_nums
    for num in row
    if (int_num := int(num)) % 2 == 0
])

boiling_temperature_celsius = {
    "Al": 2518,
    "H2O": 100,
    "Hg": 357,
}
boiling_temperature_fahrenheit = {
    material: (celsius_temperature * 1.8) + 32
    for material, celsius_temperature in boiling_temperature_celsius.items()
}
print(boiling_temperature_fahrenheit)
