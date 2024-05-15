# Пользователь вводит целое положительное число, программа должна
# вернуть строку в виде римского числа
# Пример:
# 3 -> III
# 15 -> XV
# 234 -> CCXXXIV
one = 'I'
two = 'II'
three = 'III'
three_plus_one = 'IV'
five = 'V'
six = 'VI'
seven = 'VII'
eight = 'VIII'
nine = 'IX'
ten = 'X'
twenty = 'XX'
thirty = 'XXX'
forty = 'XL'
fifty = 'L'
sixty = 'LX'
seventy = 'LXX'
eighty = 'LXXX'
ninety = 'XC'
hundred = 'C'
two_hundred = 'CC'
three_hundred = 'CCC'
for_hundred = 'CD'
five_hundred = 'D'
six_hundred = 'DC'
seven_hundred = 'DCC'
eight_hundred = 'DCCC'
nine_hundred = 'CM'
one_thousand = 'M'
two_thousand = 'MM'
three_thousand = 'MMM'
number = int(input(' Введите число: '))

result = ''
first = ''
second = ''
third = ''
forth = ''

if number >= 1000:
    forth = number % 10
    third = number // 10 % 10
    second = number // 100 % 10
    first = number // 1000

    if first == 1:
        result += one_thousand
    elif first == 2:
        result += two_thousand
    elif first == 3:
        result += three_thousand

    if second == 1:
        result += hundred
    elif second == 2:
        result += two_hundred
    elif second == 3:
        result += three_hundred
    elif second == 4:
        result += for_hundred
    elif second == 5:
        result += five_hundred
    elif second == 6:
        result += six_hundred
    elif second == 7:
        result += seven_hundred
    elif second == 8:
        result += eight_hundred
    elif second == 9:
        result += nine_hundred

    if third == 1:
        result += ten
    elif third == 2:
        result += twenty
    elif third == 3:
        result += thirty
    elif third == 4:
        result += forty
    elif third == 5:
        result += fifty
    elif third == 6:
        result += sixty
    elif third == 7:
        result += seventy
    elif third == 8:
        result += eighty
    elif third == 9:
        result += ninety

    if forth == 1:
        result += one
    elif forth == 2:
        result += two
    elif forth == 3:
        result += three
    elif forth == 4:
        result += three_plus_one
    elif forth == 5:
        result += five
    elif forth == 6:
        result += six
    elif forth == 7:
        result += seven
    elif forth == 8:
        result += eight
    elif forth == 9:
        result += nine

elif number >= 100:
    forth = number % 10
    third = number // 10 % 10
    second = number // 100

    if second == 1:
        result += hundred
    elif second == 2:
        result += two_hundred
    elif second == 3:
        result += three_hundred
    elif second == 4:
        result += for_hundred
    elif second == 5:
        result += five_hundred
    elif second == 6:
        result += six_hundred
    elif second == 7:
        result += seven_hundred
    elif second == 8:
        result += eight_hundred
    elif second == 9:
        result += nine_hundred

    if third == 1:
        result += ten
    elif third == 2:
        result += twenty
    elif third == 3:
        result += thirty
    elif third == 4:
        result += forty
    elif third == 5:
        result += fifty
    elif third == 6:
        result += sixty
    elif third == 7:
        result += seventy
    elif third == 8:
        result += eighty
    elif third == 9:
        result += ninety

    if forth == 1:
        result += one
    elif forth == 2:
        result += two
    elif forth == 3:
        result += three
    elif forth == 4:
        result += three_plus_one
    elif forth == 5:
        result += five
    elif forth == 6:
        result += six
    elif forth == 7:
        result += seven
    elif forth == 8:
        result += eight
    elif forth == 9:
        result += nine

elif number >= 10:
    forth = number % 10
    third = number // 10 % 10

    if third == 1:
        result += ten
    elif third == 2:
        result += twenty
    elif third == 3:
        result += thirty
    elif third == 4:
        result += forty
    elif third == 5:
        result += fifty
    elif third == 6:
        result += sixty
    elif third == 7:
        result += seventy
    elif third == 8:
        result += eighty
    elif third == 9:
        result += ninety

    if forth == 1:
        result += one
    elif forth == 2:
        result += two
    elif forth == 3:
        result += three
    elif forth == 4:
        result += three_plus_one
    elif forth == 5:
        result += five
    elif forth == 6:
        result += six
    elif forth == 7:
        result += seven
    elif forth == 8:
        result += eight
    elif forth == 9:
        result += nine

else:
    forth = number

    if forth == 1:
        result += one
    elif forth == 2:
        result += two
    elif forth == 3:
        result += three
    elif forth == 4:
        result += three_plus_one
    elif forth == 5:
        result += five
    elif forth == 6:
        result += six
    elif forth == 7:
        result += seven
    elif forth == 8:
        result += eight
    elif forth == 9:
        result += nine

print(f'{number} -> {result}')
