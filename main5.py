# Пользователь вводит данные, проверить - являються ли они положительным вещественным числом.
# Не использовать встроенные функции для проверки, только методы данных и конструкцию IF.
# (Дополнительное задание, по желанию - проверка на отрицательные вещественные числа)
# Пример:
# 5.6 -> True
# .78 -> True
# .67. -> False
# 5 -> True
import re
while True:
    number = input('Введите вещественное число или пробел для выхода: ')
    if number == ' ':
        break
    match = re.search(r'^[+-]?\d*\.?\d+$', number)
    print(f'{number} -> True' if match else f'{number} -> False')