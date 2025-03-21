#'''This is a docstring'''

import random

word_list =  ['apple', 'peach', 'grape', 'melon', 'blueberry']

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list) #The word the user needs to guess, picked at random from word_list.
        self.word_guessed = ['_' for _ in self.word] #A list of the letters in the answer word, with _ representing each unguessed letter.
        self.num_letters = len(set(self.word)) #The number of UNIQUE letters in the answer word that have not been guessed yet
        self.num_lives = num_lives #Number of lives the player gets, defaulted to 5.
        self.word_list = word_list #The list of words from which the game selects one to be the answer.
        self.list_of_guesses = [] #List holding all the user's guesses, for each game this is initially an empty list.
        # pass

    def check_guess(self, guess):
        guess_lowercase = guess.lower()
        if guess_lowercase in self.word:
            print(f"Good guess! {guess_lowercase} is in the word.")
            for index, letter in enumerate(self.word): #Gets index of the guessed letter in the answer if it is in the answer word.
                if letter == guess_lowercase:
                    self.word_guessed[index] = guess #Replace _ with the guessed letter at the matching index/indices.
            self.num_letters -= 1
            print(self.word_guessed)
        else:
            self.num_letters -= 1
            print(f"Sorry, Cicely {guess} is not in the word. Please try again.")
            print(f"You have {self.num_lives} lives left.")
            
    
    def ask_for_input(self):
        while True:
            guess = str(input("Enter a letter: "))
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)                

game = Hangman(word_list)

game.ask_for_input()