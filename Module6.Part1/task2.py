# Приклади MRO
class A:
    def display(self):
        print(f" From class A")


class B(A):
    def display(self):
        print(f" From class B")


class C(A):
    def display(self):
        print(f" From class C")


class D(C, B):
    def display(self):
        print(f" From class D")


class E(B, C):
    def display(self):
        print(f" From class E")


class F(D, E):
    pass


print(E.mro())
print(D.mro())
