list1 =[]
list2=[]
list3=list1
print(list1==list2)# This will give true because value of list1 is equal to list2

print(list1 is list2) #This will give false because index is different.

print(list1 is list3)
list3=list2+list1
print(list1 is list3)

l=[3]
f=[3]
print(l is f) #Again False because both have different address
print(l in f) 
