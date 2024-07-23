# Створити клас-список унікальних елементів
from collections import UserList


class UniqueList(UserList):
    def __init__(self, initlist=None):
        unique_initlist = self.__build_unique_list(initlist) if initlist else None

        super().__init__(unique_initlist)

    def __build_unique_list(self, original_list):
        unique_list = []
        for item in original_list:
            if item not in unique_list:
                unique_list.append(item)
        return unique_list

    def append(self, item):
        if item not in self.data:
            return super().append(item)
        return None

    def extend(self, other):
        super().extend(other)

        self.data = self.__build_unique_list(self.data)

    def insert(self, index, item):
        if item not in self.data:
            super().insert(index, item)

    def __setitem__(self, index, item):
        if item not in self.data:
            super().__setitem__(index, item)


default_list = []
default_list.append(1)
default_list.append(1)
default_list.append(2)

my_list = UniqueList()
my_list.append(1)
my_list.append(1)
my_list.append(2)

print(default_list)
print(UniqueList([1, 1, 2]))
print(my_list)
