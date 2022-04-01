# Работа с файлами
# import sys
file_index = open('file_test.py', 'r')
file_value = file_index.read()

print(file_value)

positions = input('Введите индексы элементов в списке через пробел > ').strip().split()
print(positions)
file_positions = open('index_positions.txt', 'w')
file_positions.writelines([string + '\n' for string in positions])
file_positions.close()
# res_split = file_value.split()
# print(res_split)

# sys.stdout.write('Вывод с помощью потока вывода\n')
# value_in = sys.stdin.readline()
# print(value_in)
