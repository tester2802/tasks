"""
5. Напишите функцию которая находит самою длинную слово в строке.
"""

strng = input("Enter string: ")
print(strng)

# преобразование строки в список слов,разделение происходит по пробелу
listWords = strng.split()

# предполагается, что самое длинное слово находится первым в списке, т. е. имеет индекс 0
idLongestWord = 0

# остальные слова перебираются в цикле
for i in range (1,len(listWords)):
	
    # Если длина слова под индексом idLongestWord больше, чем длина слова под текущим индексом,
    if len(listWords[idLongestWord]) < len(listWords[i]):
        # то следует записать индекс текущего слова в переменную idLongestWord
        idLongestWord = i

# извлечение из списка listWords слова с индексом idLongestWord и его вывод на экран
print(listWords[idLongestWord], len(ifLongestWord[i]))