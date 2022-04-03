# Даны два файла в каждом из которых находится запись многочлена.
# Сформировать файл содержащий сумму многочленов.
def string_analysis(source_str):
    temp_list = source_str.replace(' = 0\n', '').split(' + ')
    temp_dict = {}
    dict_value = None
    # print(temp_list)
    for str_item in temp_list:
        i = 0
        flag = True
        dict_key = None
        while i < len(str_item):
            if str_item[i].isdigit():
                if flag:
                    i, dict_value = convert_number(i, str_item)
                    flag = False
            elif str_item[i] == 'x':
                if i + 1 < len(str_item) and str_item[i + 1] == '^':
                    i += 2
                    i, dict_key = convert_number(i, str_item)
                else:
                    i += 1
                    dict_key = 1
            elif str_item[i] == '*':
                i += 1
        if dict_key is None:
            dict_key = 0
        temp_dict[dict_key] = dict_value
    return temp_dict


def convert_number(j, str_item):
    temp_str = ''
    while j < len(str_item) and str_item[j].isdigit():
        temp_str += str_item[j]
        j += 1
    return j, int(temp_str)


def sum_dict(dict_more, dict_less):
    dict_res = {}
    for dict_key in dict_more:
        if dict_key in dict_less:
            dict_res[dict_key] = dict_more[dict_key] + dict_less[dict_key]
        else:
            dict_res[dict_key] = dict_more[dict_key]
    return dict_res


def creating_polynomial(course_dict):
    result_str = ''
    for item in course_dict:
        if item == 0:
            result_str += f'{course_dict[item]} = 0'
        elif item == 1:
            result_str += f'{course_dict[item]}*x + '
        else:
            result_str += f'{course_dict[item]}*x^{item} + '
    return result_str


file_descriptor = open('polynomial.txt', 'r')
first_line = file_descriptor.readline()
second_line = file_descriptor.readline()
file_descriptor.close()
print(first_line.replace('\n',''))
print(second_line.replace('\n',''))
dict1 = string_analysis(first_line)
dict2 = string_analysis(second_line)
# print(dict1)
# print(dict2)
if len(dict2) > len(dict1):
    dict_result = sum_dict(dict2, dict1)
else:
    dict_result = sum_dict(dict1, dict2)
# print(dict_result)
str_dict = creating_polynomial(dict_result)
print(str_dict)
