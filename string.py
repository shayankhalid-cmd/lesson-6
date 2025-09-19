string1= input("Enter a string: ")
print ("entered string is: ", string1)
reversed_string = ('')
for i in string1:
    reversed_string = i + reversed_string
    print ("the original string is: ", string1)
    print ("the reversed string is: ", reversed_string)