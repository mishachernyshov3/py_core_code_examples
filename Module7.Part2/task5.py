# Create a generator of average value counting.

def running_average():
    total = 0
    count = 0
    average = None

    while True:
        value = yield average
        total += value
        count += 1
        average = total / count


ra = running_average()

next(ra)

print(ra.send(10))  # Output: 10.0 (average of [10] is 10.0)
print(ra.send(20))  # Output: 15.0 (average of [10, 20] is 15.0)
print(ra.send(30))  # Output: 20.0 (average of [10, 20, 30] is 20.0)
print(ra.send(5))  # Output: 16.25 (average of [10, 20, 30, 5] is 16.25)
