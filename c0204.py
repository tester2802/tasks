'''
4) Minimal positive integer: Find minimal positive integer that is not in list.
Example: [1,2,3,4,6] - Answer 5
Example: [1,2,3] - Answer 4
Example: [-1, -2, -6] - Answer 1
Create effective algorithm
'''

# ml = int(input("Enter the list of numbers: "))
# next(i for i, e in enumerate(sorted(a) + [None], 1) if i != e)
# print(enumerate(ml))
# next(a for a, b in enumerate(myList, 1) if a != b)

l = [1,2,3,5,7,8,-77,12,14,0,9,19]
m = range(1,len(l))
print("l:",l)
print("m:",m)
print("len(l):",len(l))
print("set(m)",set(m))
print("set(l)",set(l))
print("result:",min(set(m)-set(l)))