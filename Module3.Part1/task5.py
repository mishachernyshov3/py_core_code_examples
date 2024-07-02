# Підрахувати час обчислення суми чисел від 0 до N.
import time

n = int(input("Enter n: "))


def get_numbers_sum(max_number):
    result = 0
    for number in range(max_number + 1):
        result += number
    return result


start = time.time()
get_numbers_sum(n)
end = time.time()

print(end - start)
