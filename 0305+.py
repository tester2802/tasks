"""
5. Напишите функцию которая находит самою длинную слово в строке.

Палиндромом называется слово или фраза, которые читаются одинаково справа налево, и слева направо.

"""
def thelongestword():
	words = input("\nYour words, pls: \n")
	wordslist = words.split()
	idlw = 0
	for i in range(1,len(wordslist)):
		if len(wordslist[idlw]) < len(wordslist[i]):
			idlw = i
	print(wordslist[idlw])

thelongestword()
thelongestword()
thelongestword()