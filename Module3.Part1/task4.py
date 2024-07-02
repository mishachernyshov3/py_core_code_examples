# Виверження вулкану відбулось о 12:45:19 30.04.2020 за Гринвічем.
# Вивести час виверження у 3 часовому поясі.
from datetime import datetime, timezone, timedelta

eruption_datetime = datetime(2020, 4, 30, 12, 45, second=19, tzinfo=timezone.utc)
third_timezone = timezone(timedelta(hours=3))
print(
    'Eruption datetime in 3 timezone:',
    eruption_datetime.astimezone(third_timezone).strftime('%d.%m.%Y %H:%M:%S'),
)
