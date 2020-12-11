from date_01.log import logger
from dis import dis
import time
import functools
from functools import singledispatch
import numbers

# class Student():
#     def __init__(self, name, age):
#         self.name = name
#         self._age = age
#
#
#     def __str__(self):
#         return '姓名:' + self.name + '\n年龄:' + str(self._age)
#
#     def get_age(self):
#         return self._age
# stu = Student('张三',12)
# print(stu)

# self表示当前实例化对象，cls表示类

"""多态"""


class Animal(object):

    def __init__(self, age):
        self._age = age

    def run(self):
        print("Animal is running...")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value


class Dog(Animal):
    def run(self):
        print("Dog is running...")


class Cat(Animal):
    def run(self):
        print("Cat is running...")


def run_twice(animal):
    animal.run()
    animal.run()


# run_twice(Animal())
# run_twice(Dog())


# a = Animal()
# a.age = 12
# print(a.age)


# 类装饰器
# class Foo(object):
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         print('class decorator running')
#         self.func()
#         print('class decorator ending')
#
#
# @Foo
# def bar():
#     print('i am bar')
#
#
# bar()


# def remove(list_exmple=[], value=None, index=-1):
#     print(value, index)
#     if len(list_exmple) > index and value == None:
#         list_exmple.pop(index)
#     elif value:
#         list_exmple.remove(value)
#     else:
#         return None

# list_exmple = [1, 2, 3, 4, 5]
# remove(list_exmple)
# print(list_exmple)


# 类方法 使用 cls.方法()调用或者实例对象.方法()
# 静态方法 不能直接使用类中的任何属性和方法，使用类名.静态方法()
# class Teacher:
#
#     @classmethod
#     def run(cls):
#         print('running')
#
#     # 静态方法
#     @staticmethod
#     def sleep():
#         print('sleep')
#
#
# try:
#     raise IOError
# except IOError:
#     logger.exception('record this error')
#     logger.warning(''.center(50, '-'))

# 装饰器

# registry = []
#
#
# def register(func):
#     print('running register(%s)' % func.__name__)
#     registry.append(func)
#     return func
#
#
# @register
# def f1():
#     print('running f1()')
#
#
# @register
# def f2():
#     print('running f2()')
#
#
# def f3():
#     print('running f3()')
#
#
# def main():
#     print('running main()')
#     print('registry ->', registry)
#     f3()
#     f2()
#     f1()
#
#
# if __name__ == '__main__':
#     main()

# @functools.lru_cache()缓存装饰器

def clock(func):
    @functools.wraps(func)
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ','.join(repr(arg) for arg in args)
        print('[%0.8fs]%s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result

    return clocked


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


# @functools.lru_cache()
# @clock
# def fibonacci(n):
#     if n < 2:
#         return n
#     return fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == '__main__':
    print(factorial.__name__)
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6! =', factorial(6))
    print(factorial(6))

# @singledispatch泛型函数，由参数决定调用那些方法

# @singledispatch
# def sort_type(obj):
#     print(obj, type(obj), 'obj')
#
#
# @sort_type.register(str)
# def _(text):
#     print(text, type(text), 'str')
#
#
# @sort_type.register(numbers.Integral)
# def _(n):
#     print(n, type(n), 'int')
#
#
# @sort_type.register(list)
# def _(list):
#     print(list, type(list), 'list')
#
#
# sort_type('aaa')
# sort_type(123)
# sort_type(list)
# sort_type(tuple)
# sort_type([1, 2, 3])
