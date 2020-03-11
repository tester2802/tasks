"""
7. Напишите функцию где исходный список содержит положительные и отрицательные числа.
Требуется положительные поместить в один список, а отрицательные - в другой.
"""

def posneg(nums):
	pos_num = []
	neg_num = []
	pos = 0
	neg = 0
	zero = 0
	for i in nums:
		if int(i) > 0:
			pos_num.append(i)
			pos += 1
		elif int(i) == 0:
			zero += 1
			continue
		else:
			neg_num.append(i)
			neg += 1
	
	print("total numbers: ", pos+neg, "from the list 0 are:", zero)		
	print(pos, "positive numbers: ", pos_num)
	print(neg, "negative numbers: ", neg_num)
	# print(zero, ":0")

enter_nums = input("Enter the num: ").split(' ')

posneg(enter_nums)