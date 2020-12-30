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
