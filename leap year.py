a=int(input("enter the year:"))
if a%400==0:
    leapyear=True
elif a%100==0:
    leapyear=False
elif a%4==0:
    leapyear=True
else:
    leapyear=False
if leapyear:
    print(a,'is a leapyear')
else:
    print(a,'is not a leapyear')
