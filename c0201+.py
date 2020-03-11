'''
1) Попросить пользователя ввести текст. В результате вывести процент букв в верхнем регистре (заглавные) и в нижнем регистре (прописные).
'''

sm = input("Pls enter the string: ")
sp = sm.count(" ")

low = cap = 0
for i in sm:
	if 'a'<=i<='z':
		low += 1
	elif 'A'<=i<='Z':
		cap += 1
 
print("length of the string: ", len(sm))
print("spaces: ",sp, "\nin percent: %.2f"% (sp/len(sm)*100),"%")
print("%% of lower case letters: %.2f" % (low/len(sm) * 100),"%")
print("%% of capital letters: %.2f" % (cap/len(sm) * 100),"%")
