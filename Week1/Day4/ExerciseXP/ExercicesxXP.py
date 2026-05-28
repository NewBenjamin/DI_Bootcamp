# EXERCISE 1
def display_message():
    print("I am learning about functions in Python.")

display_message()


# EXERCISE 2
def favorite_book(title):
    print(f"One of my favorite books is {title}.")

favorite_book("Alice in Wonderland")
favorite_book("The Great Gatsby")
favorite_book("1984")


# EXERCISE 3
def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}.")

describe_city("Reykjavik", "Iceland")
describe_city("Paris")
describe_city("Tokyo", "Japan")
describe_city("Berlin")


# EXERCISE 4
import random

def guess_number(my_guess):
    random_number = random.randint(1, 100)
    
    if my_guess == random_number:
        print("Success!")
    else:
        print(f"Fail! Your number: {my_guess}, Random number: {random_number}")

guess_number(50)
guess_number(75)
guess_number(42)


# EXERCISE 5
def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}.")

make_shirt()
make_shirt(size="medium")
make_shirt(size="small", text="Hello!")
make_shirt(text="Code is Fun", size="extra large")


# EXERCISE 6
def show_magicians(magician_names):
    for magician in magician_names:
        print(magician)

def make_great(magician_names):
    for i in range(len(magician_names)):
        magician_names[i] = magician_names[i] + " the Great"

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
make_great(magician_names)
show_magicians(magician_names)


# EXERCISE 7
import random

def get_random_temp():
    return random.randint(-10, 40)

def main():
    temperature = get_random_temp()
    print(f"The temperature right now is {temperature} degrees Celsius.")
    
    if temperature < 0:
        print("Brrr, that's freezing! Wear some extra layers today.")
    elif temperature < 16:
        print("Quite chilly! Don't forget your coat.")
    elif temperature < 23:
        print("Nice weather.")
    elif temperature < 32:
        print("A bit warm, stay hydrated.")
    else:
        print("It's really hot! Stay cool.")

main()