sentence = input("Enter the string: ")
words = sentence.split()

print("Even length words in the string: ")

for i in words:
    if len(i) % 2 == 0:
        print(i)