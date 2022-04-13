import time

from alg_test import create_int_array, convert_array_to_string, selection_sort, fact, quicksort, separation_fractional_part
from urllib.request import urlopen
from bs4 import BeautifulSoup
new_arr = create_int_array(20, -100, 100)
str_arr = convert_array_to_string(new_arr)
sort_arr = selection_sort(new_arr)
print(str_arr + '\n')
str_arr = convert_array_to_string(sort_arr)
print(str_arr)
for i in range(1, 10):
    print(fact(i))

print(quicksort([10, 5, 2, 3, 12, 0]))
number = float(input('Input float number: '))
fractional_part = separation_fractional_part(number)
result = fractional_part * 10 - separation_fractional_part(fractional_part * 10)
print(int(result))
html = urlopen('http://pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(), 'html.parser')
name_list = bs.find_all('span', {'class':'green'})
for name in name_list:
    print(name.get_text())

x = [time.time() % 10]
for i in range(10):
    x_tmp = (7 * x[i] + 10) % 19
    x.append(round(x_tmp, 2))
print(x)
