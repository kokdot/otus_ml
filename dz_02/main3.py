# Написать упрощенную версию алгоритма RLE.

# Алгоритм RLE объединяет подряд идущие символы в
# коэффициент и символ.
# Пример:
# aaabbbbccccc -> 2a4b5c
# asssdddsssddd -> 1a3s3d3s3d
# abcba -> 1a1b1c1b1a

string = input('Введите сроку для кодирования: ')
recent = string[0]
current = string[1]
result = ''
i = 1
index = 1
while i < len(string) - 1:
    if recent == current:
        index += 1
    else:
        result += str(index) + str(recent)
        index = 1
    recent = string[i]
    current = string[i + 1]
    i += 1
result += str(index) + str(recent)
print(f'result: {result}')
