# Love Calculator
print("Welcome to the Love Calculator!")
name1 = input("Enter your name : ")
name2 = input("Enter their name : ")
name3 = name1 + name2
lower_case_name = name3.lower()
# Converting the Names to 
number_T = lower_case_name.count('t')# print(f"T occurs {number_T} times")
number_R = lower_case_name.count('r')# print(f"R occurs {number_R} times")
number_U = lower_case_name.count('u')# print(f"U occurs {number_U} times")
number_E = lower_case_name.count('e')# print(f"E occurs {number_E} times")

total1 = number_T + number_R + number_U + number_E # Getting total for TRUE

number_L = lower_case_name.count('l')# print(f"L occurs {number_L} times")
number_O = lower_case_name.count('o')# print(f"O occurs {number_O} times")
number_V = lower_case_name.count('v')# print(f"V occurs {number_V} times")
number_E = lower_case_name.count('e')# print(f"E occurs {number_E} times")

total2 = number_L + number_O + number_V + number_E # Getting total for LOVE

Love = int(str(total1)+str(total2)) # Summing the 2 totals as strings and converting to integer

if Love < 10 or Love > 90:
    print(f"Your score is {Love}%, you go together like coke and mentos.\n")
elif 40 <= Love <= 50:
    print(f"Your score is {Love}%, you are alright together.\n")
else:
    print(f"Your score is {Love}%\n")