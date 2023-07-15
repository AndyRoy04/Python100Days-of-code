
# programming_dictionary ={
#     "Bug":"An error from a program that prevents it from running as expected",
#     "Function": "A piece of code that you can easily call again in a program",
# }
#retrieving items from a list
# print(programming_dictionary["Loop"])

# Adding new items to a dictionary or editing
# programming_dictionary["Loops"] = "The action of doing something over and over again"
# print(programming_dictionary)

# Creating an empty dictiionary
# new_dic = {}

# Wipe an existing dictionary
# programming_dictionary = {}

# Loop through a dictionary
# for key in programming_dictionary:
#     print(programming_dictionary[key])

# Grading
# student_scores = {
#     "Neville" : 85,
#     "Harry" : 79,
#     "Randy" : 68,
#     "Gerald" : 80,
#     "Angela" : 99,
# }
# student_grades = {}#creating a new list to store students grade
# for student in student_scores: # Looping through the previous list to get students score and assigning them grades
#     print(student)
#     if 91 <= student_scores[student] <= 100:
#         student_grades[student] = "Outstanding"
#     elif 81<= student_scores[student]<=90:
#         student_grades[student] = "Exceeds Expectation"
#     elif 71<=student_scores[student]<=80:
#         student_grades[student] = "Acceptable" 
#     elif student_scores[student]<71:
#         student_grades[student] = "Fail" 
# print(student_grades) 

# capitals = {
#     "Cameroon":"Yaoundé",
#     "United Kingdom": "London",
# }
# # Nesting a list in a dictionary
# travel_log = {
#     "Cameroon":["Yaoundé", "Douala", "Bamenda"],
#     "United Kingdom" : ["London", "Bermingham", "Manchester"], 
# }
# Nesting a dictionary in dictionary
# travel_log = {
#     "Cameroon": {"cities_visited":["Yaoundé", "Douala", "Bamenda"], "Monuments_visited":32},
#     "United_Kingdom" : {"popular_cities":["London", "Bermingham", "Manchester"], "popular_dishes":["fries", "Pizza"]}, 
# }
# Nesting a dictionaries in lists
# travel_log = [
#     {
#         "Country":"Cameroon",
#         "cities_visited":["Yaoundé", "Douala", "Bamenda"], 
#         "Monuments_visited":32
#     },
#     {
#         "Country":"United_Kingdom", 
#         "popular_cities":["London", "Bermingham", "Manchester"], 
#         "popular_dishes":["fries", "Pizza"]
#     }, 
# ]
# Dictionary in list
# import os
# os.system('cls')
# a = 'Welcome to Antana'
# print(a.center(90, '#'))
# travel_log = [
#     {
#         "country":"Cameroon",
#         "cities":["Yaoundé", "Douala", "Bamenda"], 
#         "visits":32
#     },
#     {
#         "country":"United_Kingdom", 
#         "cities":["London", "Bermingham", "Manchester"], 
#         "visits":25
#     }, 
# ]
# def add_new_country(country_visited, cities_visited, Monuments_visited):
#     new_country = {}  #Creating a new dictionary so as to fill in different arguements
#     new_country["country"]= country_visited
#     new_country["cities"] = cities_visited 
#     new_country["visits"] = Monuments_visited
#     travel_log.append(new_country)  # Here we append the newly created dictionary to our travel_log list
#     os.system("cls")  # To cls the screen after the above has been processed
# Country = input("\nEnter country name : ")
# Cities = input("Enter places you visited : ").split(", ")
# Visits = int(input("How many time did you visit this palce : "))
# add_new_country(Country, Cities, Visits) # calling the Function
# print(f"\n{travel_log}\n")

# Secret auction program 🔨
import os   #We import the OS module so as to use the os.system(cls) funtion to wipe the screen after a bid has been made
import art
Bidders_Dictionary = {} # creating our empty dictionary
answer = True
def register_bids(Records):
    highest = 0
    winner = ""
    for bidder in Records: #Loop through our list to get the highest bid and the bidders name
        amount = Records[bidder]
        if amount > highest:
            highest = amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest}")

print(art.logo)
print("\nWelcome to the secret auction Bid Game.\n")
while answer:
    Bidders_name = input("Bidder enter your name : ")
    Bidders_bid = int(input("Whats your Bid ? : $"))

    Bidders_Dictionary[Bidders_name] = Bidders_bid # Here a dictionary was created and it stores, key="bidders_name", value="bidders_bid"
    check = input("Are there other Bidders around ? Type 'Yes' or 'No'\n").lower()    
    if check == "yes":
        answer = True        
        os.system("cls")  # Clear screen after bid is placed and there are other bidders
    else:
        answer = False
        register_bids(Bidders_Dictionary)  # Executing the main function when there are no more bidders
        # os.system("cls")