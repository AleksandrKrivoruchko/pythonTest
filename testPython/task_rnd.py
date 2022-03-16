# Генерированние псевдослучайных чисел
# Линейный конгруэнтный метод r1 = mod(k * r0 + b, M)
# M - модуль(0<M), k - множитель(0<=k<M), b - приращение(0<=b<M), r0 - начальное значение(0<=r0<M)
def my_rnd(n_count):
    m = 2 ^ 31 - 1
    k = 33
    b = 7
    r0 = n_count
    rnd_number = (k * n_count + b) // m
    return rnd_number


result_list = []
temp = my_rnd(7)
for i in range(50):
    temp = my_rnd(temp)
    result_list.append(temp)
print(result_list)
list1 = []
