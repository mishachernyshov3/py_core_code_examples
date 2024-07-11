# Check whether all numbers are correct.
num_string = input("Enter numbers separated by whitespaces: ")
numbers = num_string.split(" ")

if all(
    map(
        lambda num_str: num_str.isnumeric(),
        numbers,
    ),
):
    print("All numbers are correct.")
else:
    print("Please, enter correct values.")
