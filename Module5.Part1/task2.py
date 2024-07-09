# Вивести імена студентів із найпоширенішою оцінкою.
from collections import Counter, namedtuple

TestResult = namedtuple('TestResult', ['student_name', 'grade'])

results = [
    TestResult('Emma Johnson', 2),
    TestResult('Liam Smith', 4),
    TestResult('Olivia Williams', 2),
    TestResult('Noah Brown', 5),
    TestResult('Ava Jones', 1),
    TestResult('William Garcia', 3),
    TestResult('Sophia Martinez', 4),
    TestResult('James Anderson', 2),
    TestResult('Mia Hernandez', 5),
    TestResult('Benjamin Clark', 5),
]

grades = [result.grade for result in results]

grades_counter = Counter(grades)
grade_counts = grades_counter.most_common()
most_common_grade_value = grade_counts[0][1]
most_common_grades = [count_tuple[0] for count_tuple in grade_counts if count_tuple[1] == most_common_grade_value]
students_with_the_most_common_grade = [
    result.student_name
    for result in results
    if result.grade in most_common_grades
]

print(students_with_the_most_common_grade)
