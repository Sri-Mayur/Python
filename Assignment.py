year= int(input("Enter the year:"))

if(year%4==0):
    feb=29
else:
    feb=28


if(1917>year>1700):
    d=256-(31+feb+31+30+31+30+31+31)

elif(year==1918):
    d=256-(31+15+31+30+31+30+31+31)

else:
    if((year%400==0) and (year%4==0 and year%100!=0)):
        feb=29
    else:
        feb=28

    d=256-(31+feb+31+30+31+30+31+31)

print(str(d), '09',  str(year), sep=".")