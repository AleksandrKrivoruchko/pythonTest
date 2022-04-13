# Дан список чисел. Создать список в который попадают числа,
# описывающие возрастающую последовательность, и содержащий максимальное количество элементов
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
#         [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
# Порядок элементов менять нельзя

# Формирует список списков, полученных при помощи new_list
def analysis_list(lst_in):
    return [new_list(lst_in[i:]) for i in range(len(lst_in)-1)]


# Возвращает True, если элемент меньше элементов следующих за ним
# в исходном списке и он больше последнего элемента в формируемом списке
# Аргументы: list_in - исходный список,
#            el_list_out - последний элемент формирующегося списка
#            index - индекс проверяемого элемента
def whether_add_el(list_in, el_list_out, index):
    for i in range(index, len(list_in)):
        if el_list_out >= list_in[i]:
            continue
        elif list_in[index] > list_in[i]:
            return False
    return True


# Функция формирует список возрастающих элементов из исходного списка.
# Порядок следования элементов не меняется.
# Использует функцию whether_add_el
def new_list(list_in):
    list_out = []
    for i in range(len(list_in)):
        if len(list_out) == 0 and list_in[i] < list_in[i+1]:
            list_out.append(list_in[i])
        elif len(list_out) > 0 and list_in[i] > list_out[-1] and whether_add_el(list_in, list_out[-1], i):
            list_out.append(list_in[i])
    return list_out


lst = [1, 5, 2, 3, 4, 6, 1, 7]
lst_1 = [5, 2, 3, 4, 6, 1, 7, 3, 8, 2, 4, 9, 10, 1, 6, 2, 3, 4, 5, 6, 7, 8, 9, 10, 7, 8, 11]
lst_2 = [5, 2, 3, 4, 6, 1, 7]

lst_res = analysis_list(lst_1)
index_max = 0
for i, item in enumerate(lst_res):
    if len(item) > len(lst_res[index_max]):
        index_max = i
    # print(item)
print(lst)
print(new_list(lst), '\n')
print(lst_2)
print(new_list(lst_2), '\n')
print(lst_1)
print(lst_res[index_max])
