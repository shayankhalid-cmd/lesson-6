num = int(input("Enter a number: "))
temp = num
count = 0
while temp > 0:
    digit = temp % 10
    rev = rev*10+digit
    count = count+1
    temp //= 10
    print("reverse of given number is:", rev)
    print ("no. of digits:", count)