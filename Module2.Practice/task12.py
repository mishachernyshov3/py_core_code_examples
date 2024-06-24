# Створено Machine learning модель, яка має дослідити, чи впливає
# номер у черзі на іспті на фінальну оцінку.
# Для цього створити список індексів поганих оцінок, який буде
# передано цій моделі.

exam_results = [
    {"grade": 95, "name": "Jessica Williams"},
    {"grade": 100, "name": "Daniel Brown"},
    {"grade": 66, "name": "Emily Davis"},
    {"grade": 5, "name": "James Miller"},
    {"grade": 87, "name": "Olivia Wilson"},
    {"grade": 99, "name": "Ethan Moore"},
]
bad_results_indexes = []

for index, result in enumerate(exam_results):
    if result["grade"] < 60:
        bad_results_indexes.append(index)


print(bad_results_indexes)
