#Create a list which contains multiple of 3 or 5

l=[]

for i in range (1,51):
    if(i%3==0 or i%5==0):
        l.append(i)

print(l)


l2=[i for i in range(1,51) if(i%3==0 or i%5==0)]

print(l2)
