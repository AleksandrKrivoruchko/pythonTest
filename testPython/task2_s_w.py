# Написать калькулятор с операциями:
# Умножение,деление, остаток от деления, вычитание, целочисленное деление.
def calcs(a, b, sign):
    if sign == '+':
        return a + b
    elif sign == '-':
        return a - b
    elif sign == '*':
        return a * b
    elif sign == '/':
        return a / b
    elif sign == '//':
        return a // b
    elif sign == '%':
        return a % b
    else:
        print('Неизвестный знак!')

a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
sign = input('Введите знак: ')
if not b and (sign == '/' or sign == '//' or sign == '%'):
    print('Делнее на ноль невозможно!')
else:
    print('{} {} {} = {}'.format(a, sign, b, calcs(a, b, sign)))
