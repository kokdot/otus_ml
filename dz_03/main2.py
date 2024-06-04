# Написать функцию проверяющую валидность введенной даты.
# Пример:
# 29.02.2000 -> True
# 29.02.2001 -> False
# 31.04.1962 -> False
month_dic = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


def intercalary_year(number):
    if not number % 4:
        if not number % 100:
            if not number % 400:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def control_date():
    data = input('Введите дату для проверки корректности: ')
    # data = '29.02.2024'
    data_split = data.split('.')
    print(f'data_split: {data_split}')
    if len(data_split) != 3:
        # print(len(data_split))
        print(f'1: {data} -> False')
        return
    if not data_split[0].isdigit() and not data_split[1].isdigit() and not data_split[3].isdigit():
        print(f'2: {data} -> False')
        return
    day = int(data_split[0])
    month = int(data_split[1])
    year = int(data_split[2])
    if month_dic[month] < day:
        if intercalary_year(year) and month == 2 and day == 29:
            print(f'4: {data} -> TRUE')
            return
        print(f'3: {data} -> False')
        return
    print(f'{data} -> True')
    return


control_date()
