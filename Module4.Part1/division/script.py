# Зчитати з файлу "input.txt" пари чисел і порахувати ділення першого числа на друге.
# Результати записати у файл "output.txt".

input_file = open('input.txt')
output_file = open('output.txt', 'w', buffering=-1)
while True:
    line = input_file.readline()
    if not line:
        break
    dividend, divisor = map(float, line.split(' '))
    output_file.write(f'{dividend / divisor}\n')
input_file.close()
output_file.close()
