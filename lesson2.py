# Tuples

from ast import arg
from typing import Callable
from re import X
from tkinter.messagebox import NO
from typing import List


my_tuple = (1, 2, 3)
my_tuple_2 = (1,) # tuple с одним элементом
my_list = [1]

# set
# set - неупорядаоченная коллекция уникальных элементов

my_set = {1, 2, 3, 4, 5, 5, 5, 5}
my_second_set = {"first_str", "second_str", 1, "53", "third", 3.14}
# print(my_second_set)
my_set.add(6)
my_set.remove(5)
# print(my_set)

first_set = {1, 2, 3}
second_set = {3, 4, 5}

# print(first_set | second_set) # {1, 2, 3, 4, 5} объединение
# print(first_set & second_set) # {3} пересечение
# print(first_set - second_set) # {1, 2} разность

# Dictionary (Словарь)
# Словарь - неупорядоченная коллекция данных, которая хранит данные
# в виде пар "ключ-значение", Ключи в словаре должны быть
# уникальными и неизменямыми, а значения - любыми типами данных

my_dict = {"key": ["value", "value2", 2], "second_key": "second_value"}
my_sencod_dict = my_dict
# большой массив 
# O(n) - list
# O(1) - dict
# "key" -> алгоритм хэширования -> index [100]

my_dict['key'] = 'new_value'
# del my_dict['key']
# print(my_dict["non-existant key"]) # KeyError потому такой ключ не существует
# print(my_dict.get("non-existant key")) # get - вывести значение по ключу или вернуть None если ключа нет
keys = my_dict.keys() # Возвращает массив всех ключей словаря
keys = list(keys)
values = my_dict.values() # Возвращает массив всех значений словаря
values = list(values)
items = my_dict.items() # Возвращает массив всех ключей и значений словаря [(ключ, значение), ...]

# Циклы For и While

# my_list = [1, 2, 3, 4]
# for i, elem in enumerate(my_list, 1): # enumerate(<Объект, по которому проходит итерация>, начало отсчета (не в итераторе, а на выходе))
#     print(f"{i}) value={elem}")

# for i in range(3, 10, 2): # range(<первый индекс>:<конечный индекс>:<шаг>)
#     print(i)

# for i in range(len(my_list)):
#     print(my_list[i])

# for index in range(0, len(my_list), 2):
#     print(my_list[i])

# my_list_new = [1, 2, 'stop', 3]
# for elem in my_list_new:
#     if elem == 'stop':
#         continue # break прекращает цикл полностью, continue отправляет нас на следующую итерацию
#     print(elem)
# else: # else работает тогда и только тогда, когда цикл доходит до конца итерируемого объекта
#     print("Я дошел до конца цикла!")

# i = 0
# while i < 10: # бесконечный цикл - while True
#     i += 1
#     if i % 2 == 0:
#         continue
#     print(i)
# else:
#     print("Конец цикла")

# def random_func() -> int | None:
#     return 1

# while i := random_func(): # присваевание внутри цикла
#     i += 1
#     if i % 2 == 0:
#         continue
#     print(i)
# else:
#     print("Конец цикла")

# Логические выражения

x = 10
if x > 5: # < > <= >=
    print("x больше 5")
elif x == 5:
    print("x равно 5")
else:
    print("x меньше 5")

a = [1, 2]
b = [1, 2]

a == b # сравнивает по значению -> True
a is b # сравнивает по адресу -> False

a != b
a is not b

a = True
b = False

def is_it_true():
    return True

# if a := is_it_true(): 
#     print("a and b")
# elif a or b:
#     print("a or b")
# elif not a and not b:
#     print("not a and not b")

if a:
    c = a
else:
    c = b

not (a or b) and (a or b)
# && = and
# || = or
# ! = not
# 0 - False
# '' - False
# None - False

# a = 0
# while a < 10: print(a := a + 1)

# Функции

# function
def my_function() -> None:
    return 'Hello'

def function_with_arguments(arg1: int, arg2: int = 5) -> int:
    return arg1 - arg2

# print(function_with_arguments(arg1=10))

def function_with_many_args(*args): # args = (1, 2, 3, 4, 5, 6)
    for arg in args:
        print(arg)

function_with_many_args(1, 2, 3, 4, 5, 6)

def function_with_many_kwargs(**kwargs): # {'first_kwarg': 1, 'second_kwarg': 25, third_kwarg: "third"}
    for key, value in kwargs.items():
        print(key, " ", value)

function_with_many_kwargs(first_kwarg=1, second_kwarg=25, third_kwarg="third")

def third_func(arg1, *args, **kwargs) -> int: # Передача в функцию множества аргументов
    print(arg1)

third_func(1)
print(type(third_func))

def my_func() -> Callable:
    def inner_func():
        print("inner")
    inner_func()
    print(inner_func)
    return inner_func

print(my_func())
inner = my_func()
inner()
