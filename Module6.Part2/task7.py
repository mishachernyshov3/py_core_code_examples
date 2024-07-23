# Створити Enum підтримуваних мов програмування для автоперевірки і перевірити програмний код для вказаної мови.
import os
from enum import Enum, auto


class SupportedLanguages(Enum):
    PYTHON = auto()
    JAVA = auto()


def evaluate_code(code, expected_result, language=SupportedLanguages.PYTHON):
    match language:
        case SupportedLanguages.PYTHON:
            with open("python_task.py", "w") as py_file:
                py_file.write(code)
            os.system("python3 python_task.py")
            with open("output.txt") as output_file:
                res = output_file.read()
            os.remove("python_task.py")
            os.remove("output.txt")
            return res == expected_result
        case SupportedLanguages.JAVA:
            with open("java_task.java", "w") as java_file:
                java_file.write(code)
            os.system("javac JavaTask.java")
            os.system("java JavaTask")
            with open("output.txt") as output_file:
                res = output_file.read()
            os.remove("javac JavaTask.java")
            os.remove("output.txt")
            return res == expected_result


py_code = (
"""
with open("output.txt", "w") as f:
    f.write("100")
"""
)

print(evaluate_code(py_code, "100"))
