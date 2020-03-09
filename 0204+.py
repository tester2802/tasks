"""
4. A timestamp is three numbers: a number of hours, minutes and seconds.
Given two timestamps, calculate how many seconds is between them. The
moment of the first timestamp occurred before the moment of the second
timestamp. (На английском языке, чтобы Вы научились 6, 1, 30, 6, 2, 10 result 40 sec.)
"""
hour1 = int(input("pls, enter the 1-hour "))
min1 = int(input("pls, enter the 1-min "))
sec1 = int(input("pls, enter the 1-sec "))
t1 = hour1*60*60+min1*60+sec1
print("\n time1 in sec: ",t1)

hour2 = int(input("\npls, enter the 2-hour "))
min2 = int(input("pls, enter the 2-min "))
sec2 = int(input("pls, enter the 2-sec "))
t2 = hour2*60*60+min2*60+sec2
print("\n time2 in sec: ",t2)

print("\n difference: \n", t2-t1, "in sec.\n", int((t2-t1)/60), "in min.\n", int((t2-t1)/60/60), "hour")