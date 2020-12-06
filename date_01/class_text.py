from date_01.log import logger

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


def remove(list_exmple=[], value=None, index=-1):
    print(value, index)
    if len(list_exmple) > index and value == None:
        list_exmple.pop(index)
    elif value:
        list_exmple.remove(value)
    else:
        return None


# list_exmple = [1, 2, 3, 4, 5]
# remove(list_exmple)
# print(list_exmple)


# 类方法 使用 cls.方法()调用或者实例对象.方法()
# 静态方法 不能直接使用类中的任何属性和方法，使用类名.静态方法()
class Teacher:

    @classmethod
    def run(cls):
        print('running')

    # 静态方法
    @staticmethod
    def sleep():
        print('sleep')


try:
    raise IOError
except IOError:
    logger.exception('record this error')
    logger.warning(''.center(50, '-'))
