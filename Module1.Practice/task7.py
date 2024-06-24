# Робота із словниками
import datetime

person: dict = {
    'age': 18,
    'name': 'John',
    'birthday': datetime.date(day=26, month=2, year=1995),
    17: 'Hello'
}

person.update({
    'age': 27, 
    'name': 'Hello',
})

print(person['age'])
print(person['name'])
