array = [2, 8, 1, 5]
# arr1 = array[0]
# arr2 = array[1]
# array[0] = arr2
# array[1] = arr1
# print(array)


lists = []
for i in range(len(array)):
    min_num = array.index(min(array))
    lists1 = array.pop(min_num)
    lists.append(lists1)
print(lists)














