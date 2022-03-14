from alg_test import create_int_array, convert_array_to_string, selection_sort, fact, quicksort

new_arr = create_int_array(20, -100, 100)
str_arr = convert_array_to_string(new_arr)
sort_arr = selection_sort(new_arr)
print(str_arr + '\n')
str_arr = convert_array_to_string(sort_arr)
print(str_arr)
for i in range(1, 10):
    print(fact(i))

print(quicksort([10, 5, 2, 3, 12, 0]))
