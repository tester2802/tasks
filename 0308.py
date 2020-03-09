"""
8. Напишите функцию где дан список целых чисел.
Заменить отрицательные на -1, положительные - на число 1, ноль оставить без изменений.
"""


def change(nums):
	numbers = []
	for i in nums:
		if int(i)>0:
			numbers.append(1)
		elif int(i)<0:
			numbers.append(-1)
		elif int(i)==0:
			numbers.append(0)
		else:
			continue
	print("Changed_nums: ", numbers)

enter_nums = input("Enter the num: ").split(' ')

change(enter_nums)