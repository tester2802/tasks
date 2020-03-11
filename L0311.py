'''
Date: 11.03.2020
Продолжение темы Фунцкии

function abc() возвращает абсолютное значение
встроенная функция

number = -123.23
absolute_value = abs(number)
print(absolute_value)

function all() - 
Вернёт True, если все элементы итерируемого объекта представляются истиной (True).
Также возвращает True, если итерируемый объект пуст.

iterable_obj = [1,2,3,4,5]
print("1:",all(iterable_obj))

iterable_obj = [1,2,0,4,5]
print("2:",all(iterable_obj))

print("3:",all([True, True, False]))  # False
print("4:",all([True, True, True]))  # True

print("5:",all([1, 2, 0]))  # False
print("6:",all([1, 2, 3]))  # True

print("7:",all([1, 2, ""]))  # false

def all_(iter):
	for x in iter:
		if not x:
			return False
	return True
print("\n8 by defined func:", all_([1,2,3,4,5]),"\n")

=== Function any()
Проверяет, есть ли среди указанных элементов хотя бы один, принимающий значение True.

print(any([]))  # False

print(any([False]))  # False
print(any([False, True]))  # True

print(any([0]))  # False
print(any([0, 1]))  # True

=== Function Bool()
Логический тип представлен двумя постоянными значениями False и True. Значения используются для представления истинности.

print(bool(0))
print(bool(1))
print(bool([])==False)

=== Function ascii()
Возвращает строковое представление объекта с экранированными не-ASCII символами.

print(ascii("гол"))
print(ascii("goal"))

=== Function callable()
Возвращает True для объекта, поддерживающего вызов.

def adder(a1,a2):
	return a1 + a2
is_callable = callable(adder)
print("Function is callable", is_callable)
print(adder (12, 34))

=== Function chr()
Возвращает символ по его числовому представлению.
Function ord() - антипод chr()

print(chr(120))
print(chr(97))
for i in range (90,100):
	print(chr(i))

print(ord("i"))

=== Function divmod() - Возвращает пару частное-остаток от деления аргументов.

a1 = int(input("a1="))
a2 = int(input("a2="))
print("Результат функции divmod():",divmod(a1,a2))
a,b = divmod(a1,a2)
print("Целое число: ",a)
print("Остаток: ",b)

=== Function float()
Тип представляет число с плавающей запятой.

from decimal import Decimal
import math
print(math.pi)

=== Function enumerate()
Возвращает генератор, отдающий пары счётчик-элемент для элементов указанной последовательности.
'''
seasons = ['Spring','Summer','Fall','Winter']
new = list(enumerate(seasons))
print(new)