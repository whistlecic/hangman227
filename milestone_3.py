import random

word_list =  ['apple', 'peach', 'grape', 'melon', 'blueberry']
word = random.choice(word_list) 

def check_guess(guess):
    guess_lowercase = guess.lower()
    if guess_lowercase in word:
        print(f"Good guess! '{guess_lowercase}' is in the word.")
    else:
        print(f"Sorry, '{guess_lowercase}' is not in the word. Please try again.")
        ask_for_input()

def ask_for_input():
    while True:
        guess = str(input("Enter a letter: "))
        if len(guess) == 1 and guess.isalpha():
            break
        print("Invalid letter. Please,  enter a single alphabetical character.")
    check_guess(guess)

ask_for_input()
    
