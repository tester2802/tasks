# Lesson No.6 
# date: 03.09.20
# while loop.  Важна точка выхода
"""
i=0
while i<5:
	print(i+1,"Hello")
	i+=1 # Можно и в обратном направлении поставить степ


password = "helloworld"
enter_pass = ""
while enter_pass != password:
	enter_pass = input("enter your password please: ")

Генераторы списков, словарей и множеств (Работают быстрее чем обычный цикл)

diap = range(1,11) # range(10 - конечная точка)
squares = [x**2 for x in diap]
print(squares)


city = "Bishkek"
print(city, "\n\nresult:")
letters_up = [x.upper() for x in city]
print(letters_up)
letter_down = [x.lower() for x in letters_up]
print(letter_down)


# Обработка условий внуткри генератора
diap = range (1,12)
even_num = [x for x in diap if x%2==0] # Генераторы списков обработают только одно условие!!
odd_num = [x for x in diap if x%2==1]
print(even_num)
print(odd_num)

# Сравнение времени выполнения задач
from datetime import datetime # это объект
start = datetime.now()
new_list = []
for x in range (1, 10000000):
	new_list.append(x)
print(datetime.now() - start)


from datetime import datetime # это объект
start = datetime.now()
new_list = [x for x in range (1, 1000000)]
print(datetime.now() - start)


# Генераторы словарей - пользуется для быстрого создания списка
dict_ = {key: key**2 for key in range(1,10)}
print(dict_)

names = ['abu', 'beri', 'stiven','ivan']
new_dict = {key:value.title() for key, value in enumerate(names)} # enumerate возвращает [(0, 'abu', 1: 'bei']
print(new_dict)
"""
list_ = [1,1,1,1,1,2,2,2,2,2,3,3,3,3]
new_sets = {x for x in range(1,10)}
new_list = {x for x in list_}
print(new_sets)
print(new_list)# from the list_ extracted only tht unique values
print(type(new_sets)) # множество то же самое что и словари с единственны отличием: у множества есть уникальный ключ...??
