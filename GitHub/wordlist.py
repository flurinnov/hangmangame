import random

def get_word():
    words = ['python', 'hangman', 'challenge', 'programming', 'computer']
    return random.choice(words).upper()
