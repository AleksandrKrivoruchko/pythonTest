# Генерированние псевдослучайных чисел
# Линейный конгруэнтный метод r1 = mod(k * r0 + b, M)
# M - модуль(0<M), k - множитель(0<=k<M), b - приращение(0<=b<M), r0 - начальное значение(0<=r0<M)
import time


def my_rnd(n_count):
    m = 2 ^ 31 - 1
    k = 33
    b = 7
    r0 = n_count
    rnd_number = (k * n_count + b) // m
    return rnd_number


# Реализация алгоритма Лемера
# x(i) = a * x(i - 1) mod m
def lehmer_rng(num_previous):
    a = 16807
    m = 21474
    q = 73
    r = 2836
    hi = num_previous // q
    lo = num_previous % q
    num_previous = (a * lo) - (r * hi)
    if num_previous <= 0:
        num_previous = num_previous + m
    return num_previous / m


result_list = []
temp = my_rnd(21)
for i in range(10):
    temp = my_rnd(temp)
    result_list.append(temp)
print(result_list)
list1 = []
hi_l = 10
lo_l = 0
x = lehmer_rng(1)
for i in range(10):
    x = lehmer_rng(x)
    ri = round((hi_l - lo_l) * x + lo_l, 2)
    list1.append(ri)
print(list1)
print(time.time())
