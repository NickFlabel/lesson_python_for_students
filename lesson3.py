# Рекурсия - ситуация, когда функция вызывает сама себя

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# В рекурсивной функции всегда должен быть базовый сценарий

print(factorial(5))

# factorial(5)
# return 5 * factorial(4) (1st rec)
# (1st rec) factorial(4)
# (1st rec) return 4 * factorial(3) (2d rec)
# (2d rec) factorial (3)
# (2d rec) return 3 * factorial(2) (3d rec)
# (3d rec) factorial(2)
# (3d rec) return 2 * factorial(1) (4th rec)
# (4th rec) factorial(1)
# (4th rec) return 1
# (3d rec) return 2 * 1
# (2d rec) return 3 * 2
# (1th rec) return 4 * 6
# return 5 * 24
 

# Создайте игру, в которой компьютер загадывает слово, а игрок должен его угадать
# Каждую попытку программа сообщает, сколько букв было угадано

# Требования: использовать словарь, где ключ - категория загаданного слова,
# а значение - список слов, относящийся к этой категории


from operator import add
import random
from xml.dom.minidom import Attr

# Словарь категорий и слов
words = {
    "Animals": ["elephant", "giraffe"],
    "Fruits": ["apple", "orange"],
    "Countries": ["canada", 'brazil']
}

# Основная функция игры
def guess_the_word():
    category = random.choice(list(words.keys()))
    word = random.choice(words[category])
    attempts = 5

    print(f"Category: {category}")
    guessed_letters = ['_'] * len(word)

    while attempts > 0:
        guess = input("Enter a letter: ").lower()

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_letters[i] = letter
            print(f"Correct guess: {''.join(guessed_letters)}") # ['_', 'a', 'b'] -> '_ab'
        else:
            print("Wrong guess!")
            attempts -= 1
        
        if "_" not in guessed_letters:
            print(f'Congratulations! You guessed the word: {word}')
            break

        print(f'Attempts left: {attempts}')
    else:
        print(f"Game over! The word was: {word}")

random.randint(1, 100)

a = 1
b = 2
a, b = b, a

# Модули, библиотеки, пакеты
import utils # импорт модуля в качестве переменной utils

print(utils.addition(1, 2))

from utils import addition, subtraction # импорт конкретных переменных модуля

addition(1, 2)

from utils import addition as addition_from_utils # импорт и изменение имени

addition_from_utils(1, 2)

from utils import * # импорт всего

import time # простейшие манипуляции со временем
# time.sleep(1)
import datetime # работа с датой и временем from datetime import datetime
# now = datetime.datetime.now()
# print(now)
from typing import List, Any

import requests

# response = requests.get("http://example.com")
# print(response.content)

# py -m venv <название вашего виртуального окружения> - создает виртуальное окружение
# ./<название окружения>/Scripts/activate - активировать окружение
# deactivate - деактивировать окружение
# pip install <название модуля> - установить библиотеку
# pip freeze - показать установленные библиотеки
# pip freeze > requirements.txt - сохранить установленные библиотеки в файл
# pip install -r requirements.txt - устанавливает все библиотеки из файла

# import my_python_dir
# from my_python_dir import my_module_func
# from my_python_dir.my_module import my_tuple

# print(my_tuple)

# my_module_func()

# Обработка исключений

a = {}

try:
    a['non-existant key']
    raise Exception # Вызов исключений через raise
except Exception as e: # Несколько исключений
    print(e)
else: # После try если try не raise'ил исключений
    print("No error")
finally:
    print("Either try or except")

# Лямбда-функции - анонимная функция, имеющая произвольное количество
# аргументов, но только одно выражение. Результат выражения
# возвращается в качестве резултата функции

addition_lambda = lambda a, b: a + b # lambda <аргументы>: <выражение>
print(addition_lambda(1, 2))

from typing import Callable

def my_callable_func(func: Callable):
    print(func())

my_callable_func(lambda: "value")
