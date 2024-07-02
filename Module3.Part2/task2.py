# Гравці мають вгадати слово за його описом. Зчитати відповіді гравця і визначити, чи вгадав він.
expected_word = "ring"
user_answers = input("Enter user answers: ")

if user_answers.find("ring") != -1:
    print("User answers correct.")
else:
    print("User answers incorrect.")
