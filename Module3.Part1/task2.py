# Визначити, у який день тижня у Вас буде день народження у 2025 році. Дату увести у форматі "dd-mm".
import datetime

datetime_string = input("Enter your birthday in format 'dd-mm': ")
birthday = datetime.datetime.strptime(datetime_string, "%d-%m")
birthday = birthday.replace(year=2025)

weekday_translations = {
    0: "Понеділок",
    1: "Вівторок",
    2: "Середа",
    3: "Четвер",
    4: "П'ятниця",
    5: "Субота",
    6: "Неділя",
}

print(weekday_translations[birthday.weekday()])
print(birthday.strftime("%A"))
