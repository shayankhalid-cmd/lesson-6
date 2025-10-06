valid = False
while not valid:
    try:
        n = int(input("enter a number that is not zero: "))
        while n % 2 == 0:
            print("bye bye")
            valid = True
    except ValueError:
        print("invalid")