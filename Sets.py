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

a.discard(7)
print(a)

a.clear()
print(a)

c=b
print(c)
b.discard(9)
print(b)
print(c)

# The changes which we have done on b will directly affect c as well
# a+b and a*b can't be use

print(10 in b)

c.add(12)

print(b.intersection(c))

print(a.intersection(c))
print(a.union(b))


x={}
print(type(x)) # Dictionary <class 'dict'>

s=set()
print(type(s)) # Set  <class 'set'>

m='1 2 3 4'
m.split()
print(m)
m= type[int]  #Generic Alias

print(type(m))