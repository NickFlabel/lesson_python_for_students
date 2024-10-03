# Band of Four в 1994 написали книгу под названием "Design Patterns: 
# Elements of Reusable Object-Oriented Software"

# Книга содержала каталог из 23 паттернов, которые помогали решать распространенные
# пролемы с проектированием на основе объектно-ориентированного программирования

# Зачем нужны паттерны?
'''
1) Повторное использование решений
2) Упрощение сложных задач
3) Улучшение коммуникации
4) Поддержка и развитие кода

Паттерны в первую очередь относятся к ООП потому помогают правильно организовать 
взаимодействие объектов

Типы паттернов:
1) Структурные паттерны - помогают организовать классы и объекты для создания
больших структур, которые легко поддерживать
2) Порождающие паттерны - сосредоточены на том, как создаются объекты и помогают
абстрагировать процесс создания объектов
3) Поведенческие паттерные - фокусируются на взаимодействии объектов и способах 
управления ими

Паттерн - решение задачи в контексте
'''

# Абстрактный класс

from abc import ABC, abstractmethod

# class Animal(ABC):
    
#     @abstractmethod
#     def make_sound(self):
#         print("sound")

#     def sleep(self):
#         print("sleep")


# class Cat(Animal):

#     def make_sound(self):
#         print("meaow")


# cat = Cat()
# cat.make_sound()
# cat.sleep()

class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass


class SleepBehavior:

    def sleep(self):
        print("sleep")


class Cat(Animal, SleepBehavior):

    def make_sound(self):
        print("meaow")


# Стратегия

# Есть симулятор утиного пруда и нам надо сделать разные виды уток
# утки должны плавать и издавать звук


# Принцип 1: Выделите аспекты приложения, которые могут изменяться и отделите их от тех,
# которые всегда остаются постоянными

# Неизменным у нас был класс Duck, а вот методы fly() и quack() следует выделить в
# отдельные наборы классов. 

# Принцип 2: Программируйте на уровне интерфейса, а не на уровне реализации
# Programm to interface not details


class FlyBehavior(ABC):
    @abstractmethod
    def __call__(self):
        pass


class QuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass


class FlyWithWings(FlyBehavior):
    def __call__(self):
        print("Я лечу с крыльями!")


class NoFly(FlyBehavior):
    def __call__(self):
        print("Я не умею летать")


class Quack(QuackBehavior):
    def quack(self):
        print("quack")


class NoQuack(QuackBehavior):
    def quack(self):
        print("No quack")


class Duck(ABC):
    def __init__(self, fly_behavior, quack_behavior):
        self.perform_fly_function = fly_behavior
        self.quack_behavior = quack_behavior

    def perform_quack(self):
        self.quack_behavior.quack()

    def swim(self):
        print("Все утки умею плавать")


class MallardDuck(Duck):
    ...

class RubberDuck(Duck):
    ...

class ReadheadDuck(Duck):
    ...

mallard = MallardDuck(FlyWithWings(), Quack())
rubber = RubberDuck(NoFly(), NoQuack())
redhead = ReadheadDuck(FlyWithWings(), Quack())
functional_duck = MallardDuck(lambda: print("lambda func"), Quack())


mallard.perform_fly_function()
mallard.perform_quack()
rubber.perform_fly_function()
rubber.perform_quack()
rubber.perform_fly_function = FlyWithWings()
rubber.perform_fly_function()
functional_duck.perform_fly_function()


# Гибкость - мы можем легко изменять поведение уток в зависимости от их типа или обстоятельств
# не изменяя сам основной код

# Масштабируемость - добавление нвоых уток или иного поведения не требует измения существующих классов

# Простота поддержки - мы избежали дублирования кода и можем менять алгоритмы, не затрагивая структуру программы

# Стратегия - это паттерн, который определяет семейство алгоритмов, инкапсулирует и
# обеспечивает их взаимозаменяемость. Паттерн позволяет модицировать алгоримны
# независимо от их использования на стороне клиента


# Принцип 3: Отдавайте предпочение композиции перед наследованием

# Декоратор

# У нас есть кофейня с несколькими видами кофе

class Beverage(ABC):
    size: int

    @abstractmethod
    def cost(self) -> int:
        pass

    @abstractmethod
    def description(self) -> str:
        pass

    def get_size():
        pass


class Esspresso(Beverage):
    def cost(self):
        return 600
    
    def description(self):
        return "Эспрессо"
    

class DarkRoast(Beverage):
    def cost(self):
        return 700
    
    def description(self):
        return "Черный кофе"
    

class ComponentDecorator(Beverage):
    pass


class Milk(ComponentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def cost(self):
        # какой-нибудь алгоритм
        return self.beverage.cost() + 100

    def description(self):
        return self.beverage.description() + ", молоко"
    
    def get_size(self):
        return self.beverage.get_size()
    

coffee = DarkRoast()
milk = Milk(coffee)
double_milk = Milk(milk)
# print(double_milk.description())
# print(double_milk.cost())

