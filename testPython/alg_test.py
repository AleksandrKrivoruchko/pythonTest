from random import randint


# Алгоритм бинарного поиска в упорядоченном списке
def binary_search(list1, item):
    low = 0
    high = len(list1) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list1[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


# Создание списка заполненого случайными целыми числами
def create_int_array(array_len, min_range, max_range):
    new_array = []
    for i in range(array_len):
        new_array.append(randint(min_range, max_range))
    return new_array


# Конвертация списка в строку
def convert_array_to_string(source_array):
    array_str = ''
    k = 0
    for i in range(len(source_array)):
        if i < len(source_array) - 1:
            array_str += str(source_array[i]) + '\t'
        else:
            array_str += str(source_array[i])
        k += 1
        if k == 10:
            array_str += '\n'
            k = 0
    return array_str


# Поиск минимального числа в списке
def find_minimum(arr):
    min_index = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[min_index]:
            min_index = i
    return min_index


# Сортировка списка выбором
def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        min_index = find_minimum(arr)
        new_arr.append(arr.pop(min_index))
    return new_arr


# Быстрая сортировка
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = [array[0]]
        less = [i for i in array[1:] if i <= pivot[0]]
        greater = [i for i in array[1:] if i > pivot[0]]
        return quicksort(less) + pivot + quicksort(greater)


# Функция вычисляющая факториал
def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


# my_list = [1, 3, 5, 7, 9]
# print(binary_search(my_list, 7))
# print(binary_search(my_list, -1))
# create_arr = create_int_array(100, -100, 100)
# # print(create_arr)
# str_arr = convert_array_to_string(create_arr)
# print(str_arr)
# sort_arr = selection_sort(create_arr)
# str_arr = convert_array_to_string(sort_arr)
# print(str_arr)
