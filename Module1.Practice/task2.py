# Прямокутний трикутник
# a і b - катети, с - гіпотенуза.
# c - ? a ^ 2 + b ^ 2 = c ^ 2 -> c = (a ^ 2 + b ^ 2) ^ 0.5
# S - ? S = a * b / 2


a = int(input("Enter 'a' value: "))
b = int(input("Enter 'b' value: "))

c = (a ** 2 + b ** 2) ** 0.5
S = a * b / 2
print(f'c = {c}, S = {S}')
