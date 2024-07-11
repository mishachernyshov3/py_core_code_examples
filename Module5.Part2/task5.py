# Create a function that call its call count.

def get_calls_count():
    counter = 0

    def inner():
        nonlocal counter
        counter += 1
        return counter

    return inner


calls_counter = get_calls_count()

for k in range(10):
    print(calls_counter())
