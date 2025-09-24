n=int(input("enter the number of rows: "))
print ("right angle triangle is :")
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()