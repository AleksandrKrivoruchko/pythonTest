# Модуль для вывода
# print('0 | X | 0')
# print('---------')
# print('X | 0 | X')
# print('---------')
# print('0 | X | 0')
def do_mod(board_list):
    print(f'{board_list[0]} | {board_list[1]} | {board_list[2]}')
    print('---------')
    print(f'{board_list[3]} | {board_list[4]} | {board_list[5]}')
    print('---------')
    print(f'{board_list[6]} | {board_list[7]} | {board_list[8]}')
    print()
    return board_list


def demo_mod():
    print('''\033[32m                            Игра <<Крестики-нолики>>                       
    1   2   3           Введено X (1, 3)        Введено 0 (3, 1)
1   0 | X | 0             |   | X                 |   |
    ---------           ---------               ---------
2   0 | X | X             |   |                   |   |
    ---------           ---------               ---------
3   X | X | 0             |   |                 0 |   |''')
    print('\n')
