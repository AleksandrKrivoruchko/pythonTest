# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random


def creating_polynomial(ratio):
    coefficients = [random.randint(0, 100) for i in range(ratio + 1)]
    temp_ratio = ratio
    result_str = ''
    for j in range(len(coefficients)):
        if temp_ratio == 0:
            result_str += f'{coefficients[j]} = 0'
        elif temp_ratio == 1:
            result_str += f'{coefficients[j]}*x + '
        else:
            if coefficients[j] == 0:
                continue
            elif coefficients[j] == 1:
                result_str += f'x^{temp_ratio} + '
            else:
                result_str += f'{coefficients[j]}*x^{temp_ratio} + '
        temp_ratio -= 1
    return result_str


coff = random.randint(1, 5)
temp_str = creating_polynomial(coff)
print(temp_str)
file_descriptor = open('polynomial.txt', 'a')
file_descriptor.write(temp_str + '\n')
file_descriptor.close()
