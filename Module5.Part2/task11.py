# Check whether we can process at least one number.
num_string = input("Enter numbers separated by whitespaces: ")
numbers = num_string.split(" ")

if any(
    map(
        lambda num_str: num_str.isnumeric(),
        numbers,
    ),
):
    print("There are values for processing.")
else:
    print("There are no values to process.")
