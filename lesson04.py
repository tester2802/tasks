# Continue the topic dictionary
# method fromkeys
"""
dictionary = dict.fromkeys(['key1', 'key2'])
print(dictionary)
print(type(dictionary))
test_var = dict.fromkeys(['name1', 'name2'], 'testUser')
print(test_var)
"""
"""
#Извлечение данных
test_dictionary = {'name': 'John', 'lastname': 'Snow'}
print(test_dictionary['name'])
print(test_dictionary['lastname'])
print(test_dictionary['key1']) #error
"""
"""
some_data = {1:5, 2:8, 3:4}
some_data[4] = 10 + 5
print(some_data)
some_data[10] = 20
print(some_data)
"""
"""
# method get() получает по ключу значение
cars = {'mersedec': 'mclaren', 'BMW': 'Samuray', 'toyouta': 'camry'}
print(cars.get('honda'))
"""
"""
# method keys выводит все ключи
university = {'KGTU': 'Politex', 'AUCA': 'American', 'KRSU':
'Russian'}
print(university.keys())
keys = list(university.keys())
print(keys)
"""
"""
# method values выводиь все значения
courses = {'sherlock': 'English Course', 'makers': 'Programming
Course'}
print(courses.values())
values = list(courses.values())
print(values)
print(list(courses))
print(len(courses))
"""
"""
# method items() возвращает пары ключ значение
example_dict = {'some_key': 'value', 'key2': 'value 2', 'space':
'some value' }
pairs = example_dict.items()
print(pairs)
pairs = list(example_dict.items())
print(pairs)"""
"""
method pop удаляет по ключ и значение возвращает значение
test_dictionary = {'first': 'python', 'second': 'js', 'third': 'java'}
print(test_dictionary)
var = test_dictionary.pop('third')
print(test_dictionary)
print(var)
"""
#method popitem
"""
dict_ = {'student1': 'john', 'student2': 'raychel'}
deleted = dict_.popitem()
print(deleted)
"""
"""
# method update
computers = {'Lenovo': 'e51', 'Acer': '1913' }
laptops = {'Acer': '1215', 'Macbook': 'Pro', 'Asus': 'Zenbook'}
print(laptops)
laptops.update(computers)
print(laptops)
"""
"""
# method setdefault
dict_ = {'key1': 1, 'key2': 2, 'key3': 3}
new = dict_.setdefault('key2')
print(new)
dict_.setdefault('key4', 'hello')
dict_.setdefault('key5', 'hello')
print(dict_)
"""
#
#
#
#
SETS/ Множества
new_set = set()
print(type(new_set))
print(new_set)
# unique_numbers = {1, 2, 3, 4, 5, 6, 1, 1,1,1,1, 2, 2,2, }
# print(unique_numbers)
# print(type(unique_numbers))
"""
data = [7777, 8888, 9999, 5555, 5555, 6666, 8888]
new_data = []
for phone_number in data:
if phone_number not in new_data:
new_data.append(phone_number)
else:
continue
print(data)
print(new_data)
print(list(set(data)))
"""
"""a = {1, 5, 6,8,3,4,9}
b = list(a)
b.sort()
print(set(b))
"""
# method add
sets = {1,2}
sets.add(3)
print(sets)
#method remove
sets.remove(1)
# print(sets)
# sets.remove(1)
# method discard()
# sets.discard(2)
# print(sets)
"""
numbers = {1, 2, 8, 7, 3, 4, 5,}
numbers.pop()
"""
# isdisjoint - issubset - issuperset - union -
# print(dir({1, 2}))
