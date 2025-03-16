# This is milestone 5
import random

#Copy all the codes in milestone_4.py file into the newly created milestone_5.py file.
#Not sure why this is necessary should just import milestone_4 file?

from milestone_3 import ask_for_input
word_list =  ['apple', 'watermelon', 'cherry', 'peach', 'blueberry']

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list #The list of words from which the answer is selected
        self.num_lives = num_lives #Number of lives at the start of the game
        self.word = random.choice(word_list) #The answer, randomly selected from word_list
        self.word_guessed = ['_' for _ in self.word] #List of blank letters representing the answer
        self.num_letters = len(set(self.word)) #The number of unique letters in the word that haven't been guessed
        self.list_of_guesses = [] #List of guesses that have already been tried
        pass

    def check_guess(self, guess):
        guess_lowercase = guess.lower()
        if guess_lowercase in self.word:
            print(f"Good guess! {guess_lowercase} is in the word.")
            for letter in self.word:
                if letter == guess_lowercase:
                    index_of_letter = self.word.index(letter) #We don't need to 
        else:
            print(f"Sorry, {guess} is not in the word. Please try again.")
            
    
    def ask_for_input(self):
        #
        while True:
            guess = str(input("Enter a letter: "))
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)                
            break


game.ask_for_input()

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if num_lives == 0:  #If num_lives is zero then game has been lost
            print("You lost!")    
        elif self.num_letters > 0: #Checks if there are letters left in the game to play
            ask_for_input()
        if num_lives != 0 and num_letters < 1: #Checks there's more than 0 lives left and all the letters have been guessed
            print("Congratulations. You won the game!")

play_game(word_list)
