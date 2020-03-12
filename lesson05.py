# # and or not
# True and True
# True or False

"""
point = input("Enter your point: ")
if point == "5":
print("Молодец !!!")
elif point == "4":
print("Ты молодец, чуть чуть осталось до отличника")
elif point == "3":
print("Старайся учиться лучше! ")
else:
print("Ты можешь лучше учиться ")
"""
# python.kg
"""
is_user_facebook_user = False
is_user_github_user = True
if is_user_facebook_user and is_user_github_user:
print("You can enter the system!")
else:
print("Sorry, you should have Facebook and Github accounts")
"""
"""
is_user_facebook_user = True
is_user_github_user = True
is_user_age_greater_18 = False
user_account_money = 9000
if (is_user_facebook_user and is_user_github_user) and (
is_user_age_greater_18 or user_account_money > 10000
):
print("You can enter the system")
else:
print("Sorry, you should have Facebook and Github accounts")
"""
"""
user_is_authenticated = False
user_has_instagram_account = True
user_has_gitlab_account = True
if user_is_authenticated:
print("Authenticated")elif user_has_gitlab_account:
print("Has gitlab account")
elif user_has_instagram_account:
print("Has instagram account")
"""
"""
[1 - 100]
3 == foo
5 == bar
3 and 5 foobar
"""
"""
numbers = list(range(1, 100))
for number in numbers:
if number % 3 == 0 and number % 5 == 0:
print(number, "foobar")
elif number % 5 == 0:
print(number, "bar")
elif number % 3 == 0:
print(number, "foo")
else:
continue
"""
"""
work_experience = 10
has_javascript = True
has_python = False
has_golang = True
if work_experience >= 10:
print("Блок1")
print("О ты Сениор разработчик")
if has_python:
print("Отлично! Ты знаешь python!")
if has_golang and has_javascript:
print("Отлично! Ты гофер и джаваскриптизер! ")
print("Молодец!,---- ")
print("Ну, ты знаешь много")
print("Продолжение блока 1")
"""
# for loop / While loop
"""
print("Без циклов не обойтись")
print("Без циклов не обойтись")
print("Без циклов не обойтись")
print("Без циклов не обойтись")
print("Без циклов не обойтись")
"""
"""
for _ in range(0, 100, 5):
print("Без циклов не обойтись")
# range(Начало, конец, шаг) start end step"""
"""
pizza = [
'first_item', 'second_item', 'third_item',
'fourth_item', 'fifth_item', 'sixth_item',
'seventh_item', 'and last_item'
]
enumerations = []
for item in pizza:
new_item = item.split('_')[0]
enumerations.append(new_item.title())
# print(f'eating {item} of pizza')
print(enumerations)
"""
str_ = "hello"
# print(dir(str_))
iterator = str_.__iter__()
# print(type(iterator))
# # print(dir(iterator))
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
"""
words = "this is the python lamguage"
new = words.split(' ')
iterator = new.__iter__()
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
"""
"""
Оператор break
Оператор continue
"""
"""
pizza = [
'first_item', 'second item', 'third_item',]
'fourth_item', 'fifth_item', 'sixth_item',
'seventh_item', 'and last_item'
enumerations = []
for item in pizza:
new_item = item.split('_')[0]
if new_item.startswith('s'):
continue
elif new_item.startswith('a'):
break
enumerations.append(new_item.title())
print(enumerations)
"""
pizza = [
'first_item', 'second item', 'third_item',
'fourth_item', 'fifth_item', 'sixth_item',
'seventh_item', 'and last_item'
]
enumerations = []
for index, item in enumerate(pizza):
print(f'This is index {index},and item ---{item}')
new_item = item.split('_')[0]
enumerations.append(new_item.title())
# print(enumerations)
# Python program to illustrate
# enumerate function
l1 = ["eat","sleep","repeat"]
s1 = "geek"
# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)
print("Return type:",type(obj1))
print(list(enumerate(l1)))
# changing start index to 2 from 0
print(list(enumerate(s1,2)))
# index, value = (0, "k")
