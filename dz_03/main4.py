# Пользователь в бесконечном цикле вводит данные пользователей:
# имя, затем фамилию, возраст и ID.
# Ввод продолжается до тех пор пока не будет введено пустое поле.
# Пользователи заносятся в словарь, где ключ это ID пользователя,
# а остальные данные записываются в виде кортежа.
# Так же программа должна проверять,
# что имя и фамилия состоят только из символов и
# начинаются с большой буквы, если не с большой,
# то заменяет на большую, возраст должен быть числом от 18 до 60,
# ID - целое число, дополненое до 8 знаков незначащими нолями,
# ID должен быть уникальным
# Дополнительно написать функцию, которая будет выводить полученный
# словарь в виде таблицы
test_list = ['tom dore 23 1', 'dick smith 34 2', 'jhon bore 35 3']
my_dict = {}


def quiz():
    while True:
        string = input('Введите новую строку: ')
        if not string:
            print_my_dict(my_dict)
            return
        parsed_string = string.split()
        name = parsed_string[0]
        if not name.isalpha():
            print(f'Имя должно состоять из букв, Вы ввели {name}')
            continue
        name = name.capitalize()
        surname = parsed_string[1]
        if not surname.isalpha():
            print(f'Имя должно состоять из букв, Вы ввели {surname}')
            continue
        surname = surname.capitalize()
        age = int(parsed_string[2])
        if age > 60 or age < 18:
            print(f'Возраст должен быть от 18 до 60, Вы ввели: {age}')
            continue
        id = parsed_string[3]
        if not id.isdigit():
            print(f'ID должно состоять целым числом, Вы ввели {id}')
            continue
        my_dict[int(id)] = tuple([name, surname, age])
    return


def print_my_dict(my_dict):
    for id, line in my_dict.items():
        print(f"{id : 08d}: {line}")


quiz()
