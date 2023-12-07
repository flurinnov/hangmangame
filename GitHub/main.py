#!/usr/bin/python

import hangman

def main():
    while True:
        hangman.play()  # Start a game of Hangman

        # Ask the player if they want to play again
        play_again = input("Play Again? (Y/N) ").upper()
        if play_again != "Y":
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()

