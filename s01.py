x = int(input("Enter the number 5 digit: "))
a = x//10000
b = x//1000%10
c = x//100%10
d = x//10%10
e = x%10

print(a,b,c,d,e)
print(a+b+c+d+e)