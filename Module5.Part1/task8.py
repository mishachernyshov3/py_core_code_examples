# Додати завдання у чергу відповідно до типу (від нашвидших до найдовших) і виконати їх.
from collections import deque


tasks = [
    {"type": "fast", "name": "Помити посуд"},
    {"type": "slow", "name": "Подивитись серіал"},
    {"type": "fast", "name": "Вигуляти собаку"},
    {"type": "slow", "name": "Почитати книгу"}
]

task_queue = deque()

for task in tasks:
    if task["type"] == "fast":
        task_queue.appendleft(task)
        print(f"Додано швидке завдання: {task['name']}")
    else:
        task_queue.append(task)
        print(f"Додано повільне завдання: {task['name']}")


while task_queue:
    task = task_queue.popleft()
    print(f"Виконується завдання: {task['name']}")
