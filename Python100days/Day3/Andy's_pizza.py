print("Welcome to Andy's Pizzas")
size = input("What pizza size do you want? S, M or L : ").lower()
pepperoni = input("Do you want pepperoni? Y or N : ").lower()
cheese = input("Do you want cheese? Y or N : ").lower()
bill = 0
# Small size pizza calculation
if size == 's':
    bill = 15
    print("Small Pizza : $15")
    if pepperoni == 'y':
        bill += 2
        print("Pepperoni for Small Pizza : +$2")
    if cheese == 'y':
        bill += 1
        print("Extra cheese for Pizza : +$1")
    print(f"Your final bill is : ${bill}")
# Medium size pizza calculation
elif size == 'm':
    bill = 20
    print("Medium Pizza : $20")
    if pepperoni == 'y':
        bill += 3
        print("Pepperoni for Medium Pizza : +$3")
    if cheese == 'y':
        bill += 1
        print("Extra cheese for Pizza : +$1")
    print(f"Your final bill is : ${bill}")
# Large size pizza calculation
elif size == 'l':
    bill = 25
    print("Large Pizza : $25")
    if pepperoni == 'y':
        bill += 3
        print("Pepperoni for Large Pizza : +$3")
    if cheese == 'y':
        bill += 1
        print("Extra cheese for Pizza : +$1")
    print(f"Your final bill is : ${bill}")
 
else:
    print("No such Pizza size exist here")

# # Another one
# size = input("What pizza size do you want? S, M or L : ").lower()
# pepperoni = input("Do you want pepperoni? Y or N : ").lower()
# cheese = input("Do you want cheese? Y or N : ").lower()
# bill = 0

# if size =='s':
#     bill +=15
# if size =='m':
#     bill +=20
# if size =='l':
#     bill +=25
    
# if pepperoni == 'y':
#     if size == 's':
#         bill += 2
#     else:
#         bill += 3

# if cheese == 'y':
#     bill += 1

# print(f"Your Final bill is : ${bill}")