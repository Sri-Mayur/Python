# Sets are defined by curly braces just like dictionaries

a={9,1,7}
print(a)
print(type(a))
# print(a[0])  TypeError: 'set' object is not subscriptable

b={8,9,10}

print(a-b) #It will remove the element present in a and also present in b

print(b-a) #It will remove the element present in b and also in a

print(a)
print(b)
#The above subtaraction fuctions were just providing a copy of the particular operation
# No change in the original set will occur

# We can use update function

a.difference_update(b)
print(a) 

a.add(5)
print(a)
