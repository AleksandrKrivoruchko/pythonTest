# При заданном целом числе n посчитайте n + nn + nnn
str_number = input('Введите число: ')
if str_number[0] == '-':
    nn = str_number + str_number[1:]
    nnn = str_number + nn[1:]
else:
    nn = str_number + str_number
    nnn = str_number + nn
sum = int(str_number) + int(nn) + int(nnn)
print(f'{str_number} + {nn} + {nnn} = {sum}')
print('Вариант второй:')
n = int(str_number)
print(f'{str_number} + {n} * {n} + {n} * {n} * {n} = {n*(1 + n + n*n)}')
