############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?: "))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")
# else:
#     print("You're older than expected")

# # Fix the Errors
# age = int(input("How old are you? "))
# if age > 18:
#     print(f"You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)
# list_tiem = [1,2,3,5,8,13]
# mutate(list_tiem)

# # Even and odd number debugging
# number = int(input("What number do you want to check ? "))
# if number % 2 == 0:
#     print("It's an even number")
# else:
#     print("It's an odd number")

# # Leap year debugging
# year = int(input("Enter the year : "))
# if year%4 == 0:
#     if year%100 == 0:
#         if year%400 == 0:
#             print("It's a leap year")
#         else:
#             print("Not a leap year")
#     else:
#         print("It's a leap year")
# else:
#     print("It's not a leap year")

# So today we basically had to do with debugging. 
# I learnt several debugging steps and thats quite amazing how several steps can help solve s little bug in an entire code
# I can give you a tip and that'll be to always run your code when you finish a line and when you get stucked, tryout stackOverflow.
