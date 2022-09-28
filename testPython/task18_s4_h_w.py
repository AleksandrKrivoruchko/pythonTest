# Задать список из N элементов заполненных числами из [-N, N].
# Найти произведение элементов на указанных позициях.
# Позиции хранятся в файле в одной строке одно число.
import random


def create_list(n):
    return [random.randint(-n, n) for i in range(n)]


count_elements = int(input('Введите количество элементов N > '))
file_indexes = open('index_positions.txt', 'r')
indexes = [int(number) for number in file_indexes]
file_indexes.close()
test_list = create_list(count_elements)
product = 1
for i in indexes:
    if i < len(test_list):
        product *= test_list[i]

print('Произведение элементов на указанных позициях равно {}'.format(product))
print('Список позиций элементов для произведения')
print(indexes)
print('Список из {0} элементов заполненный числами [-{0}, {0}]'.format(count_elements))
print(test_list)
