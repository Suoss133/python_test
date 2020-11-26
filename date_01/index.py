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

list1 = [1, 2, 1, 2, 3, 1, 3, 4, 5, 1, 4, 5, 1]

# 方式一
for i in list1.copy():
    while i == 1:
        list1.remove(1)
        break
print(list1)

# 方式二
# for i in list1.copy():
#     if i < 2:
#         list1.remove(1)
# print(list1)
# # 方式二
# while i in list1:
#     if i == 1:
#         list1.remove(1)
# print()
# 方式三

float_num = 33.4444444
print('{:.2f}'.format(float_num))
print(f'{float_num:.3f}')