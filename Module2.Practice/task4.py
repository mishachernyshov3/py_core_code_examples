# З'ясувати, чи є студент одним із переможців

student_name = input("Enter your name: ")

winners_list = [
    "Alice Johnson",
    "Michael Smith",
    "Jessica Williams",
    "Daniel Brown",
    "Emily Davis",
    "James Miller",
    "Olivia Wilson",
    "Daniel Miller",
    "Daniel Wilson",
    "Alice Smith",
]

print(
    f"Student is a winner"
    if student_name in winners_list
    else f"Student is not a winner"
)
