# Написать программу вычисления арифметического выражения заданного строкой.
# Используются операции +,-,/,*.
# приоритет операций стандартный. Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# Добавить возможность использования скобок, меняющих приоритет операций.
# Пример: 1+2*3 => 7; (1+2)*3 => 9;
def calcs(a, b, sign):
    if not b and (sign == '/' or sign == '//' or sign == '%'):
        print('Деление на ноль невозможно!')
        return
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


def convert_str_to_list(str_source):
    str_source = str_source.strip().replace(' ', '')
    list_str = []
    tmp_str = ''
    len_str = len(str_source)
    i = 0
    flag = True
    while i < len_str:
        if str_source[i] == '-':
            if i == 0:
                flag = False
            elif str_source[i-1] in ['+', '-', '*', '/', ')', '(']:
                flag = False
        if str_source[i] in ['+', '-', '*', '/', ')', '('] and flag:
            list_str.append(str_source[i])
            if i + 1 < len_str and str_source[i+1] == '(':
                flag = True
            else:
                flag = False
            i += 1
        elif not flag and str_source[i] == '-':
            tmp_str += str_source[i]
            flag = True
            i += 1
        elif str_source[i].isdigit():
            while i < len_str and str_source[i].isdigit():
                tmp_str += str_source[i]
                i += 1
            flag = True
            if len(tmp_str) > 0:
                list_str.append(tmp_str)
            tmp_str = ''
    print(list_str)
    return list_str


def operation_list(temp_list, sign1, sign2):
    len_list = len(temp_list) - 1
    j = 0
    while j < len_list:
        if temp_list[j] in [sign1, sign2]:
            tmp = calcs(float(temp_list[j - 1]), float(temp_list[j + 1]), temp_list[j])
            del temp_list[j + 1]
            del temp_list[j]
            temp_list[j - 1] = str(tmp)
            len_list -= 2
            j -= 1
        j += 1
    # print(temp_list)
    return temp_list


def calcs_list(source_list):
    tmp_list = [i for i in source_list]
    tmp_list = operation_list(tmp_list, '*', '/')
    tmp_list = operation_list(tmp_list, '+', '-')
    return tmp_list


source_str = '-3 + (-8 / 4 * 6  -16/2)'
print(source_str)
result_list = convert_str_to_list(source_str)
# print(calcs_list(result_list)[0])
