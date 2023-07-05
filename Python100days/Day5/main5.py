# the range(a) funct returns an object that produces a seq of int 
   

# meals = ['Achu', 'Eru', 'Friedrice', 'Okok']
# number = [1,2,3,4,5,6]
# print(number)
# for food in meals:
#     print(food)
# print((len(meals)))
# a = 3.5545222
# print(round(a))

# student_height = input("Input list of Students : ").split()

# for number in range(len(student_height)):
#     student_height[number] = int(student_height[number])
# # print(student_height)
# total_height = 0
# for a_height in student_height:
#     total_height += a_height
# # print(total_height)
# total_students = 0
# for a_height in student_height:
#     total_students += 1
# # average_height = total_height / len(student_height) 
# average_height = total_height / total_students
# print(f"Average height is {round(average_height)}")

# scores = input("Enter the lsit of scores: ").split()
# for a_score in range(len(scores)):
#     scores[a_score] = int(scores[a_score])
# # sum_score = 0
# # for get_score in scores:
# #     sum_score += get_score
# # total_scores = 0
# # for get_score in scores:
# #     total_scores+=1
# # Average = round(sum_score/total_scores)
# # print(Average)
# highest_score = 0
# for another_score in scores:
#     # if another_score > Average:
#     if another_score > highest_score:
#         highest_score = another_score
# print(highest_score)

# print(scores)
# highest_score= max(scores)
# print(highest_score)
# number1 = int(input("Where do you want to start : "))
# number2 = int(input("Where do you want to stop : "))

# summer = 0
# for summing in range(0, 101, 2):
#     summer += summing
# # print(range(number1, number2))
# print (summer)

# for a_number in range(1, 101):
#     if a_number % 3 == 0 and a_number % 5 == 0:
#         print("FizzBuzz")
#     elif a_number % 5 == 0:
#         print("Buzz")
#     elif a_number % 3 == 0:
#         print("Fizz")
#     else:
#         print(a_number)

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
        'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 
        'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 
        'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 
        'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcom to Andy's Password Generator!!")
number_letters = int(input("How many Letters do you want in your passowrd ? \n"))
number_numbers = int(input("How many Numbers do you want ?\n"))
number_symbols = int(input("How many Symbols do you want ?\n"))


# rand_letters=random.sample(letters, number_letters)
# rand_numbers=random.sample(numbers, number_numbers)
# rand_symbols=random.sample(symbols, number_symbols)
# print(rand_letters+rand_numbers+rand_symbols)
rand_letters = ''
for new_letter in range(1, number_letters+1):
    rand_letters += random.choice(letters)
    
rand_numbers = ''
for new_number in range(1, number_numbers+1):
    rand_numbers += random.choice(numbers)
    
rand_symbols =''
for new_symbol in range(1, number_symbols+1):
    rand_symbols += random.choice(symbols)

password = rand_letters + rand_numbers + rand_symbols
print(f"Your password is : {password}")
# summing = number_letters+number_numbers+number_symbols
# print(random.sample(password, summing))
new_password = ''.join(random.sample(password, len(password)))
print(f"Your new password is : {new_password}")
