# Create an iterator that will provide values from a positive number down to 0.
class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == 0:
            raise StopIteration
        self.current -= 1
        return self.current


if __name__ == '__main__':
    counter = CountDown(5)
    for count in counter:
        print(count)
