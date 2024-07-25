# Create a functor that will allow to multiply a base number by an arbitrary number.

class Multiplier:
    def __init__(self, base_number):
        self.base_number = base_number

    def __call__(self, other_number):
        return self.base_number * other_number


multiply_by_5 = Multiplier(5)
print(multiply_by_5(10))
print(multiply_by_5(40))
