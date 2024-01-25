'''
The hangman game is a word guessing game where the player is given a word and has to guess the letters that make up the word. 
The player is given a certain number of tries (no more than 6 wrong guesses are allowed) to guess the correct letters before the game is over.
'''

# Output
'''
You have 6 tries left.                                                                                                                                           
Used letters:                                                                                                                                                    
Word: _ _ _ _                                                                                                                                                    
Guess a letter: a 

You have 6 tries left.                                                                                                                                           
Used letters: a                                                                                                                                                  
Word: _ a _ a                                                                                                                                                    
Guess a letter: j    

You have 6 tries left.                                                                                                                                           
Used letters: j a                                                                                                                                                
Word: j a _ a                                                                                                                                                    
Guess a letter: v                                                                                                                                                
You guessed the word java !
'''

import requests
import random
import os
import sys

#Create CMD Menu
def menu():
    print("***********************************")
    print("      WELCOME TO HAGMAN GAME       ")
    print("***********************************\n")
    print("Please choose one of the following options: \n")
    print("1. Play Game with random API\n")
    print("2. Play Game with your own word file\n")
    print("3. Exit\n")
    choice = int(input("Enter your choice: "))
    return choice

#Create function to clear console when started and finished game
def clear_console():
    if sys.platform.startswith("win"):
        os.system("cls")
    elif sys.platform.startswith("linux"):
        os.system("clear")
    elif sys.platform.startswith("darwin"):
        os.system("clear")

#Create function to get random word from API
def get_random_api_word(lenght_word: int):
    try:
        response = requests.get(f"https://random-word-api.herokuapp.com/word?length={lenght_word}")
        word = response.json()[0]
        return word
    except OSError as e:
        print(f"Encountered connection error: {e}.\n")
        return None
    except Exception as e:
        print(f"Encountered error: {e}.\n")
        return None

#Create function to get random word from file



if __name__ == "__main__":
    option = 0 #Default value of option to enter the while loop
    while(option != 3):
        option = menu()
        
        #Cases of excecution
        if option == 1:
            input_lenght_word = int(input("Enter the lenght of the word: "))
            word = get_random_api_word(input_lenght_word)
            print(word)
        
        elif option == 2:
            pass
        elif option == 3:
            print("Thanks for playing. Goodbye!\n")
        else:
            print("Invalid option. Please try again.\n")