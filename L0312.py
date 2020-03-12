'''
DateL 12.03.2020
Тема: Область видимости переменных в функции

this_var_is_visible = "\nCan be seen inside and outside\n"

def var_visibility():
	this_is_not_visible = "Can't be seen outside"
	print(this_is_not_visible)
	return

var_visibility()

print(this_var_is_visible)
print(this_is_not_visible)


def some_func():
	print(locals()) # получаем пустой словарь

some_func('Daniyar')

name = "Asus"
def get_name():
	name = "Acer"
	return name
print(get_name())
print(name) # выходит глобальное переменное


def get_info():
	# name, man, zil, abc = "John", "Abil", "Gulu", "Theta"
	kil = ["aaa","bbb","ccc"]
	age = 18
	print(locals())
get_info()


def get_name():
	name = "Soke"
	age = 18
	print("Function get_name() и его пространство:", locals())

print("Внешнее пространство имени: ",locals())
get_name()

'''
import time
name = "Lenovo" #global
def fn_one():
	name = "fn_one()"
	def fn_two():
		# name = "Acer"
		print(name)
		print(locals())

	fn_two()
time.sleep(3)
fn_one()

# ELGB - local > enclosed > global > built-in

