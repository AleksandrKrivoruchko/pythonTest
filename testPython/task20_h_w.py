# Написать программу получающую набор произведений от 1 до N
# Пример: пусть N = 4, тогда [1, 2, 6, 24]
input_str = input('Введите число N: ')
if input_str.isdigit():
    n = int(input_str)
    result_list = [1]
    for i in range(2, n + 1):
        result_list.append(result_list[i-2] * i)
    print(result_list)
else:
    print(f'Некорректное значение N {input_str}')
