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
import time

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
    print("\n")
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
def get_random_file_word(f_path: str):
    if os.path.exists(f_path):
        with open(f_path, "r") as f:
            words = f.readlines()
            word = random.choice(words).strip()
            return word
    else:
        raise FileNotFoundError
    
#Create game function
def hangman_game(word: str):
    win_comp = False
    used_letters = []
    word_completion = "_" * len(word)
    for i in range(0, 6):
        print(f"You have {6 - i} tries left.")
        print (f"Used letters: {used_letters}")
        print(f"Word: {word_completion}")
        guess = input("Guess a letter or word: ").lower()
        print("\n")
        if len(list(guess)) == 1: #Check if the guess is a word
            word_completion = check_letter(guess, word, word_completion) #Check if the letter is in the word and update the word_completion
            used_letters.append(guess) #Update the used letters array
            if "_" not in word_completion: #Check if the word is completed
                clear_console()
                print(f"You guessed the word {word} !")
                print("YOU WIN!")
                break
        else:
            if guess == word: #Check if the guess is the word
                clear_console()
                print(f"You guessed the word {word} !")
                print("YOU WIN!")
                win_comp = True
                break
            
    if "_" not in word_completion and not win_comp: #Check if the word is completed
        clear_console()
        print(f"You guessed the word {word} !")
        print("YOU WIN!")
    elif not win_comp:
        print(f"The word was {word} !")
        print("YOU LOSE :(")
        

#Create function to check if letter is in word
def check_letter(guess: str, word: str, word_completion: str):
    char_list = list(word_completion)
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                char_list[i] = guess
                
    return ''.join(char_list)


if __name__ == "__main__":
    option = 0 #Default value of option to enter the while loop
    while(option != 3):
        option = menu()
        
        #Cases of excecution
        if option == 1:
            input_lenght_word = int(input("Enter the lenght of the word: "))
            word = get_random_api_word(input_lenght_word)
            clear_console()
            hangman_game(word)
            time.sleep(10) #Wait 10 seconds before clearing the console
            clear_console()
        elif option == 2:
            input_file_path = input("Enter the path of the file: ")
            try:
                word = get_random_file_word(input_file_path)
                clear_console()
                hangman_game(word)
                time.sleep(10) #Wait 10 seconds before clearing the console
                clear_console()
            except FileNotFoundError:
                print(f"The selected file {input_file_path} doesn't exist. Please try again.\n")
        elif option == 3:
            print("Thanks for playing. Goodbye!\n")
        else:
            print("Invalid option. Please try again.\n")