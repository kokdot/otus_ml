# Пользователь вводит целое число, программа складывает все цифры
# числа, с полученым числом - тоже самое и так до тех пор, пока не
# получится однозначное число.
# Пример:

# 545 -> 5
# 12345 -> 6
number = int(input('Введите число: '))
input_number = number
leftover = 0
result = 0
# number = 12345
while number > 10:
    result = 0
    while number > 0:
        leftover = number % 10
        result += leftover
        number = number // 10
    number = result
print(f'{input_number} -> {result}')
