# Работа с файлами
import sys
file_index = open('file_test.py', 'r')
file_value = file_index.readlines()
for item in file_value:
    print(item)

# print(file_value)
# res_split = file_value.split()
# print(res_split)

sys.stdout.write('Вывод с помощью потока вывода\n')
value_in = sys.stdin.readline()
print(value_in)
