import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist).upper()

guessed_letters = []
correct_guesses = []
wrong_guesses = 0
max_wrong = 6

def display_hangman(wrong):
    stages = [
        "  +---+\n  |   |\n      |\n      |\n      |\n      |\n  =========",
        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n  =========",
        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n  =========",
        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n  =========",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n  =========",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n  =========",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n  ========="
    ]
    return stages[wrong]

def display_word(word, guessed):
    display = ""
    for letter in word:
        if letter in guessed or letter == " ":
            display += letter
        else:
            display += "*"
    return display

while wrong_guesses < max_wrong:
    print(display_hangman(wrong_guesses))
    print("\nWord: " + display_word(word, correct_guesses))
    print("Guessed letters: " + ", ".join(guessed_letters))
    
    if display_word(word, correct_guesses) == word:
        print("\nYou won! The word was: " + word)
        break
    
    guess = input("Guess a letter: ").upper()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter!")
        continue
    
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue
    
    guessed_letters.append(guess)
    
    if guess in word:
        correct_guesses.append(guess)
        print("Good guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

if wrong_guesses >= max_wrong:
    print(display_hangman(wrong_guesses))
    print("Game Over! The word was: " + word)