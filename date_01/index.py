from random import randint

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

# from collections import OrderedDict
#
# dit = OrderedDict({'name': 'Tom', 'age': 12})
# print(dit)
# print(type(dit))
# print(dit[0])
# print(dit.popitem())

# str ='python \njava'
# print(str)
# lists = str.split('\n')
# str = ' '.join(lists)
# print(str)

# from copy import copy
#
#
# class HaunteBus:
#     def __init__(self, passengers=None):
#         # 解决函数的参数是引用的问题
#         if passengers == None:
#             self.passengers = []
#         else:
#             # 创建外部参数的副本，不影响外部的引用
#             self.passengers = copy(passengers)
#
#     def pick(self, name):
#         self.passengers.append(name)
#
#     def drop(self, name):
#         self.passengers.remove(name)


# bus1 = HaunteBus(['Alice', 'Bill'])
#
# bus1.pick('Charlie')
# bus1.drop('Alice')
# print('bus1 ->', bus1.passengers)
#
# bus2 = HaunteBus()
# bus2.pick('Carrie')
# print('bus2 ->', bus2.passengers)
#
# bus3 = HaunteBus()
# print('bus3 ->', bus3.passengers)

# bus = ['Alice', 'Bill', 'Pat']
# bus1 = HaunteBus(bus)
# bus1.drop('Pat')
# print(bus1.passengers)
# print(bus)

import weakref


# class Cheese:
#     def __init__(self, kind):
#         self.kind = kind
#
#     def __repr__(self):
#         return 'Cheese(%r)' % self.kind
#
#
# stock = weakref.WeakValueDictionary()
# catalog = [Cheese('Rea Leicester'), Cheese('Tilist'),
#            Cheese('Brie'), Cheese('Parmesan')]
# for cheese in catalog:
#     stock[cheese.kind] = cheese
#
# print(sorted(stock.keys()))
# del cheese
# print(sorted(stock.keys()))

# import copy
#
# t1 = (1, 2, 3)
# t2 = copy.copy(t1)
# print(t1 == t2)
# print(t1 is t2)
#
# t1 = [1, 2, 3]
# t2 = copy.copy(t1)
# print(t1 == t2)
# print(t1 is t2)


# def ge_123(end):
#     start = 0
#     while start < end:
#         x = yield start
#         print(x,'yield')
#         start += 1
# m = ge_123(5)
# print(next(m))
# print(next(m))
# print(next(m))
# print(m.send(10))

# def g(x):
#     yield from range(x, 0, -1)
#     yield from range(x)
# print(list(g(5)))


# a = 10
# b = 1
# try:
#     c = b / a
#     print(c)
# except Exception:
#     print('错误')
# else:
#     print('没有错，我才执行。。。else')
# finally:
#     print('没有有错我都执行')


# class Query(object):
#
#     def __init__(self, name):
#         self.name = name
#
#     def __enter__(self):
#         print('Begin')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type:
#             print('Error')
#         else:
#             print('End')
#
#     def query(self):
#         print(f'Query info {self.name}')
#
#
# with Query('Bod') as q:
#     q.query()


def simple(a):
    print('-> Started:a = ',a)
    b = yield a
    print('-> Received:b = ',b)
    c = yield a + b
    print('-> Received:c = ', c)

try:
    my_coro = simple(12)
    next(my_coro)
    my_coro.send(28)
    my_coro.send(99)
except StopIteration:
    print('结束')

