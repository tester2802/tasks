"""
6. Напишите функцию которая подсчитает количество четных и нечетных чисел в списке чисел.
"""

def evenORodd(nums):
	numbers = []
	x = 0
	y = 0
	for i in nums:
		if int(i)%2 == 0:
			x+=1
		else:
			y+=1
			
	print("Entered total: ", x+y, "numbers")
	print("the quantity of _Even_ numbers: ", x)
	print("the quantity of _Odd_ numbers: ", y)

enter_nums = input("Enter the num: ").split(' ')

evenORodd(enter_nums)