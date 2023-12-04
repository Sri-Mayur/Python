# Write a python function check whether a number belongs to a fibonacci series or not.

def fib(n):

    a=0
    b=1

    l = [a, b]

    for i in range (n+1):
        c = a+b
        a = b
        b = c

        l.append(c)

    if(n in l):
        return True

    else:
        return False
    


number = int(input("Enter the number: "))

result = fib(number)

if(result):
    print("Fibonacci Member")
else:
    print("Not Fibonacci Member")