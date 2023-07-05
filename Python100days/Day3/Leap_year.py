print("Welcom to the Leap year calculator.")
year = int(input("What year do you want to check  : "))
new_year1 = year % 4
new_year2 = year % 100
new_year3 = year % 400
# if new_year1 == 0:
#     if new_year2 == 0:
#         if new_year3 == 0:
#             print("It's a Leap year")
#         else:
#             print("Not a Leap Year")
#     else:
#         print("It'a a Leap Year")
# else:
#     print("Not a Leap Year")
if new_year1 == 0 and new_year2 != 0 or new_year3 == 0:
    print("It's a Leap year")
else:
    print("Not a Leap Year")