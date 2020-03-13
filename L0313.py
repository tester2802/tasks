'''
Fn: 
filter()
func -- Фильтрующая функция. Должна принимать элемент фильтруемого объекта. Если функция вернёт False, данный элемент не попадёт в результат. Если передано None, считается что требуется применить тождественное отображение (lambda *args: args), таким образом все элементы, оцениваемые как False будут отфильтрованы.


def get_even_numbers(num):
	if num%2==0:
		return True
	else:
		return False

numbers = [x for x in range(1,20)]
print(list(filter(get_even_numbers, numbers)))

====

alphabets = ['a','b','c','d']

def filterVowels(alph):
	vowels = ['a','j','s,','d','k']
	if (alph in vowels):
		return True
	else:
		return False
filteredVowels = list(filter(filterVowels,alphabets))
print(filteredVowels)

Sample 2

prods = ['acer','lenovo','asus','hp','dell']
def filter_prod(prod):
	if prod in prods:
		return True
	else:
		return False

result = list(filter(filter_prod,['lenovo','fujitsu','dell']))
print("prod_list: ",prods)
print("filtered result",result)

Sample 3 --

def genderFilter(obj):
	people = ["Sinan":"M","Olya":"F","Vika":"F","Tahir":"M","Guka":"F"]
	if obj in people.values():
		return True
	else:
		return False
result = filter(genderFilter,["M",])
for x in result:
	print(people)
print(result)

Sample 4

dict_of_names = {
	7: "Sam",
	8: "John",
	9: "Bush",
	10: "Obama",
	11: "Putin",
	12: "Si Zin Pin",
	13: "Marks",
	14: "Atilla"
}

newDict = dict(filter( lambda elem: elem[0] %2 == 0, dict_of_names.items()))
print("Filtered dictionary:")
print(newDict)

Sample 5 - doen not work!!


dict_of_names = {
	7: "Sam",
	8: "John",
	9: "Bush",
	10: "Obama",
	11: "Putin",
	12: "Si Zin Pin",
	13: "Marks",
	14: "Atilla"
}

newDict = dict(filter( lambda elem: len(elem[1] == 6, dict_of_names.items())
print(newDict)


Sample 6 - Extract by the value "m"

people = {"adam":"m", "asel":"f","kira":"f","kalys":"m"}
newDict = dict(filter(lambda elem: elem[1] == 'm', people.items()))
print(newDict)

Sample 7 - Extract by sex

people = {"adam":"m", "asel":"f","kira":"f","kalys":"m"}

def genderFilter(elem):

	if elem[1] == sex:
		return True
	else:
		return False

sex = input("Enter the gender (m / f): ")
newDict = dict(filter(genderFilter,people.items()))
print(newDict)
print(type(newDict))

===== Lamdda
Генерирует и возвращает анонимную функцию.
Выражение «лямбда» создаёт объект функции, который в отличии от определения при помощи def не именован, т.е. анонимен.
feature for using one string fn


x = lambda a,b : a*b
print(x(5,7))


x = lambda a,b,c : a+b+c
print(x(1,2,45))

def sort_int(x):
	return int(x)
def sort_el(x):
	return x[-1]

data = ['21','138','45','88']
print(sorted(data,key = sort_int))
print(sorted(data,key = sort_int))

lets write the same fns with lambda

data = ['53','38','45','87']
print(sorted(data, key = lambda z: int(z))) # сортировка
print(sorted(data, key = lambda z: z[-1]))  # сортировка по 2-индексу

Function map

name_length = map(len,['Alik','Malik','Tom','Van Damm']) # принимает список имен и высчитвывает длину каждошо элемента
print("Принимает список имен и высчитвывает длину каждошо элемента")
print(list(name_length))

squares = map(lambda x: x*x, [1,2,3,4,5,6,7])
print(list(squares))

Сложение / умножение элементов

from functools import reduce
sum1 = reduce(lambda a, x: a*x, [3,1,2,3,4,5])
print(sum1)


Сравненеие
i=lambda x ,y: x if x<y else y
print (i(36,2))


Использования ламбду в циклах для умножения каждого элемента на определенное число
'''

list0 = [1,2,3,4,5,6]
new_list = lambda list: [number*mult_num for number in list0]
print("List: ", list0)
mult_num = int(input("Enter the num multiply into: "))
print("result: ", new_list(list0))