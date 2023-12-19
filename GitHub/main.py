#!/usr/bin/python

import hangman
# Define the main function to start the game
def main():
    while True:
        hangman.play()  

        # Ask the player if they want to play again
        play_again = input("Play Again? (Y/N) ").upper()
        if play_again != "Y":
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()

