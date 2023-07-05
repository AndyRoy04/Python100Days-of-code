# Tip calculator
print("Welcome to the tip calculator !")
total_bill = float(input("Enter the total bill in FCFA : "))
tip = float(input("Enter the percentage tip you'll like to give : "))
people = int(input("Enter the number of People to split the bill to : "))
tip_bill = total_bill * (tip)/100
net_bill = total_bill + tip_bill
bill = net_bill / people
the_bill = round(bill, 2)
# the_bill = "{:.2f}".format(bill) #converting a float to 2dp string
print(f"Each person is to pay : {the_bill}")