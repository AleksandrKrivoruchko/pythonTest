# На вход программе подается натуральное число n.
# Напишите программу, которая для каждого из чисел от 0 до n
# (включительно) выводит фразу: «Квадрат числа [число] равен [число]» (без кавычек).
n = int(input('Введите число n: '))
for i in range(n + 1):
    print('Квадрат чила {} равен {}'.format(i, i * i))
