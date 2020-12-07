import requests, re


# # python3.6+的规范
#
# # def fun(参数: 类型) -> 返回值类型:
# #     print(num)
#
#
# # def fun(num: list) -> list:
# #     return num
# #
# #
# # print(fun([1, 2, 3]))
#
# # import requests
# #
# #
# # def getRequestValue(url: str, params: dict) -> str:
# #     response = requests.get(url=url, params=params)
# #     return f'{response.json()}'
#
#
# def test(a):
#     a1 = list(a)
#     b1 = a1[::-1]
#     if a1 == b1:
#         return True
#     else:
#         return False
#
#
# print(test('31213'))
#

# def generate_new_list(*args):
#     # args传入的是一个元组
#     list1 = [i for i in args]
#     return list1
#
#
# print(generate_new_list(1, 2, 3, 4))


# 装饰器
# def use_logging(level):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             if level == 'warn':
#                 print('%s is running' % func.__name__)
#             return func(*args)
#
#         return wrapper
#
#     return decorator
#
#
# @use_logging(level='warn')
# def bar():
#     print('i am bar')
#
#
# bar()

# lambda表达式格式：lambda 参数: 返回值
# f = lambda x, y: x ** 2 + y ** 2
# print(f(3, 4)


# **kwargs传入的是一个字典
def fun(context, **kwargs) -> str:
    print(context, kwargs.get('name'))


fun('1', name='Tom')

# 装饰器的意义：将目标函数<被装饰的函数>当成参数传入到装饰器里面
list1 = [1, '2', 35, 6, 6, 7]
list1 = ['1', '2']
for i in list1:
    data = ''.join(list1)
print(data)

st = '123'
tu = (1, 2, 3)
print(str(tu))
