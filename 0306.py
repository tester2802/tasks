"""
6. Напишите функцию которая подсчитает количество счетных и несчетных чисел в списке чисел.
"""



def change(nums):
	numbers = []
	x = 0
	y = 0
	for i in nums:
		if int(i)%2 == 0:
			x=x+1
		else:
			y=y+1
			
	print("Entered total: ", x+y)
	print("the quantity of Even numbers: ", x)
	print("the quantity of Odd numbers: ", y)

enter_nums = input("Enter the num: ").split(' ')

change(enter_nums)