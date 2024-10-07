# Принцип 4: открытости-закрытости (Open/Close Principle)
# Классы должны быть открыты для расширения, но закрыты для модификации


request = {"method": "GET"}


class AuthenticationMiddleware:

    def __init__(self, next):
        self.next = next

    def __call__(self, request):
        # каким-то образом проверяет пользователя
        user = {"name": "user"}
        request['user'] = user
        if user:
            return self.next(request)
        else:
            raise Exception


def request_handler(request):
    print(request)
    return {"answer": f"Your {request['method']} request has been handled!"}


middleware = AuthenticationMiddleware(request_handler)
next_middleware = AuthenticationMiddleware(middleware)
next_next_middleware = AuthenticationMiddleware(next_middleware)
# print(next_next_middleware(request))


# Observer

from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def _notify_observers(self):
        pass


class Observer(ABC):
    @abstractmethod
    def update(self):
        pass


class WeatherData(Subject):
    def __init__(self):
        self.observers = []


    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def _notify_observers(self):
        for observer in self.observers:
            observer.update()

    def event(self):
        self._notify_observers()


class CurrentConditionDisplay(Observer):
    def __init__(self, subject: Subject):
        self.weather_data = subject
        self.weather_data.register_observer(self)

    def update(self):
        print('I was notified')


weather_data = WeatherData()
current_display = CurrentConditionDisplay(weather_data)
weather_data.event()


# Template (Шаблон)


# Рецепт кофе - 1) вода 2) заварить кофе 3) перелить в чашку 4) добавить сахар и молоко
# Рецепт чая - 1) вскипятить воду 2) заварить чай 3) перелить в чашку 4) добавить лимон



class CaffeineBeverage(ABC):

    def prepare_recipe(self):
        self.boil_water()
        self.prepare()
        self.pour_in_cup()
        self.add_extra_components()

    @abstractmethod
    def prepare(self):
        pass

    def add_extra_components(self):
        pass

    def boil_water(self):
        print("Boiling water")

    def pour_in_cup(self):
        print("Pouring in a cup")


class Tea(CaffeineBeverage):

    def prepare(self):
        print("preparing tea")


tea = Tea()
tea.prepare_recipe()

# Шаблон определяет основные шаги алгоритма и позволяет подклассам предоставить реализацию
# одного или нескольких шагов

# Factory Method определяет интерфейс создания объекта, но позволяет подклассам 
# выбирать конкретный класс создаваемого экземляра

# Абстрактная фабрика определяет интерфейс для создания семейств взаимосвязанных объектов
# без указания их конкретных классов

# Фасад - структурный паттерн, котоырй предоставляет простой интерфейс к сложной системе 
# классов, библиотеке или фреймворку

# ORM - get(id)

# Команда (Command) - поведенческий паттерн,, который превращает запросы в объекты, позволяя
# передавать их как аргументы при вызове методов, поддерживает отмену операций

# MVC - Model View Controller
