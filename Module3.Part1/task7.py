# Створити функцію, що генерує випадковий пароль довжини N.
import random
import string

n = int(input("Enter the password length: "))


def generate_password(length):
    password = ""

    for i in range(length):
        allowed_characters = string.ascii_letters + string.digits
        password += random.choice(allowed_characters)

    return password


print(generate_password(n))
