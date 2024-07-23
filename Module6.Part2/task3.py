# Створити клас словника, який не дозволяє встановлювати значення для ключів, що вже існують
from collections import UserDict


class KeyAlreadyExistsError(Exception):
    def __init__(self, message="The provided key is already inside a dict. Please, remove it and try again."):
        self.message = message
        super().__init__(self.message)


class CustomDict(UserDict):
    def __setitem__(self, key, value):
        if key in self.data:
            raise KeyAlreadyExistsError
        super().__setitem__(key, value)


dict_1 = CustomDict({"name": "Ivan", "age": 34})
dict_1["name"] = "Ihor"
