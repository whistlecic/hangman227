import random
# This is a comment
'''This is a Docstring'''

word_list = ['apple', 'melon', 'orange', 'peach', 'cherry']

word = random.choice(word_list)

guess = str(input("Enter a single letter: "))

def check_valid_input():
    if len(guess) == 1 and guess.isalpha():
        print("Good guess!")
    else:
        print("Oops! That is not a valid input.")

