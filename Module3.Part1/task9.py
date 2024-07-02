# Огляд модуля math
import math

numbers = [23.56, 23.31, -23.56, -23.31]

for number in numbers:
    print(f'Original: {number}. math.trunc: {math.trunc(number)}')
    print(f'Original: {number}. math.ceil: {math.ceil(number)}')
    print(f'Original: {number}. math.floor: {math.floor(number)}')
    print(f'Original: {number}. round: {round(number)}')
    print(f'Original: {number}. math.fabs: {math.fabs(number)}')
