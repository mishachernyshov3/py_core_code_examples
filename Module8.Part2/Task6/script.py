# Реалізувати глибоке копіювання завдань, не копіюючи об'єкти відповідей, так як вони для різних студентів не
# змінюються. Відповіді перемішуються під час копіювання.
import copy
import random


class Answer:
    def __init__(self, content, is_correct):
        self.__content = content
        self.__is_correct = is_correct

    @property
    def content(self):
        return self.__content

    @property
    def is_correct(self):
        return self.__is_correct

    def __repr__(self):
        return f"Answer({self.__content}, {self.__is_correct})"


class Quiz:
    def __init__(self, question: str, answers: list[Answer]):
        self.__question = question
        self.__answers = answers

    @property
    def question(self):
        return self.__question

    @property
    def answers(self):
        return self.__answers

    def __repr__(self):
        return f"Quiz({self.__question}, {self.__answers})"

    def __deepcopy__(self, _):
        answers = copy.copy(self.__answers)
        random.shuffle(answers)

        return Quiz(self.__question, answers)


quiz1 = Quiz(
    "Who created Python?",
    [
        Answer("Guido van Rossum", True),
        Answer("Rasmus Lerdorf", False),
        Answer("Brendan Eich", False),
    ],
)
quiz2 = Quiz(
    "What is the capital of France?",
    [
        Answer("Paris", True),
        Answer("Berlin", False),
        Answer("London", False),
    ],
)

student1_tests = [copy.deepcopy(quiz1), copy.deepcopy(quiz2)]
student2_tests = [copy.deepcopy(quiz1), copy.deepcopy(quiz2)]
print(student1_tests)
print(student2_tests)
