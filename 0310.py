"""
10. Напишите функцию которая определит сколько раз встречается элемент в списке.
"""


a = [int(i) for i in input().split()] #заполним список
x = int(input()) #пользователь вводит число, количество вхождений которого нужно подсчитать
print(a.count(x)) #выводим количество вхождений числа X в список A