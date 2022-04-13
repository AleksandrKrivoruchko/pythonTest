# Реализовать алгоритм перемешивания списка
import random

test_list1 = [i for i in range(1, 16)]
print(test_list1)
test_list = [test_list1[i] for i in range(len(test_list1))]
while test_list[0] == test_list1[0]:
    for k in range(random.randint(10, 100)):
        mixing_list = [random.randint(0, len(test_list) - 1) for j in range(len(test_list))]
        # print(mixing_list)
        length = len(mixing_list) // 2
        for i in range(length):
            test_list[i], test_list[-i] = test_list[-i], test_list[i]
            test_list = test_list[i:] + test_list[:i]

print(test_list)
