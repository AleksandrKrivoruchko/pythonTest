# Работа с файлами
file_index = open('file_test.py', 'r')
file_value = file_index.read()
print(type(file_value))
print(file_value)
res_split = file_value.split()
print(res_split)
