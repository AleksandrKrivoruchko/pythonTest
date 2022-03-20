# Дано пятизначное или шестизначное натуральное число.
# Напишите программу, которая изменит порядок его последних пяти цифр на обратный.
def revers_digits(number, n):
    count = count_digits(number)
    result = 0
    i = 1
    if count > n:
        source_number = number // power(n)
        temp = number % power(n)
        while temp > 10:
            result += temp % 10 * power(n - i)
            temp //= 10
            i += 1
        return source_number * power(n) + result + temp % 10
    else:
        temp = number
        while temp > 10:
            result += temp % 10 * power(count - i)
            temp //= 10
            i += 1
        return result + temp % 10


def power(n):
    result_power = 1
    for i in range(n):
        result_power *= 10
    return result_power


def count_digits(number):
    temp = number
    count = 0
    while temp:
        temp //= 10
        count += 1
    return count


number = input('Введите число: ')
number1 = int(number)
print(revers_digits(number1, 5))
if len(number) > 5:
    tmp = number[-5:]
    result_str = number[:-5] + tmp[::-1]
else:
    result_str = number[::-1]
print('Второй вариант {}'.format(result_str))
