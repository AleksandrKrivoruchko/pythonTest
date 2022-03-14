# Сформировать список из N членов последовательности
# Для N=5: 1, -3, 9, -27, 81 и т. д.
number_of_elements = int(input("Введите количество членов последовательности: "))
sequence = [1]
for i in range(number_of_elements - 1):
    sequence.append(sequence[i] * -3)
print(sequence)
