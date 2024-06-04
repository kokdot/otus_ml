# Написать функцию, которая будет перводит снейк_кейс в КэмелКейс
# и наоборот. Функция сама определяет - какой формат ей передали.
# Можно добавить ключевой аргумент, который будет принудительно
# возвращать один из форматов.
# Пример:
# otus_course -> OtusCourse
# PythonIsTheBest -> python_is_the_best
# string = 'PythonIsTheBest'
string = input('Введите слово: ')


def translate(string):
    result = ''
    check_underscore = False
    # print(string.find('_'))
    if string.find('_') >= 0:
        for i in range(len(string)):
            if i == 0:
                result += string[0].upper()
            elif check_underscore:
                result += string[i].upper()
                check_underscore = False
            elif string[i] != '_':
                result += string[i]
            elif string[i] == '_':
                check_underscore = True
    else:
        # print("else")
        for i in range(len(string)):
            # print(f'i = {i}, string[i] = {string[i]}, result = {result}')
            if i == 0:
                result += string[0].lower()
            elif not string[i].islower():
                result += '_'
                result += string[i].lower()
            else:
                result += string[i]
    return result


print(f'{string} -> {translate(string)}')
