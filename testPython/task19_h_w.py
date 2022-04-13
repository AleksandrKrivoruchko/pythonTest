# Подсчитать сумму цифр в вещественном числе
def sum_digits(str_source):
    len_str = len(str_source)
    sum_number_digits = 0
    i = 0
    if str_source[i] == '-':
        i = 1
    while i < len_str:
        if str_source[i] != '.':
            sum_number_digits += int(str_source[i])
        i += 1
    return sum_number_digits


def is_string_number(input_str):
    len_str = len(input_str)
    is_dot = False
    i = 0
    if input_str[i] == '-':
        i = 1
    while i < len_str:
        if input_str[i] == '.':
            if is_dot:
                return False
            is_dot = True
            i += 1
            continue
        if not input_str[i].isdigit():
            return False
        i += 1
    return True


str_number = input('Введите число: ')
if is_string_number(str_number):
    sum_result = sum_digits(str_number)
    print(f'Сумма цифр числа {str_number} равна {sum_result}')
else:
    print(f'Это {str_number} - не число.')
