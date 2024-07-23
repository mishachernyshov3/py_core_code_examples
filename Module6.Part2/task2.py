# Створити клас рядка, який вміє повертати індекси усіх підрядків
from collections import UserString


class SearchingString(UserString):
    def find_all(self, substring):
        occurrences = []
        index = 0
        while index < len(self.data):
            index = self.data.find(substring, index)
            if index == -1:
                break
            occurrences.append(index)
            index += 1
        return occurrences


some_str = SearchingString("Hellolo Hello Hello")
print(some_str.find_all("lo"))
