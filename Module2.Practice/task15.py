# Визначити, чи є число простим

y = int(input())

x = y // 2
while x > 1:
    if y % x == 0:
        print(y, 'hasfactor', x)
        break
    x -= 1
else:
    print(y, 'is prime')
