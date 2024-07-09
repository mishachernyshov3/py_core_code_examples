# Написати генератор чисел Фібоначчі

def generate_fibonacci():
    yield 0

    previous = 0
    current = 1

    while True:
        next_number = previous + current
        yield current
        previous = current
        current = next_number


gen = generate_fibonacci()

for k in range(10):
    print(next(gen))
