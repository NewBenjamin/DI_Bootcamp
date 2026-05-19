#Exercise 1: Converting Lists into Dictionaries

# Instructions:
# You are given two lists. Convert them into a dictionary
# where the first list contains the keys and
# the second list contains the corresponding values.

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result = dict(zip(keys, values))
print(result)

# 🌟 Exercise 2: Cinemax #2

# Instructions:
# Write a program that calculates the total cost
# of movie tickets for a family based on their ages.

# Ticket pricing rules:
# Under 3 years old: Free
# 3 to 12 years old: $10
# Over 12 years old: $15

family = {
    "rick": 43,
    "beth": 13,
    "morty": 5,
    "summer": 8
}

total_cost = 0

for name, age in family.items():

    if age < 3:
        price = 0

    elif age <= 12:
        price = 10

    else:
        price = 15

    print(f"{name} has to pay ${price}")

    total_cost += price

print(f"Total cost: ${total_cost}")

#Exercise 3: Zara

# Instructions:
# Create and manipulate a dictionary
# that contains information about the Zara brand.

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

# Change the value of number_stores to 2
brand["number_stores"] = 2

# Print a sentence describing Zara’s clients
print(f"Zara's clients are: {brand['type_of_clothes']}")

# Add a new key country_creation with the value Spain
brand["country_creation"] = "Spain"

# Add “Desigual” to the competitors list
brand["international_competitors"].append("Desigual")

# Delete the creation_date key
brand.pop("creation_date")

# Print the last item in international_competitors
print(brand["international_competitors"][-1])

# Print the major colors in the US
print(brand["major_color"]["US"])

# Print the number of keys in the dictionary
print(len(brand))

# Print all keys of the dictionary
print(brand.keys())


# 🌟 Exercise 4: Disney Characters

# Instructions:
# Create three dictionaries based on different patterns.

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# 1. Create a dictionary that maps characters to their indices

disney_users_A = {}

for index, name in enumerate(users):
    disney_users_A[name] = index

print(disney_users_A)

# 2. Create a dictionary that maps indices to characters

disney_users_B = {}

for index, name in enumerate(users):
    disney_users_B[index] = name

print(disney_users_B)

# 3. Create a dictionary where characters are sorted alphabetically
# and mapped to their indices

sorted_users = sorted(users)

disney_users_C = {}

for index, name in enumerate(sorted_users):
    disney_users_C[name] = index

print(disney_users_C)
