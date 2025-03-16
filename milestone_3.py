import random

word_list = ['apple', 'watermelon', 'cherry', 'peach', 'blueberry']

word = random.choice(word_list)

def ask_for_input():
    #Function to get user's guess for a letter in the word.
    guess = str(input("Enter a letter: ")).lower().strip()
    
    if not check_guess(guess):  # Checks whether guess is valid
        return ask_for_input()  # If invalid asks for input again

    if guess in word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Please try again.")

def check_guess(guess):
    if len(guess) == 1 and guess.isalpha():
        return True
    else:
        print("Invalid letter. Please,  enter a single alphabetical character.")
        return False

ask_for_input()
