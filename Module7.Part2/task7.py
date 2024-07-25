# Iterate subgenerator.
def subgenerator():
    yield 'A'
    yield 'B'
    yield 'C'


def generator():
    yield 'Start'
    yield from subgenerator()
    yield 'End'


for value in generator():
    print(value)
