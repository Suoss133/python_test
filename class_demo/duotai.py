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
