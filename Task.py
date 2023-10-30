l1=[]
l2=[]

for i in range (5):
    n=int(input())
    l1.append(n)

for i in range (5):
    m=int(input())
    l2.append(m)



print(l1)
print(l2)



for i in l1:
    if i in l2:
        print(i)