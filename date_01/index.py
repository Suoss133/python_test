array = [2, 8, 1, 5]
# arr1 = array[0]
# arr2 = array[1]
# array[0] = arr2
# array[1] = arr1
# print(array)


# lists = []
# for i in range(len(array)):
#     min_num = array.index(min(array))
#     lists1 = array.pop(min_num)
#     lists.append(lists1)
# print(lists)

# for i in range(1,10):
#     for j in range(1,10):
#         if i >= j:
#             print(f'{j}*{i}={i * j}', end=' ')
#     print('\n')

lists = [(str(j) + '*' + str(i) + '=' + str(i * j)) for i in range(1, 10)
                                                    for j in range(1, i + 1)]
print(lists)
