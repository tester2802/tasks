"""
2. N students take K apples and distribute them among each other evenly.
The remaining (the undivisible) part remains in the basket.
How many apples will each single student get?
How many apples will remain in the basket?
The program reads the numbers N and K.
It should print the two answers for the questions above.
Each N student will take K apples, and remains X)
"""
stud = int(input("How many students? "))
apl = int(input("How many apples? "))
x=int(apl/stud)
print("for each stud: ", x)
print("remain: ", apl-x*stud)