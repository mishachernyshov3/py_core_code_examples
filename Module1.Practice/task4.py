# Є коло, r - радіус, знайти площу круга і довжину кола
import math

radius_string: str = input("Input R: ")
radius: float = float(radius_string)

l: float = 2 * math.pi * radius
S: float = math.pi * radius ** 2 / 2

print(f'l = {l:.2f}, S = {S:.1f}')
