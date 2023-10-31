l1=[1,2,3,4,5]

l1.extend([7,8,9])

print(l1)

l1.append([11,12])
print(l1)



for i in l1:
    print(i*2, sep=" ")


print(l1*2)

l1.pop(8)

print(l1)

l1.remove(8)

print(l1)

l2=['a','b','c']
l2.remove('b')
print(min(l2))
print(max(l2))
print(l2)
# l3=[1,'a',True,'b']
# print(max(l3))         It will give error because string and integer can't be compared

l3=[1,6,8,True,False]

l3.remove(0)

print(l3)