# Створити функцію, яка приймає словник із даними про користувача і перетворює усі значення дат у рядок

from datetime import datetime


person = {
    'first_name': 'Oleksandr',
    'last_name': 'Ivanov',
    'email': 'olexandrivanov1959@example.com',
    'birth_date': datetime(year=1959, month=1, day=3),
    'marriage_date': datetime(year=1991, month=10, day=12),
}


def get_json_person(person_dict):
    json_person = {}

    for attribute, value in person.items():
        if isinstance(value, datetime):
            json_person[attribute] = value.isoformat()
        else:
            json_person[attribute] = value

    return json_person


print(get_json_person(person))
