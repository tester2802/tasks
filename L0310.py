'''
accumulator :: 
try except finally :: выполнять код при любом исходе. В основном пользуется try / except. Работа с ошибками. Обход ошибок.
def :: 

accumulator = 0
for x in range (1, 15):
	accumulator = accumulator + x
	print (accumulator,)
print("\n",accumulator)

import math
numbers = sum([x for in range (1,101)])
print(numbers)

passed_num = 0
our_num = 50
try:
	result = our_num / passed_num
except ZeroDivisionError: #если не указать конкретную ошибку, то блок будет применяться на все виды ошибок
	result = 0
finally:
	print("Done")

Functions:

def add(x,y):
	return x+y

print(add(15,12))

Функция калькулятор

def sum_(num1, num2):
	result = num1 + num2
	return result #Если написать только print, то тогда результат выйдет только на терминал

def sub_(num1, num2):
	result = num1 - num2
	return result
def div_(num1, num2):
	try:
		result = num1 / num2
	except ZeroDivisionError:
		result = 0
	return result
def mul_(num1, num2):
	result = num1 * num2
	return result

def main():
	num1 = int(input("num1: "))
	num2 = int(input("num2: "))
	operator = input("operator + - * / : ")
	if operator == "-":
		print(sub_(num1, num2))
	elif operator == "+":
		print(sum_(num1, num2))
	elif operator == "*":
		print(mul_(num1, num2))
	elif operator == "/":
		print(div_(num1, num2))
	else:
		print("The operator is not defined!")
	question = input("Would u like to continue? (yes / no): ")
	if question.lower() == "yes":
		main()
	else:
		print("\nYou have choosen 'no' option. Bye.")
main()
=============

def func (a, b, c=2): # с - аргумент по умолчанию. и Должен стоять в КОНЦЕ. Остальные позиционные аргументы
	return a+b+c
print(func(12,14))
============

def get_data(*args):
	return args

print(get_data(1,2,3,4,5,"hello wotrl","hi, galaxy")) # positional argumentt


def get_data(*args):
	for x in args:
		print(x)
	return args

print(get_data(1,2,3,4,5,"hello, world","hi, galaxy")) # positional argumentt

#kwargs
def get_dict(**kwargs):
	return kwargs
print(get_dict(name='abil', lastname='Kojojash',age = 26))

# 
def testing(*args, **kwargs):
	return args, kwargs # tuple and dicts wil be inside the cortezh
	#args принимает только позиционные аргументы, а kwargs принимаем именованные аргументы

print(testing(12, 12, 16, name='Abil', lastname="Manasov", age=26))


def get_info(name, lastname, age):
	return name+lastname+str(age)
print(get_info('Abil',lastname="Manasov", age=30))


#функция это именованный блок кода, которого можно вызывать (импортировать в другие алй) несколько раз, чтобы не писать один и тот же код несколько раз
