# Write a python function check whether a number belongs to a fibonacci series or not.

n = int (input("Enter the number: "))

a, b = 0, 1

while(a <= n):
    if a == n:
         result = True
    a, b = b, a + b

else:
    reselt = False


if(result):
    print("Fibonacci")

else:
    print("Not Fibonacci")

