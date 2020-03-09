# Lesson 030720
# and or not
"""
point = int(input("Enter your point: "))
if point == 5:
	print("Great!")
elif point == 4:
	print("Little bit")
elif point == 3:
	print("bad result..")
else:
	print("You should try to study..")


#python.kg - Check if the user have account in FB nd GH by True and "and" operators
is_user_fbuser = True
is_user_github_user = True

if is_user_fbuser and is_user_github_user:
	print("You can enter to the system")
else:
	print("You should have FB and GitHub accounts")

is_user_fbuser = True
is_user_github_user = True
is_user_age_greater_18 = False
user_account_money = 10100

if is_user_fbuser and is_user_github_user and is_user_age_greater_18 or user_account_money<10100:
	print("You can enter to the system")
else:
	print("sorry, you should have to own accounts in fb and gh and also your shoule be elder 18 and have funds more that 10100")


user_is_authenticated = True
user_has_insta = True
user_has_gitlab = True

if user_is_authenticated:
	print("User is authenticated")

if user_has_insta:
	print("User has Instagram account")

elif user_has_gitlab:
	print("User has gitlab account")
"""

# Sample for 
""" 
[1-100]
3 == foo
5 == bar
3 and 5 foobar


numbers = list(range(1,50))
for num in numbers:
	if num%3 == 0 and num%5 == 0:
		print(num, ": foobar")
	elif num%5 == 0:
		print(num, ": bar")
	elif num%3 == 0:
		print(num, ": foo")
	else:
		continue


# Sample of IF conditions

work_experience = 10
has_JS = False
has_python = True
has_golang = True

if work_experience >=10:
	print("Block1 ")
	print("you are seniour razrab")
	if has_python:
		print("Goood. Yo know Python!")
		if has_golang and has_JS:
			print("You know JS and Golang")
		print("Molodets!")
	print("You do know many programming languages!")
	print("continue of the Block1")


# LOOPS (for / while)
rng = int(input("range: "))
for x in range (0,rng,3): # _ if we do not use x or i
	print(x," :you cant handle without loops")


# SAMPLE
pizza = ['first_item','second_item','third_item','fourth_item','fifth_item','sixth_item','seventh_item','and_the_last_item']


# need to replace the first word
enumeration = []

for item in pizza:
	new_item0 = item.split('_')[0].upper()
	new_itemboth = item.split('_')
	print(new_item0)
	print(new_itemboth)
	enumeration.append(new_item0.title())
	print(enumeration)
	#print("eating",item,"of pizza")


str_ = "hello"
iterator = str_.__iter__()
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(type(iterator))

word = "this is the new sentence"
print (word)
new_word = word.split(" ")
print(new_word)
iterator = new_word.__iter__()
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


# Sample с дан башталгандарды откоруп жиберет, т дан башталганда токтойт
pizza = ['first_item','second_item','third_item','fourth_item','fifth_item','sixth_item','seventh_item','and_the_last_item']



enumeration = []

for item in pizza:
	new_item = item.split('_')[0]
	if new_item.startswith('s'):
		continue
	elif new_item.startswith('t'):
		break
	enumeration.append(new_item.title())
print(enumeration)

"""

# Sample с дан башталгандарды откоруп жиберет, т дан башталганда токтойт
pizza = ['first_item','second_item','third_item','fourth_item','fifth_item','sixth_item','seventh_item','and_the_last_item']

for index, item in enumerate(pizza):
	print("This is index",index,'and item ---', item)
	new_item = item.split('_')[0]

# Множественное перестановка
a = [1, 2, 3]
b = [4, 5, 6]
print("\n")
print ('a:',a)
print ('b:',b)
a, b = b, a
print("\nResult of replacing:\n")
print ('a:',a)
print ('b:',b)