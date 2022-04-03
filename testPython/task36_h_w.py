def is_element(i1, i2, i3):
    if (i1 + i2) == i3:
        return True
    return False


list1 = [1, 5, 2, 3, 4, 6, 1, 7]
list2 = []
i = 0
flag = True
while i < len(list1) - 2:
    if list1[i] < list1[i + 1]:
        for el2 in list1[i+2:]:
            for el1 in list1[i+1: -1]:
                if is_element(list1[i], el1, el2) and flag:
                    list2.append(list1[i])
                    list2.append(el1)
                    list2.append(el2)
                    flag = False
                elif is_element(list1[i], el1, el2):
                    list2.append(el2)
    i += 1
print(list2)
