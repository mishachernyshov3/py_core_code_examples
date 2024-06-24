# 5-значне число
# Сума третьої і другої цифри - ?
# Сума третьої і першої цифри
# Сума 4 і 5 цифри

number = int(input("Enter 5-x number: "))

fifth_d = number % 10
forth_d = number // 10 % 10
third_digit = number // 100 % 10
second_digit = number // 1000 % 10
first_digit = number // 10000 % 10

print(third_digit + second_digit)
print(third_digit + first_digit)
print(forth_d + fifth_d)
