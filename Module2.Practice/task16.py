# Визначити, чи немає помилки у значеннях пікселів матриці

MAX_ALLOWED_COLOR_VALUE = 255
MIN_ALLOWED_COLOR_VALUE = 0

matrix = [
    [(120, 221, 89), (120, 94, 89), (203, 64, 23), (75, 186, 11)],
    [(23, 43, 14), (120, 94, 89), (203, 64, 23), (75, 186, 56)],
    [(50, 85, 89), (120, 83, 89), (203, 43, 23), (52, 32, 259)],
    [(80, 1, 9), (120, 94, 89), (203, 64, 45), (75, 186, 12)],
]

for row in matrix:
    for column in row:
        for color_value in column:
            if not (MIN_ALLOWED_COLOR_VALUE <= color_value <= MAX_ALLOWED_COLOR_VALUE):
                print(f"Matrix is invalid. Value {color_value}")
                break
        else:
            continue
        break
    else:
        continue
    break
