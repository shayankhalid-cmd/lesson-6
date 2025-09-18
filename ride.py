print("select your ride")
print ("1:bike")
print ("2:car")
choice=int(input("enter your choice as 1 or 2:"))
if (choice==1):
    print("what type of bike?")
    print ("1:scooty")
    print("2:scooter")
    ch1=int(input("enter bike type"))
    if (ch1==1):
        print("you have selected scooty")
    else:
        print("you have selected scooter")


elif (choice==2):
    print("what type of car?")
    print ("1:lamborghini revuelto")
    print("2:audi r8")
    ch1=int(input("enter car type"))
    if (ch1==1):
        print("you have selected lamborghini revuelto")
    else:
        print("you have selected audi r8")
else:
    print("invalid type")