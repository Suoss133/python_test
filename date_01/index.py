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
#
# lists = [(str(j) + '*' + str(i) + '=' + str(i * j)) for i in range(1, 10)
#          for j in range(1, i + 1)]
# print(lists)
#
# list1 = [1, 2, 1, 2, 3, 1, 3, 4, 5, 1, 4, 5, 1]

# 方式一
# for i in list1.copy():
#     while i == 1:
#         list1.remove(1)
#         break
# print(list1)

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
# print(False or True)
# print(True and True)
# print(False and False)
#
# d = {'Name': 'Kate', 'No': '1001', 'Age': '20'}
# print(len(d))

# num = 66
# flag = True
# while flag:
#     input_num = int(input('输入猜测的数字:'))
#     if num < input_num:
#         print('猜大了')
#     elif num > input_num:
#         print('猜小了')
#     else:
#         print('正确')
#         flag = False


# count = 3
# while count:
#     input_access = str(input("输入用户名:"))
#     input_password = str(input("输入密码:"))
#     if input_access != '张三' and input_password != '123456':
#         count = count - 1
#         print(f'剩余次数:{count}' )


# input_num = int(input('输入数字:'))
# if input_num == 1 or input_num == 0:
#     print('1和0即非素数也非合数')
# else :
#     print('是素数')

from collections import OrderedDict

dit = OrderedDict({'name': 'Tom', 'age': 12})
print(dit)
print(type(dit))
print(dit[0])
print(dit.popitem())
