# Напишите генератор, который будет генерировать последовательность
# от start к end и наоборот если end меньше start
# Оберните генератор в декоратор, который будет пропускать только
# четные числа

from calendar import c
from datetime import datetime
from telnetlib import DO
from tkinter.messagebox import NO
from typing import Callable


def even_number_decorator(func: Callable):
    def wrapper(*args, **kwargs):
        for num in func(*args, **kwargs): # raise StopIteration
            if num % 2 == 0:
                yield num
    return wrapper

@even_number_decorator
def number_generator(start, end): # range(start, end, step)
    if start > end:
        step = -1
    else:
        step = 1
    while start != end + step:
        yield start
        start += step

# for num in number_generator(10, 1):
#     print(num)

def my_func(lst = ([],)[0]): # my_func.lst_default = ([],)
    lst.append(1)
    return lst

print(my_func())
print(my_func())

# ООП в Python

class Dog:

    def __init__(self, func, list=[]):
        self.name = func
        self.bark = lambda: print("new")
        self.breeds = list.copy()

    def bark(self): # self == this в других языках
        print("bark")

my_dog = Dog('name')
my_dog.bark()
my_dog.meow = 1
# print(my_dog.meow)
print(my_dog.breeds)
# print(dir(my_dog))
my_second_dog = Dog('name')
my_second_dog.breeds.append('new_breed')
print(my_dog.breeds) 
print(my_second_dog.breeds) # ['Retreever', 'new_breed']


# Наследование

class Animal:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("animal bark")

class Dog(Animal):
    breed: str
    new_attr: str | None = None

    def __init__(self, name):
        super().__init__(name)
        self.breed = "retreever"
        self.my_dog_func = lambda: print("my lambda")

    def bark(self):
        super().bark()
        print(f"{self.name} of {self.breed} barked")

    @staticmethod
    def static_bark():
        print("I'm static bark")

my_dog = Dog('name')
my_dog.bark()
my_dog.my_dog_func()
my_dog.static_bark()
Dog.static_bark()

def __my_func():
    print('print')

class Cat:
    def meaow(self):
        self.__make_sound()

    # def _make_sound(self): # Protected
    #     print("meaow")

    def __make_sound(self): # Private
        print("meaow")

class WhiteCat(Cat):
    def meaow(self):
        self._Cat__make_sound()

cat = WhiteCat()
cat.meaow()


# Dunder methods (__<название метода> __)

class Dog:

    def __str__(self):
        return 'this is a dog'

dog = Dog()
print(dog)
my_str = str(dog) # dog.__str__()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other): # Что будет при применении + 
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        elif isinstance(other, int):
            return Point(self.x + other, self.y + other)
        else:
            raise TypeError

    def __str__(self) -> str:
        return f"x: {self.x}, y: {self.y}"

point_1 = Point(1, 2)
point_2 = Point(2, 3)
point_3 = point_1 + point_2
print(point_3)

# __sub__ - минус
# __mul__ - умножить
# __truediv__ - деление


class MyList:

    def __init__(self, collection):
        self.collection = collection

    def __getitem__(self, index):
        return self.collection[index]

    def __setitem__(self, index, val):
        self.collection[index] = val

lst = MyList([1, 2, 3])
lst[1] = 100
print(lst[1])
