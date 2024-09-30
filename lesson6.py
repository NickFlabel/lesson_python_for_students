# Продолжение dunder методов

# __call__()

class MyCallable:

    def __call__(self, arg1, arg2): # instance()
        return arg1 + arg2
    
my_callable = MyCallable()
# print(my_callable(1, 2))


# Итератор и интерфейс итератора

from abc import ABC, abstractmethod

class MyIteratorInterface(ABC):

    @abstractmethod
    def __iter__(self):
        ...
    
    @abstractmethod
    def __next__(self):
        ... # pass

# # for i in range(10):  
# my_generator = range(10)
# print(next(my_generator))

class MyListIterator(MyIteratorInterface):
    current: int

    def __init__(self, collection: list) -> None:
        self.collection = collection

    def __iter__(self):
        self.current = 0
        return self
    
    def __next__(self):
        if self.current < len(self.collection):
            result = self.collection[self.current]
            self.current += 1
            return result
        else:
            raise StopIteration

    
my_list = MyListIterator([1, 2, 3])
for elem in my_list:
    print(elem)


class FibonacciGenerator:
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self
    
    def __next__(self):
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        return value
    
fib = FibonacciGenerator()
for _ in range(10):
    print(next(fib))


# Множественное наследование

class Animal:

    def make_sound(self):
        print("I made a sound")


class Flying:

    def fly(self):
        print("I fly")


class Bird(Animal, Flying):
    ...


new_bird = Bird()
new_bird.fly()
new_bird.make_sound()


class Parent1:
    
    def greet(self):
        print("Greetings from Parent1")


class Parent2:

    def greet(self):
        print("Greetings from Parent2")


class Child(Parent2, Parent1):
    
    def greet(self):
        super().greet()
        print("Greetings from child")

child = Child()
# child.greet()

# MRO - method resolution order (порядок разрешения методов)
# Проблема ромбовидного наследования

# print(Child.__mro__[0]().greet()) 
# print(child.__class__.__mro__)

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.mro())

# D -> B -> C -> A

class A:
    pass

class B(A):
    pass

class C:
    pass

class D(B, C):
    pass

print(D.mro())

# D -> B -> A -> C

# Mixins - классы-примеси

class A:
    def greet(self):
        print("greet from A")

class Parent1:
    
    def greet(self):
        print("Greetings from Parent1")


class Parent2(A):

    def greet(self):
        print("Greetings from Parent2")


class Child(Parent2, Parent1):
    
    def greet(self):
        super(A, self).greet()
        print("Greetings from child")

print(Child.mro())
child = Child()
child.greet()

class MyClassWithMethods:
    class_var = 0

    @classmethod
    def increment_class_var(cls):
        cls.class_var += 1

MyClassWithMethods.increment_class_var()
print(MyClassWithMethods.class_var)
my_class = MyClassWithMethods()
print(my_class.class_var)
my_class.class_var = 20
MyClassWithMethods.increment_class_var()
print(MyClassWithMethods.class_var)
print(my_class.class_var)

# базовый Product - он будет описывать товар
# ElectoronicProduct FoodProduct
# Каждый из этих классов должен реализовывать метод __add__

class Product:
    def __init__(self, name: str, price: int, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"Product: {self.name}, Price: {self.price}, Quantity {self.quantity}"
    
    def __add__(self, other: 'Product'):
        try:
            if self.name == other.name:
                return Product(self.name, self.price, self.quantity + other.quantity)
            else:
                raise TypeError
        except AttributeError:
            raise TypeError

    def __eq__(self, other: 'Product'):
        return self.name == other.name
    

class ElectronicProduct(Product):
    def __init__(self, name: str, price: int, quantity: int, warranty_id: int):
        super().__init__(name, price, quantity)
        self.warranty_id = warranty_id


class FoodProduct(Product):
    def __init__(self, name: str, price: int, quantity: int, expiration_date: str):
        super().__init__(name, price, quantity)
        self.expiration_date = expiration_date


product1 = FoodProduct("Apple", 2, 5, "11.10")
product2 = FoodProduct("Banana", 2, 3, "11.10")
product3 = FoodProduct("Apple", 1, 1, "11.10")

try:
    products = product1 + product2
except TypeError:
    print("cant add these products")

products = product3 + product1

print(products)
print(product1 == product3)
