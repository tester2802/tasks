# while loop
"""
i = 0
while i <= 20:
print("hello")
i += 1
"""
"""
password = "helloworld"
input_ = ""
while input_ != password:
input_ = input("Enter your password: ")
"""
"""
i = 30
while i != 0:
print(i)
i -= 1
"""
# Генераторы списков, словарей и множеств
"""
diapazon = range(1, 11)
squares = [x**2 for x in diapazon]
print(squares)
"""
"""
city = "bishkek"
letters_up = [x.upper() for x in city]
print(letters_up)
"""
"""
diapazon = range(1, 101)
even_numbers = [x for x in diapazon if x % 2 == 0]
print(even_numbers)
"""
# from datetime import datetime
"""
start = datetime.now()
new_list = []
for x in range(1, 1000000):
new_list.append(x)
print(datetime.now() - start)
"""
"""
start = datetime.now()
new_list = [x for x in range(1, 1000000)]
print(datetime.now() - start)
"""
# генераторы словарей
"""
dict_ = {n: n ** 2 for n in range(1, 10)}
print(dict_)
"""# [(0, 'john'), (1, 'raychel')]
"""
names = ['john', 'raychel', 'peter', 'samanda']
new_dict = {key:value.capitalize() for key, value in enumerate(names)}
print(new_dict)
"""
"""
list_ = [1,1,1,1,1,2,2,2,2,3,3,3,3,3]
new_sets = { x for x in list_}
print(new_sets)
print(type(new_sets))
"""
