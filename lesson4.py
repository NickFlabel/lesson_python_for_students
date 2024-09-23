# Сортировка, поиск, регулярные выражения

from typing import Callable


my_lst = [11, 9, 15, 20]

# print(sorted(my_lst)) # Функция sorted сортирует от наименьшего к наибольшему

# print(my_lst) # Функция sorted создает и возвращает новый отсортированный список

my_lst.sort() # сортировка in-place

# print(my_lst)

my_strs = ['abc', 'abcdef', 'a', 'ab', 'abcd']

sorted_list = sorted(my_strs, key=len, reverse=True)

# sorted(<последовательность>: Iterable, <функция-сортировщик>: Callable, <В обратном порядке>: bool)

words = ['orange', 'banana', 'cherry']

sorted_list = sorted(words, key=lambda x: x[-1])

# В качестве key нам нужен Callable объект, который принимает один позионный аргумент

my_dict = {"apple": 5, "banana": 3, "cherry": 7}

sorted_list = sorted(my_dict, key=lambda x: my_dict[x])

my_tuples = [(1, 2), (2, 1), (5, 0)]

sorted_list = sorted(my_tuples, key=lambda x: x[1])

# print(sorted_list)

isinstance(my_tuples, list) # True/False

# Поиск

numbers = [1, 2, 3, 4, 3]

if 3 in numbers:
    print("3 is found!")

index_of_3 = numbers.index(3) # Возвращет первый индекс искомого значения

my_filter = filter(lambda x: x % 2 == 0, numbers)
# filter(<функция-фильтр>, объект) -> генератор
# Функция-фильтр должна возвращать True или False

# print(list(my_filter))

# Регулярные выражения

import re

email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._%+-]+\.[a-zA-Z]{2,}$'

email = "test@test.com"

# if re.match(email_regex, email): # match проверяет string на соответствие regex с его начала
#     print("email is correct")
# else:
#     print("email is incorrect")

text = "I am here"

new_text = re.sub(r'am', 'was', text)

# print(new_text)

# re.findall -> возвращает список всех совпадений

# Работа с файлами

# file = open("my_file.txt", 'r') # 'r' - чтение, 'w' - запись, 'a' - append, 'b' - бинарный режим, используется в сочетании с другими

# w - создает новый файл или перезаписывает старый
# a - тоже самое, что и запись, но не удаляет содержимое файла
# r - чтение (файл должен существовать)
# fie.write() - записывает аргумент
# file.writelines() - записывает элементы коллекции
# a = ['my_first_line', 'my second line']
# file.writelines(a)


# with open('my_file.txt', 'r') as file:

#     for line in file.readlines():
#         print(line)

# python сам делает file.close()

# Управление OS

# import os

# if os.path.exists('my_file.txt'):
#     print("File does indeed exist")

# file_stats = os.stat('my_file.txt')
# print(f'Размер файла: {file_stats.st_size} байт')

# os.rename('my_file.txt', 'my_new_file.txt')
# # os.remove('my_file.txt')

# os.mkdir('my_new_dir')
# # os.rmdir('my_new_dir')


# Генераторы

# Генератор - это вид итератора, который позволяет создавать интерационные
# последовательности с использованием функций. Важно понимать, что
# в отличии от классического итератора, который уже содержит в памяти
# все возможные значения по которому он итерируется, Генератор же
# генерирует эти значения, не имея их в памяти

def count_up_to_ten(max):
    count = 1
    while count <= max:
        yield count
        count += 1

counter = count_up_to_ten(10)
# print(counter)
# # for i in counter: 
# #     print(i)

# print(next(counter))
# print(next(counter))
# print(next(counter))

def return_different_values():
    yield "value_1"
    yield "value_2"



my_gen = return_different_values()
my_values = list(my_gen)
print(my_values)
# print(next(my_gen))
# print(next(my_gen))

def infinite_generator():
    count = 1
    while True:
        yield count
        count += 1

# gen = infinite_generator()
# for i in gen:
#     print(i)

abc = [i * i for i in counter] # list comprehention
print(abc)
generator = (i * i for i in range(10))

for i in range(10):
    pass

# Декораторы

# В широком смысле декоратр - паттерн проектирования, который позволяет
# расширять фукционал объект без изменения его самого

# Open/Close Principle - классы должны быть открыты для расширений, но закрыты для изменений

# В более узком смысле декоратор это способ расширить обернуть функцию в Python и тем самым дополнить ее функционал

def my_dec(func: Callable):
    def wrapper(*args, **kwargs):
        print("Something before calling the func")
        func(*args, **kwargs)
        print("something after calling the func")
    return wrapper

def decorator(func: Callable, multiplier):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs) # add(*args, **kwargs)
        return result * multiplier # действия после выполнения
    return wrapper

def add(arg1, arg2):
    return arg1 + arg2

dec_func = decorator(add, 4)
print(dec_func(1, 2))

# result = decorator(add)(1, 2)
# decorated_func = decorator(add)
# print(decorated_func(1, 2))

# Снача мы передаем другую функцию в декоратор (decorator(add))
# Декоратор подставляет переданную фукцию на место func внутри вложенной функции wrapper
# Декоратор возвращает вложенную функцию, котороая уже знает какую именно 
# функцию она оборачивает
# затем мы можем вызвать уже задекорированную функцию

@my_dec
def my_func():
    print("Inside function")

my_func()


def multiplier_decorator(multiplier: int):
    def decorator(func: Callable):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * multiplier
        return wrapper
    return decorator

@multiplier_decorator(3)
def add(arg1, arg2):
    return arg1 + arg2

print(add(1, 2))

multiplier_decorator(3)(add)(1, 2)


