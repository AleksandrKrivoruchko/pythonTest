# Реализовать алгоритм задания случайных чисел
# Без использования встроенного генератора псевдослучайных чисел
import time

def rnd_gen(value_set):
    a = 45
    c = 21
    m = 67
    value_set = (a * value_set + c) % m
    return value_set


def rnd_func(n):
    set_value = time.time() % 10
    print(set_value)
    tmp_list = [rnd_gen(set_value)]
    for i in range(n):
        tmp_list.append(rnd_gen(tmp_list[i]))
    # print(tmp_list)
    tmp_list1 = [x - int(x) for x in tmp_list]
    # print(tmp_list1)
    return [round(i) for i in tmp_list]


for i in range(100):
    rnd_list = rnd_func(20)
    print(rnd_list)
