# Визначити, чи усі цифри числа різні

number = input("Enter a number: ")
number_all_digits_count = len(number)
number_unique_digits = set(number)
number_unique_digits_count = len(number_unique_digits)

if number_all_digits_count == number_unique_digits_count:
    print("All digits are unique")
elif number_unique_digits_count == 1:
    print("All digits are the same")
else:
    print("Not all digits are unique")
