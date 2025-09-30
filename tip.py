def total_calc(bill_amount,tip_perc):
    total = bill_amount*(1+ 0.01*tip_perc)
    total= round(total,2)
    print (f"please pay ${total}")
amount = int(input("enter bill amount:"))
tip = int(input("enter tip percentage:"))
total_calc(amount,tip)