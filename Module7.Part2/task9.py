# Calculate average values of different sources using subgenerators.

def main(data):
    results = {}

    for key, values in data.items():
        group = grouper(results, key)
        next(group)
        for value in values:
            group.send(value)
        group.send(None)

    report(results)


def grouper(results, key):
    while True:
        results[key] = yield from averager()


def averager():
    total = 0
    count = 0
    average = None

    while True:
        value = yield average
        if value is None:
            break
        total += value
        count += 1
        average = total / count

    return average


def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print('{:5} averaging {:.2f}{}'.format(group, result, unit))


data = {
    'girls;kg': [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
    'girls;m': [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
    'boys;kg': [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
    'boys;m': [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
}


main(data)
