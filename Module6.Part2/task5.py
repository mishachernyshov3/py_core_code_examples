# Створити декортатор класу, що змінює його рядкове представлення.

def str_modifier(cls):
    def __str__(self):
        return f"DECORATED class {self.__class__.__name__}"

    cls.__str__ = __str__

    return cls


@str_modifier
class A:
    name: str
    age: int


@str_modifier
class B:
    name: str
    age: int


print(str(A()))
print(str(B()))
