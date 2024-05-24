# Шифр Цезаря. Пользователь вводит строку и ключ

# шифра, программа должна вывести зашфированную
# строку (со сдвигом по ключу). Сдвиг циклический.
# Используем только латинский алфавит,
# пробелы не шифруются.
# Пример:
# Dog, 2 -> Fqi
# Zak zak -> Cdn cdn
# Python is the BEST -> Udymts nx ymj GJXY
alphabets_in_capital = []
for i in range(65, 91):
    alphabets_in_capital.append(chr(i))

alphabets_in_lowercase = []
for i in range(97, 123):
    alphabets_in_lowercase.append(chr(i))

lower_length = len(alphabets_in_lowercase)
capital_length = len(alphabets_in_capital)

# string = 'Python is the BEST'
# key = 5

string = input('Введите строку: ')
key = int(input('Введите ключ: '))

result = ''
for sym in string:
    if sym.isalpha() and sym.islower():
        new_index = (alphabets_in_lowercase.index(sym) + key) % lower_length
        new_sym = alphabets_in_lowercase[new_index]
        result += new_sym
    elif sym.isalpha():
        new_index = (alphabets_in_capital.index(sym) + key) % capital_length
        new_sym = alphabets_in_capital[new_index]
        result += new_sym
    else:
        result += sym

print(f'{string} -> {result}')
