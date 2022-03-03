from random import randint
# a = float(input('Введите первое число: '))
# b = float(input('Введите второе число: '))
# print(a, ' + ', b, ' = ', a + b)
# print('{} -- {}'.format(a, b))

# a, b, c = 1, 4, 5
# print(a,b,c)
# myRange = []
#line = ""
# for i in range(5):
#     line = ''
#     for j in range(5):
#         line += '*'
#     print(line)
# for k in range(1, 10, 2):
#     print(k)

original = int(input('Введите чило: '))
inverted = 0
while original:
    inverted = inverted * 10 + original % 10
    original //= 10
# else:
#     print('Пожалуй хватит!')
print(inverted)

numbers = list(range(1, 10, 2))
numbers1 = []
# print(numbers)
for i in numbers:
    numbers1.append(i * 2)
    # print(i)
print(numbers)
print(numbers1)
# print(type(numbers1))
titleTab = '\t'
for k in range(1, 10):
    titleTab += str(k) + '\t'
print(titleTab + '\n')
for i in range(1, 10):
    if i < 10:
        numbers2 = str(i) + '\t'
    else:
        numbers2 = str(i) + '  '
    for j in range(1, 10):
        numbers2 += str(i * j) + '\t'
        # print(randint(0,1),)
    print(numbers2 + '\n')
# print(type(numbers2))
