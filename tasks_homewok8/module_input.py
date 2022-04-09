# Модуль ввода
from module_output import demo_mod as demo
from module_output import do_mod as do


def do_mod(count):
    if not count:
        demo()


board_list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
do_mod(0)
do(board_list)
