# Пользователь задаёт две строки.
# Определить количество вхождений одной строки в другой.
def is_string_in_string(str_source, str_search):
    len_source = len(str_source)
    len_search = len(str_search)
    i = 0
    j = 0
    count = 0
    while i < len_source - len_search + 1:
        if str_search[j] == str_source[i]:
            while j < len_search and str_search[j] == str_source[i]:
                i += 1
                j += 1
            if j == len_search:
                count += 1
            j = 0
        else:
            i += 1
    return count


str1 = input('Введите исходную строку: ')
str2 = input('Введите искомую строку: ')
if len(str2) > len(str1):
    temp = str1
    str1 = str2
    str2 = temp
count_result = is_string_in_string(str1, str2)
if 1 < count_result % 10 < 5 and (count_result < 10 or count_result > 20):
    insert_str = 'раза'
else:
    insert_str = 'раз'
print(f' Строка {str2} входит в строку {str1} {count_result} {insert_str}')
