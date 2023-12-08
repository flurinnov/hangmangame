#!/usr/bin/python

import wordlist
import utils
import time

def play(guess_timelimit=10):
    word = wordlist.get_word()
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("Let's play Hangman!")
    print(utils.display_hangman(tries))
    print(word_completion)

    while not guessed and tries > 0:
        starttime = time.time()
        guess = input("Please guess a letter or word: ").upper()
        used_time = time.time() - starttime
        if used_time > guess_timelimit:
            print("Time has run out! Start a new game."
            continue #skipping the rest of the loop. The player has to start a new game.
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(utils.display_hangman(tries))
        print(word_completion)

    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")

if __name__ == "__main__":
    play()

