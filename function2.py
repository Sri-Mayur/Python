# Write a function to find even sum

def evenSum(*l):

    for i in l:
        
        if(i%2 == 0):
            sum = sum + i

    return sum


n = int(input("Enter the size of list: "))
 
l = []

for i in range (n):
    t=(input())
    l.append(t)

evenSum(l)