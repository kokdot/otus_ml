# Кинотеатр. Дан список списков, каждый вложенный
# список состоит из 1 и 0, Количество вложенных
# списков - количество рядов. Пользователь вводит
# сколько билетов ему требуется. Программа должна
# найти ряд, где можно приобрести нужно количество
# билетов (места должны быть рядом). Если таких
# рядов несколько то ближайший к экрану
# (ближайшим считается нулевой ряд).
# Ели таких мест нет, то вывести False
# Пример:
# [[0,1,1,0], [1, 0, 0, 0], [0,1,0,0]], 2 -> 1
# [[0,1,1,0], [1, 0, 1, 0], [1,1,0,1]], 2 -> False

number = int(input('Введите количество билетов: '))
# number = 4
cinema_hall = [[0, 1, 1, 0], [1, 0, 0, 0], [0, 0, 0, 0]]
success = False
result = 0
for row in cinema_hall:
    recent = 0
    for seat in row:
        print(f'seat: {seat}')
        print(f'recent: {recent}')
        if not seat:
            recent += 1
            # print(f'recent+: {recent}')
        else:
            recent = 0
            # print(f'recent-: {recent}')
        if recent == number:
            success = True
            break
    if success:
        break
    result += 1
print(f'{number} -> {result}')

