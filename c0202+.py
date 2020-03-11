'''
2) Попросить пользователя ввести слова через пробел.
Отсортировать слова по количеству символов и вывести на экран результат.
'''

sm = input("Pls enter the string with spaces:\n ")
sp = sm.count(" ")


print("length of the string: ", len(sm))
print("qn of words: ",sp+1)

sm = sm.split()
sm.sort(key = len)
sm = " ".join(sm)
print(sm)