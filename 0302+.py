# 2. Напишите функцию который будет конвертировать Фаренгейт в Цельсии и наоборот.

def convert():
	
	far =  int(input("Pls enter the temperature in Farengheit: "))
	cel = int(input("Pls enter the Celcium: "))

	print("\nthe temperature in far", far, "in cel is: " ,round((far-32)*5/9), "\n")
	print("the temperature in cel", cel, "in far is: " ,round(cel*9/5+32),"\n\n")
	return convert

convert()