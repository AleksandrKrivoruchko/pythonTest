def rhomb(width, height, symbol):
    x_middle = width//2 + 1
    y_middle = height//2 + 1
    str_rhomb = ''
    position_x = 0
    for i in range(1,height +1):
        for j in range(1, width + 1):
            if x_middle + position_x == j or x_middle - position_x == j:
                str_rhomb += symbol
            else:
                str_rhomb += ' '
        str_rhomb += '\n'
        if i < y_middle:
            position_x += 1
        else:
            position_x -= 1
    return str_rhomb


x = int(input("Введите ширину: "))
#y = int(input("Введите высота: "))
str_rhomb = rhomb(x, x, '*')
print(str_rhomb)