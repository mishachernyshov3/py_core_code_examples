"""
Написати функцію, що визначає порядковий номер дня у році для певної дати.
"""
import datetime


def get_date_day_order(date):
    first_year_day = date.replace(day=1, month=1)
    return (date - first_year_day + datetime.timedelta(days=1)).days


def get_date_day_order2(date: datetime.date):
    date_ordinal = date.toordinal()
    first_year_day_ordinal = datetime.date(date.year, 1, 1).toordinal()
    return date_ordinal - first_year_day_ordinal + 1


today_date = datetime.datetime.today()

print(get_date_day_order(today_date))
print(get_date_day_order(datetime.datetime(2019, 10, 29)))
print(get_date_day_order2(datetime.datetime(2019, 10, 29)))
