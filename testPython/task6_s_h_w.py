# Красный, синий и желтый называются основными цветами,
# потому что их нельзя получить путем смешения других цветов.
# При смешивании двух основных цветов получается вторичный цвет:
# если смешать красный и синий, то получится фиолетовый;
# если смешать красный и желтый, то получится оранжевый;
# если смешать синий и желтый, то получится зеленый.
# Напишите программу, которая считывает названия двух основных цветов для смешивания.
# Если пользователь вводит что-нибудь помимо названий «красный», «синий» или «желтый»,
# то программа должна вывести сообщение об ошибке. В противном случае программа должна
# вывести название вторичного цвета, который получится в результате
color1 = input('Введите один из трёх цветов (красный, синий, желтый): ')
color2 = input('Введите второй из трёх цветов (красный, синий, желтый): ')
if color1 == 'красный' or color2 == 'красный':
    color_red = 1
else:
    color_red = 0
if color1 == 'синий' or color2 == 'синий':
    color_blue = 3
else:
    color_blue = 0
if color1 == 'желтый' or color2 == 'желтый':
    color_yellow = 7
else:
    color_yellow = 0

color_mix = color_red + color_blue + color_yellow
if color_mix == 4:
    print('Если смешать {} и {} то получится фиолетовый.'.format(color1, color2))
elif color_mix == 8:
    print('если смешать {} и {}, то получится оранжевый.'.format(color1, color2))
elif color_mix == 10:
    print('если смешать {} и {}, то получится зеленый.'.format(color1, color2))
else:
    print('Вы ошиблись при вводе цвета!')