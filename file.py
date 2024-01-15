fo= open('abc.txt', 'r')

fz = open('xyz.txt', 'r')

#z = fz.writelines("Kamran \n Mayur \n Dhruv \n Prateek")
z = fz.read()
print(z)

r  = fo.readlines() #['Hi \n', ' How are you? \n', " I'm fine"]
# t = fo.readline() #Hi 

print(r)
fo.close()