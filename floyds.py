n=int(input("Enter the number of rows: "))
print("Floyd's triangle is :")
num = 1
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
    print()