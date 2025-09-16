v = int(input("enter the value here:"))
w = int(input("enter the value here:"))
x = int(input("enter the value here:"))
y = int(input("enter the value here:"))
z = (v+w)*x / y
print ("value of (v+w)*x / y : ", z)
result = v+(w*x)//y
print("the result of v+(w*x)//y :",result)

name = (input("enter your name here:"))
age = int(input("enter your age here:"))
if (name == "shayan" or name == "alex") and age >= 2:
    print ("hello! welcome")
else:
    print ("good bye")