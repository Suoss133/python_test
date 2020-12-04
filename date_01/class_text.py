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

# a = Animal()
# a.age = 12
# print(a.age)


# 类装饰器
class Foo(object):
    def __init__(self,func):
        self.func = func

    def __call__(self,*args,**kwargs):
        print('class decorator running')
        self.func()
        print('class decorator ending')


@Foo
def bar():
    print('i am bar')


bar()
