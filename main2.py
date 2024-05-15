# Пользователь вводит пятизначное число. Программа должна зеркально отразить центральные три цифры. Первая и последняя остаются на местах.
# Пример:
# 23456 -> 25436
# 30789 -> 38709
while True:
    number = int(input('Введите ваше число или 0 для выхода: '))
    if number == 0:
        break
    if len(str(number)) != 5:
        print('Число должно быть 5 значным')
        continue
    first = number // 10000
    second = number // 1000 % 10
    third = number // 100 % 10
    fifth = number // 10 % 10
    last = number % 10
    # print(f'first: {first} \nsecond: {second}\nthird: {third}\nfifth: {fifth}\nlast: {last}')
    result = int(str(first) + str(fifth) + str(third) + str(second) + str(last))
    print(f'{number} -> {result}')
