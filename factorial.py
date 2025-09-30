def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n - 1)
print ("the factorial of 0",factorial(0))
print ("the factorial of 1",factorial(1))
print ("the factorial of 2",factorial(2))
print ("the factorial of 3",factorial(3))
print ("the factorial of 4",factorial(4))
print ("the factorial of 5",factorial(5))
print ("the factorial of 10",factorial(10))