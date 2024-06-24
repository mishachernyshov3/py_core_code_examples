# Створити функцію, яка приймає словник із даними про користувача і виводить його вік

from datetime import datetime

person = {
    'first_name': 'Oleksandr',
    'last_name': 'Ivanov',
    'email': 'olexandrivanov1959@example.com',
    'birth_date': datetime(year=1959, month=1, day=3),
    'marriage_date': datetime(year=1991, month=10, day=12),
}


def print_age(first_name, last_name, birth_date, **kwargs):
    age = datetime.now().year - birth_date.year
    print(f'{first_name} {last_name} is {age} years old.')


print_age(**person)
