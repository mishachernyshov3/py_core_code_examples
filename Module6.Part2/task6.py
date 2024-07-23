# Створити Enum днів тижня і для кожного дня тижня повертати години роботи закладу в цей день.
from enum import Enum


class IncorrectWeekDay(Exception):
    pass


class WeekDay(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


def get_opening_hours(weekday_value: int) -> str:
    match weekday_value:
        case WeekDay.SUNDAY.value | WeekDay.SATURDAY.value:
            return "Day off"
        case WeekDay.TUESDAY.value | WeekDay.THURSDAY.value:
            return "8:00 - 21:00"
        case WeekDay.MONDAY.value | WeekDay.WEDNESDAY.value:
            return "9:00 - 20:00"
        case WeekDay.FRIDAY.value:
            return "10:00 - 18:00"
        case _:
            raise IncorrectWeekDay


print(get_opening_hours(2))
