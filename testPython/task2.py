def triangle(x):
    start = x//2 + 1
    end = start
    symbol = '*'
    transfer = '\n'
    str_triangle = ''
    while start:
        str_triangle += symbol_print(0, start, ' ')
        str_triangle += symbol
        str_triangle += symbol_print(start, end, symbol)
        str_triangle += transfer
        start -= 1
        end += 1
    return str_triangle

def symbol_print(count, end_space, symbol):
    str_temp = ''
    while count < end_space:
        str_temp += symbol
        count +=1
    return str_temp


while 1:
    len1 = int(input("Введите число (чтобы выйти введите 0)\n"))
    if not len1:
        break
    str1 = triangle(len1)
    print(str1)
