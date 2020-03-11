"""
10. Напишите функцию которая определит сколько раз встречается элемент в списке.
"""
def howmanytimes():
	nums = [int(i) for i in input("\nEnter the list of numbers:\n").split()] #filling the list with numbers
	check = int(input("checking number: ")) #enter the number to check how many times it's been entred
	print("Answer: The number",check,"entered",nums.count(check),"times") #print the qn of the given number

howmanytimes()
howmanytimes()