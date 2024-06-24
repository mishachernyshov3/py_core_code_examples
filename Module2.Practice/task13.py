# Вивести у табличному вигляді список учнів класу.

full_names = [
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

names_count = len(full_names)
order_column_width = len(str(names_count))


def get_max_name_length(names):
    max_length = 0

    for name in names:
        max_length = max(len(name), max_length)

    return max_length


names_column_width = get_max_name_length(full_names)


for line_number, full_name in enumerate(full_names, start=1):
    print(f'{line_number:>{order_column_width}}. {full_name:>{names_column_width}}')
