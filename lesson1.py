# Comment
# String

'''
This is 
a
very
long
comment
/* */
'''
second_name = "String with \" \n"
str_with_another_synt = 'string'

name = "Nick"
surname = "Selin"
full_name = f"{name} {surname}"

full_name = name + " " + surname

print(full_name.upper())
print(full_name.lower())

print(len(full_name))

text = "Hello+World"

print(text[::-1]) # [<первый индекс>:<конечный индекс>:<шаг>]
print(text[:-5])

a: float #  314 * 10**-2
b: int # 11

a = 3.14
b = float(5) # 5.0 == 5 * 10**0

a = a + 1
a += 1 # a = a + 1
b = "4"
type(b) # для понимания какой тип данных содержится в этой переменной

a = a ** 2 # Возведение в степень
a = a // 2 # Деление без остатка
a = a % 2 # Деление с остатком (и только с остатком)
a = 1 ^ 2 # XOR -> 101 XOR 100 -> 001

int("1")
float("1.24")

a = True # boolean в Python с большой буквы

# Списки (List) == Array

my_list = [1, 2, 3, "abc", 3.14]
print(my_list[3])
my_list[3] = "cba"
print(my_list[3])

my_list.append("new_element")
print(my_list)

print(type(my_list))
my_list.pop()
print(my_list)

print(my_list[:2]) # слайсы работают на списках

second_list = ['newest_element', 5]

my_list = second_list + my_list
print(my_list)

second_list = (second_list + my_list) * 3
print(second_list)

len(my_list)


# Tuple

# tuple == list, но не может быть изменено

my_tuple = ("first_elem", 2, 3, [1, 2])

print(my_tuple[0])
my_tuple[0][1] = 'r'
print(my_tuple)
my_list = [i for i in range(10)]
for i in range(10):
    my_list.append(i)
