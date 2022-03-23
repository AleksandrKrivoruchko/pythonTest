# Задать список из n чисел последовательности (1 + 1 / n)**n
# и вывести на экран их сумму
n = int(input('Введите n: '))
list_result = []
sum_list = 0
for i in range(1,n + 1):
    x = (1 + 1 / i)**i
    list_result.append(x)
    sum_list += x
print(list_result)
print(sum_list)
