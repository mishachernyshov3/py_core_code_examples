# Обчислити ділення чтсел a на b, зчитаних із консолі

try:
    a = int(input())
    b = int(input())
except ValueError:
    print("Incorrect int values")
else:
    try:
        print(f"Division result: {a / b}")
    except ZeroDivisionError:
        print("Zero division is not allowed.")
