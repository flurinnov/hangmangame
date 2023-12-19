#!/usr/bin/python
# Import the needed extensions
import wordlist
import utils
import time
import wordlist_extended

# Define a function that calculates the score, outside of the game loop
# The score gets calculated based on how many tries the user has left, how long the word is and how much time has passed
def calculate_score(tries_left, word_length, elapsed_time):
    max_score = 100
    time_penalty = round(elapsed_time) * 5  
    tries_penalty = (7 - tries_left) * 11  
    score = max_score - time_penalty - tries_penalty
    return max(0, score)  

#Define a function for the game itself
def play(guess_timelimit=10):
    print("Let's play Hangman!")

    # First, the user is asked to input the difficulty, in which he wants to play the game
    difficulty = input("Please enter difficulty \"easy\", \"medium\" or \"hard\"\n")
    while(difficulty!="easy" and difficulty != "medium" and difficulty!="hard"):
        difficulty = input("Input error. Please enter difficulty \"easy\", \"medium\" or \"hard\"\n")

    # The user is then asked to select a topic
    string = "Please select one the following topics:\n"
    
    for theme in wordlist_extended.getThemesByDifficulty(difficulty):
        string += "\"" + theme + "\"\n"

    theme = input(string)
    while( theme not in wordlist_extended.getThemesByDifficulty(difficulty)):
        theme = input(string)

    # Here, the user is guessing letters that are either in the word or not
    word = wordlist_extended.get_random_word(difficulty,theme)
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    game_over = False

    print(utils.display_hangman(tries))
    print(word_completion)

    score = None

    while not guessed and tries > 0:
        starttime = time.time()
        guess = input("Please guess a letter or word: ").upper()
        used_time = time.time() - starttime
        if used_time > guess_timelimit:
            print("Time has run out! Start a new game.")
            break #skipping the rest of the loop. The time has run out, the player has to start a new game.
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess) # If the player guesses a letter twice, the game suggests to try another letter.
            elif guess not in word:
                print(guess, "is not in the word.") # If the letter is not in the word, the player gets notified.
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!") # If the letter is in the word, the player gets notified. 
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

    # The game ends when the word is guessed or the player has no tries left
    if guessed or tries == 0:
        game_over = True

    if game_over:
        print("Game over! Final word:", word)
        print("Thanks for playing Hangman!")

    # The player gets notified about his score, if he guessed the word and of not he is given the word.
    if guessed:
        elapsed_time = time.time() - starttime
        score = calculate_score(tries, len(word), elapsed_time)
        print("Congrats, you guessed the word! You win! Your score:", score, "/100")
    if not guessed:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")

if __name__ == "__main__":
    play()

