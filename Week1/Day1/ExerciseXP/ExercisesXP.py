# ============================================
# DI Bootcamp - Week 1 - Day 1 - Exercises XP
# Author: Benjamin Ehrlich
# ============================================


# ----------------------------------------------
# Exercise 1: Hello World
# Instructions:
# Print "Hello world" 4 times in one line of code
# ----------------------------------------------
print("Hello world\n" * 4)


# ----------------------------------------------
# Exercise 2: Some Math
# Instructions:
# Calculate (99^3)*8
# ----------------------------------------------
print((99 ** 3) * 8)


# ----------------------------------------------
# 
# Exercise 3: What is the output?
# Predict, then verify
# ----------------------------------------------
print(5 < 3)            # Prédiction : False
print(3 == 3)           # Prédiction : True
print(3 == "3")         # Prédiction : False
# print("3" > 3)        # (TypeError) (This will raise an error because you cannot compare a string and an integer)
print("Hello" == "hello") # Prédiction : False

# ----------------------------------------------
# Exercise 4: Your Computer Brand
computeur_brand = "Mac"
print("I have a " + computeur_brand + " computer")


# ----------------------------------------------
# Exercise 5: Your information
# Instructions:
# Create variables name, age, shoe_size, info
# Print info with a sentence containing all 3 variables
# ----------------------------------------------

name = "Benjamin"                
age = 36                         
shoe_size = 47                  

info = f"Hi, my name is {name}, I am {age} years old, and my shoe size is {shoe_size}."

print(info)
# ----------------------------------------------
# Exercise 6: A & B
# Instructions:
# Create two variables, a and b
# If a is bigger than b, display "Hello World"

a = 5
b = 4
if a > b:
    print("Hello World")

#-----------------------------------------------
# Exercise 7: Odd or Even
# Instructions:
# Write code that asks the user for a number and determines whether this number is odd or even.
number = input("Please enter a number: ")
number = int(number)  # Convert the input to an integer
if number % 2 == 0:
    print(f"{number} is an even number.")
else:    print(f"{number} is an odd number.")

# -----------------------------------------------
# Exercise 8: What is your name?
# Instructions:
#Write code that asks the user for their name and determines whether or not you have the same name. Print out a funny message based on the outcome.
name = input("Please enter your name: ")
if name == "Benjamin":
    print("Wow, we have the same name! That's pretty cool!")
else:
    print(f"Nice to meet you, {name}! But I prefer the name Benjamin, it's just so unique and awesome!")

# -----------------------------------------------
# Exercise 9: Tall enough to ride a roller coaster
# Instructions:
# Write code that will ask the user for their height in centimeters.
# If they are over 145 cm, print a message that states they are tall enough to ride.
# If they are not tall enough, print a message that says they need to grow some more to ride.
height = int(input("What is your height in centimeters? "))
if height > 145:
    print("You are tall enough to ride the roller coaster! Enjoy!")
else:    print("Sorry, you need to grow some more to ride the roller coaster. Keep growing and come back soon!")