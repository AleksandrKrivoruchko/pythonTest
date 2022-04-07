import module_output as f_out
import module_input as f_in
import module_data as f_data
board_list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
f_out.demo_mod()

cell_player = f_in.do_mod()
index_list = f_in.is_correct_coordinates(cell_player)
if index_list is not None:
    f_data.filling_list(board_list, index_list, 'X')
    f_out.do_mod(board_list)
else:
    print(f'Неверный ввод {cell_player}')
