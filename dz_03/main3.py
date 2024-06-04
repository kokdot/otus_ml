# Функция проверки на простое число. Простое число - число,
# которое имеет всего 2 делителя еденица и оно само.
# Пример:
# 17 -> True
# 20 -> False
# 23 -> True
import math


def is_simple(number):
    border = int(math.sqrt(number))
    for multiplier in range(2, border):
        if not number % multiplier:
            print(f'{number} -> False, multiplier = {multiplier}')
            return
    print(f'{number} -> True')


number = int(input('Введите число для проверки: '))
is_simple(number)
