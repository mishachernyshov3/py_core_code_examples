# Із класу, що складається із 25 учнів, можна виділити 5 учнів для чергування по школі.
# Скільки існує можливих варіантів чергових бригад?

import math

n = int(input("Enter n: "))
k = int(input("Enter k: "))

C = (math.factorial(n)) / (math.factorial(k) * math.factorial(n - k))

print(f"C = {C}")
