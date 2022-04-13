# Модуль ввода
<<<<<<< HEAD
from module_output import demo_mod as demo
from module_output import do_mod as do


def do_mod(count):
    if not count:
        demo()


board_list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
do_mod(0)
do(board_list)
=======
def do_mod():
    print('Ваш ход')
    print('Введите координаты ячейки разделенные запятой (1,3)')
    cell_coord = input('> ')
    print()
    return cell_coord


def conversion_input(cell_str):
    cell = cell_str.strip().replace(' ', '').replace('(', '').replace(')', '').split(',')
    return cell


def is_input_digit(cell_str):
    cell = conversion_input(cell_str)
    if cell is not None and 0 < len(cell) < 3:
        if cell[0].isdigit() and cell[1].isdigit():
            return True
    return False


def is_correct_coordinates(cell_str):
    if is_input_digit(cell_str):
        cell = conversion_input(cell_str)
        row = int(cell[0])
        column = int(cell[1])
        if 0 < row < 4 and 0 < column < 4:
            if row == 1:
                return (row+ column) - 2
            elif row == 2:
                return row + column
            elif row == 3:
                return (row + column) + 2
    return None


def selection_symbol():
    while True:
        symbol = input('Выберите символ Х или 0 > ')
        if symbol.lower() in ['0', 'x']:
            return symbol
        print(f'Неверный ввод {symbol}')
>>>>>>> 48114de165bc6badf5011a937fb1386978a904a3
