# Написать программу вычисления арифметического выражения заданного строкой.
# Используются операции +,-,/,*.
# приоритет операций стандартный. Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# Добавить возможность использования скобок, меняющих приоритет операций.
# Пример: 1+2*3 => 7; (1+2)*3 => 9;
def calcs(a, b, sign):
    if not b and (sign == '/' or sign == '//' or sign == '%'):
        print('Деление на ноль невозможно!')
        return None
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
        return None


def calculation_expressions(list_exp, sign_list):
    len_list = len(list_exp) - 1
    i = 0
    while i < len_list:
        if list_exp[i] in sign_list:
            tmp = calcs(float(list_exp[i-1]), float(list_exp[i+1]), list_exp[i])
            if tmp is None:
                print(f'Ошибка в выражении {list_exp}')
                exit(1)
            del list_exp[i+1]
            del list_exp[i]
            list_exp[i-1] = str(tmp)
            len_list -= 2
            i -= 1
        i += 1


def counting_expressions(in_list):
    sign_mul_div = ['*', '/']
    sign_add_sub = ['+', '-']
    calculation_expressions(in_list, sign_mul_div)
    calculation_expressions(in_list, sign_add_sub)
    print(in_list)
    return str(in_list[0])


def analysis_string_expression(in_str):
    signs = ['+', '-', '*', '/']
    temp_str = ''
    str_list = []
    i = 0
    while i < len(in_str):
        if in_str[i] in signs:
            if i != 0 and in_str[i-1].isdigit():
                str_list.append(in_str[i])
                i += 1
            else:
                temp_str += in_str[i]
                i += 1
        while in_str[i].isdigit() or in_str[i] == '.':
            temp_str += in_str[i]
            i += 1
            if i > len(in_str) - 1:
                break
        if len(temp_str) > 0:
            str_list.append(temp_str)
        temp_str = ''

    return counting_expressions(str_list)


def analysis_string(source_str):
    source_str = source_str.strip().replace(' ', '')
    print(source_str)
    len_str = len(source_str)
    if '(' in source_str:
        i = 0
        while i < len_str:
            if source_str[i] == '(':
                start_index = i
            elif source_str[i] == ')':
                stop_index = i
                tmp_str = analysis_string_expression(source_str[start_index + 1: stop_index])
                if start_index == 0 and stop_index == len_str - 1:
                    return tmp_str
                elif start_index == 0 and stop_index < len_str - 2:
                    return analysis_string(tmp_str + source_str[stop_index + 1:])
                elif stop_index == len_str - 1:
                    return analysis_string(source_str[:start_index] + tmp_str)
                else:
                    return analysis_string(source_str[:start_index] + tmp_str + source_str[stop_index + 1:])
            i += 1
    else:
        return analysis_string_expression(source_str)


temp = analysis_string('((2+(-3+-4 * -3/2 )  *4)+(25 + 2 * 10)/-2 * (-10/5*2 + 2) + 1)/2')
print(temp)
