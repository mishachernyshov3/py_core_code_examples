# Output only even numbers from inputted ones.
num_string = input("Enter numbers separated by whitespaces: ")
numbers = num_string.split(" ")

even_nums = list(
    filter(
        lambda num: num % 2 == 0,
        map(int, numbers),
    )
)
even_nums2 = [
    int_num
    for str_num in numbers
    if (int_num := int(str_num)) % 2 == 0
]

print(f"Even numbers (map-filter): {even_nums}")
print(f"Even numbers (list comprehension): {even_nums2}")
