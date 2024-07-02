# Прибрати зайві пробіли в словах
import re

expected_string = "for while"
sentence = " for    while        "

print(re.sub(r" {2,}", " ", sentence).strip())
