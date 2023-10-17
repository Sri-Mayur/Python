l=[]
m=[1,2,34,5,6,6]
n=int(input("Enter the size of the list:"))

for i in range (n):
    t=(input())
    l.append(t)
    m.extend(t)


print(type(l))

print(type(m))

print(l)
print(m)