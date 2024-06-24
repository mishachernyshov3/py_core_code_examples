# Отримати число, цифри якого йдуть у зворотному порядку

def get_reversed_number(number):
    if len(number) < 2:
        return number

    return number[-1] + get_reversed_number(number[:-1])


print(get_reversed_number('12345'))
