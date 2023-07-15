travel_log = [
    {
        "country":"Cameroon",
        "cities":["Yaoundé", "Douala", "Bamenda"], 
        "visits":32
    },
    {
        "country":"United_Kingdom", 
        "cities":["London", "Bermingham", "Manchester"], 
        "visits":25
    }, 
]
def add_new_country(country_visited, cities_visited, Monuments_visited):
    new_country = {}    #Creating a new dictionary so as to fill in different arguements
    new_country["country"]= country_visited
    new_country["cities"] = cities_visited 
    new_country["visits"] = Monuments_visited
    travel_log.append(new_country) # Here we append the newly created dictionary to our travel_log list

Country = input("\nEnter country name : ")
Cities = input("Enter places you visited : ").split(", ")
Visits = int(input("How many time did you visit this palce : "))

add_new_country(Country, Cities, Visits)
print(travel_log)