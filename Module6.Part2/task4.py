# Розпарсити лані користувача із веб-форми. Інкапсулювати дані у dataclass-і.
import string
from dataclasses import dataclass


@dataclass
class UserData:
    first_name: str
    last_name: str
    password: str


class InvalidUserDataError(Exception):
    def __init__(self, errors):
        self.errors = errors

    def __str__(self):
        return str(self.errors)


def parse_user(user_data: dict) -> UserData:
    errors = {}

    if "first_name" in user_data:
        first_name = user_data["first_name"]
        if not (isinstance(first_name, str) and len(first_name) > 1):
            errors["first_name"] = "The value is incorrect"
    else:
        errors["first_name"] = "The value is missed"

    if "last_name" in user_data:
        last_name = user_data["last_name"]
        if not (last_name and isinstance(last_name, str)):
            errors["last_name"] = "The value is incorrect"
    else:
        errors["last_name"] = "The value is missed"

    if "password" in user_data:
        password = user_data["password"]
        if not (
            isinstance(password, str)
            and len(password) > 7
            and set(password).intersection(set(string.punctuation))
        ):
            errors["password"] = "The value is incorrect"
    else:
        errors["password"] = "The value is missed"

    if errors:
        raise InvalidUserDataError(errors)

    return UserData(first_name, last_name, password)


if __name__ == "__main__":
    user_data = parse_user({"first_name": "John", "last_name": "Lee", "password": "QWERTY435#$"})
    print(f"First name: {user_data.first_name}")
    print(f"Last name: {user_data.last_name}")
    print(f"Password: {user_data.password}")
