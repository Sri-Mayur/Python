a = input()
b = input()

d1, m1, y1 = a.split()
d2, m2, y2 = b.split()

d1 = int(d1)
m1 = int(m1)
y1 = int(y1)

d2 = int(d2)
m2 = int(m2)
y2 = int(y2)

if(d2>=d1 and m2>=m1 and y2>=y1):
    print("0")

elif(d2<=d1 and m2==m1 and y2==y1):
    print((d1-d2)*15)

elif(m2<m1):
    print((m1-m2)*500)

elif(y2<y1):
    print("10000")