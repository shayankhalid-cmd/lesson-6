string = input("Enter own word: ")
char = input("Enter own character: ")
i = 0
count = 0
while i < len(string):
    if string[i] == char:
        count = count + 1
    i = i + 1
print ("the total number of times", char, "has occurred is:", count)