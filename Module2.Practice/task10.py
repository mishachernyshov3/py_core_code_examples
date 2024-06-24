# Користувач вводить через кому оцінки 0-100. Визначити кількість поганих оцінок (від 0 до 59).

grades = list(map(int, input().split(',')))
bad_grades_count = 0

for grade in grades:
    if grade < 60:
        bad_grades_count += 1

print(bad_grades_count)
