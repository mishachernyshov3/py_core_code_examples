# Є банк тестів для тестування. Вибрати N випадкових тестів і перемішати варіанти відповідей.
import random
from collections import namedtuple
from copy import deepcopy
from pprint import pp


Test = namedtuple("Test", ("question", "answers"))

tests = [
    Test(
        "Who created Python?",
        ["Guido van Rossum", "Rasmus Lerdorf", "Brendan Eich"],
    ),
    Test(
        "What is the capital of France?",
        ["Paris", "Berlin", "London"],
    ),
    Test(
        "Who wrote 'The Great Gatsby'?",
        ["F. Scott Fitzgerald", "Ernest Hemingway", "Charles Dickens"],
    ),
    Test(
        "What is the largest planet in our solar system?",
        ["Jupiter", "Saturn", "Neptune"],
    ),
    Test(
        "Who painted the Mona Lisa?",
        ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso"],
    ),
    Test(
        "What year did the Titanic sink?",
        ["1912", "1905", "1923"],
    ),
    Test(
        "What is the chemical symbol for gold?",
        ["Au", "Ag", "Fe"],
    ),
    Test(
        "Who discovered penicillin?",
        ["Alexander Fleming", "Marie Curie", "Albert Einstein"],
    ),
]

n = int(input("Enter the number of tests to choose: "))

selected_tests = deepcopy(tests)
random.shuffle(selected_tests)
selected_tests = selected_tests[:n]

for test in selected_tests:
    random.shuffle(test.answers)

pp(selected_tests)
