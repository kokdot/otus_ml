# Отпуск. Пользователь вводит сколько дней осталось до ближайшего отпуска.
# Программа должна вывести количество выходных дней до отпуска,
# если учесть что выходные это суббота и воскресенье,
# сегодня понедельник и праздники мы не учитываем.
# Пример:
# 4 -> 0
# 6 -> 1
# 14 -> 2
number = int(input('Введите количество дней до отпуска: '))
result = 0
number_of_weeks = number // 7
result += number_of_weeks * 2
number_of_days_in_last_weeks = number % 7
if number_of_days_in_last_weeks == 6:
    result += 1
print(f'{number} -> {result}')
