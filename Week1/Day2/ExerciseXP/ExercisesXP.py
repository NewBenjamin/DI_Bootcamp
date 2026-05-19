#exercice 1
#Instructions:

#Create a set called my_fav_numbers and populate it with your favorite numbers.
#Add two new numbers to the set.
#Remove the last number you added to the set.
#Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
#Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
#Note: Sets are unordered collections, so ensure no duplicate numbers are added.

# Création du premier set
my_fav_numbers = {4, 8, 18}

# Ajouter des nombres
my_fav_numbers.add(7)
my_fav_numbers.add(5)
# Afficher le set
print(my_fav_numbers)

# Supprimer le dernier nombre ajouté
my_fav_numbers.remove(5)

# Afficher après suppression
print(my_fav_numbers)

# Créer le set d'un ami
friend_fav_numbers = {2, 9, 15}

# Afficher le set de l'ami
print(friend_fav_numbers)

# Fusionner les deux sets
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

# Afficher le nouveau set
print(our_fav_numbers)

#------------------------
# Exercise 2: Tuple
# Given a tuple of integers, try to add more integers to the tuple.
# Tuples are immutable, meaning they cannot be changed after creation.

my_tuple = (1, 2, 3)

my_tuple = my_tuple + (4, 5)

print(my_tuple)

#----------------
# 🌟 Exercise 3: List Manipulation
# You have a list:
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
#
# Remove "Banana" from the list.
# Remove "Blueberries" from the list.
# Add "Kiwi" to the end of the list.
# Add "Apples" to the beginning of the list.
# Count how many times "Apples" appear in the list.
# Empty the list.
# Print the final state of the list.

basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove("Banana")
basket.remove("Blueberries")

basket.append("Kiwi")

basket.insert(0, "Apples")

print(basket.count("Apples"))

basket.clear()

print(basket)

#---------------------
# Exercise 4: Floats
# Create a list containing the following sequence:
# 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5
#
# Avoid hard-coding each number manually.

numbers = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]

for i in range(3, 11):
    numbers.append(i / 2)

print(numbers)

#---------------------
# 🌟 Exercise 5: For Loop
# Write a for loop to print all numbers from 1 to 20, inclusive.
# Write another for loop that prints every number from 1 to 20 where the index is even.

for number in range(1, 21):
    print(number)

for index, number in enumerate(range(1, 21)):
    if index % 2 == 0:
        print(number)


#----------------------
# Exercise 6: While Loop
# Use an input to ask the user to enter their name.
# Using a while True loop, check if the user gave a proper name
# (not digits and at least 3 letters long).
# If the input is incorrect, keep asking.
# If the input is correct print “thank you” and break the loop.

while True:

    name = input("Enter your name: ")

    if len(name) >= 3 and not name.isdigit():
        print("thank you")
        break

    print("Incorrect name")


    #-----------------
    # Exercise 7: Favorite Fruits
# Ask the user to input their favorite fruits
# separated by spaces.
#
# Ask the user to input the name of any fruit.
#
# If the fruit is in their list of favorite fruits:
# print:
# "You chose one of your favorite fruits! Enjoy!"
#
# If not:
# print:
# "You chose a new fruit. I hope you enjoy it!"

# 🌟 Exercise 7: Favorite Fruits
# Ask the user to input their favorite fruits
# separated by spaces.
#
# Ask the user to input the name of any fruit.
#
# If the fruit is in their list of favorite fruits:
# print:
# "You chose one of your favorite fruits! Enjoy!"
#
# If not:
# print:
# "You chose a new fruit. I hope you enjoy it!"

favorite_fruits = input("Enter favorite fruits separated by spaces: ")

favorite_fruits_list = favorite_fruits.split()

fruit = input("Enter a fruit: ")

if fruit in favorite_fruits_list:
    print("You chose one of your favorite fruits! Enjoy!")

else:
    print("You chose a new fruit. I hope you enjoy it!")

    #---------------
    # 🌟 Exercise 8: Pizza Toppings
# Write a loop that asks the user to enter pizza toppings one by one.
# Stop the loop when the user types 'quit'.
#
# For each topping entered, print:
# "Adding [topping] to your pizza."
#
# After exiting the loop, print all the toppings
# and the total cost of the pizza.
#
# Base price = $10
# Each topping = +$2.50

# Liste vide pour stocker les toppings
toppings = []

# Constantes de prix
base_price = 10
topping_price = 2.50

# Boucle qui tourne tant qu'on tape pas "quit"
while True:
    topping = input("Entre un ingrédient (ou 'quit' pour terminer) : ")
    
    if topping == "quit":
        break   # SORT de la boucle
    
    # Ajoute le topping à la liste
    toppings.append(topping)
    
    # Affiche le message
    print(f"Adding {topping} to your pizza.")


# Une fois la boucle terminée :

# Calculer le prix total
total_price = base_price + len(toppings) * topping_price

# Afficher le résumé
print(f"\nVoici tes ingrédients : {toppings}")
print(f"Prix total : ${total_price:.2f}")


#----------------
# Exercise 9: Cinemax Tickets
# Ask for the age of each person in a family
# who wants to buy a movie ticket.
#
# Calculate the total cost:
#
# Under 3 years old = free
# Between 3 and 12 = $10
# Over 12 = $15
#
# Print the total ticket cost.

total_cost = 0

while True:

    age = input("Enter age or type quit: ")

    if age == "quit":
        break

    age = int(age)

    if age < 3:
        total_cost += 0

    elif age <= 12:
        total_cost += 10

    else:
        total_cost += 15

print("Total ticket cost:", total_cost)
