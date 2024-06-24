# Визначити, чи використані у скрипті ключові слова Python

reserved_keywords = {"while", "for", "if", "def", "class", "return", "continue"}
script_variable_names = {"person", "while", "age", "class"}
wrong_variable_names = reserved_keywords.intersection(script_variable_names)

if wrong_variable_names:
    print(
        "The variable names {} are not allowed.".format(
            ", ".join(
                map(lambda x: f'"{x}"', wrong_variable_names)
            )
        )
    )
