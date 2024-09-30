'''This is a docstring'''
# This is milestone 3
import random
word_list = ['apple', 'watermelon', 'cherry', 'peach', 'blueberry']

class Hangman:
    def __init__(self, word_list, num_lives=5):
        # word_list: list - A list of words
        self.word_list = word_list

        # num_lives: int - The number of lives the player has at the start of the game.
        self.num_lives = num_lives
        
        # word: The word to be guessed, picked randomly from the word_list. Remember to import the random module into your script
        self.word = random.choice(word_list)
        
        # word_guessed: list - A list of the letters of the word, with _ for each letter not yet guessed. 
        # For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']. 
        # If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
        self.word_guessed = ['_' for _ in self.word]
        
        # num_letters: int - The number of UNIQUE letters in the word that have not been guessed yet
        self.num_letters = len(set(self.word))
        
        # list_of_guesses: list - A list of the guesses that have already been tried. Set this to an empty list initially
        self.list_of_guesses = []

        pass

    def check_guess(guess):
        guess_lowercase = guess.lower()
        if guess_lowercase in self.word:
            print(f"Good guess! {guess_lowercase} is in the word.")
        else:
            print(f"Sorry, {guess} is not in the word. Please try again.")
            
    
    def ask_for_input():

        while True:
            guess = str(input("Enter a letter: "))
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                check_guess(guess)
                self.list_of_guesses.append(guess)                
            break