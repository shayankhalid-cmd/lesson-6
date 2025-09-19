n = int(input("Enter the number of terms to be added: "))
sum = 0
for i in range(1, n+1):
    print("for i =",i)
    print ("sum=",sum, "+",i)
    sum = sum + i
    print("sum =",sum)
