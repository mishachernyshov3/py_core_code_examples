# Порахувати Ваш вік
import datetime
import math


def get_int_input(input_message: str) -> int:
    """
    Provides integer value inputted from a user.
    """
    while True:
        try:
            return int(input(input_message))
        except ValueError:
            print("The value should be a valid integer.")


def calculate_age(datetime_of_birth: datetime.datetime) -> int:
    """
    Calculates a person's age.
    """
    current_date: datetime.datetime = datetime.datetime.now()
    return math.floor(
        (current_date - datetime_of_birth).days / 365.25
    )


birth_year = get_int_input("Please, enter a valid year: ")
birth_month = get_int_input("Please, enter a valid month: ")
birth_day = get_int_input("Please, enter a valid day: ")
birth_datetime = datetime.datetime(
    year=birth_year,
    month=birth_month,
    day=birth_day,
)

print(calculate_age(birth_datetime))
