import random
# This is a comment
'''This is a Docstring'''

word_list = ['apple', 'watermelon', 'cherry', 'peach', 'blueberry']

print(word_list)

word = random.choice(word_list)

print(word)

guess = str(input("Enter a single letter: "))

def check_valid_input():
    if len(guess) == 1 and guess.isalpha():
        print("Good guess!")
    else:
        print("Oops! That is not a valid input.")

check_valid_input()

