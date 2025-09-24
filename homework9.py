n=int(input("Enter a number: "))
rev = 0
t=n
while t>0:
    rem=t%10
    rev=rev*10+rem
    t=t//10
print("reversed number:",rev)
print("biniary number for given",n, ":",bin(n))