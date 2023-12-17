import random

# Words categorized by difficulty and theme
word_dict = {
    "easy": {
        "animals": ["cat", "dog", "fish", "bird", "cow", "frog", "goat", "bear", "wolf", "duck"],
        "colors": ["red", "blue", "green", "yellow", "pink", "black", "white", "gray", "brown", "azure"],
        "fruits": ["apple", "pear", "peach", "grape", "plum", "mango", "berry", "cherry", "lime", "lemon"]
    },
    "medium": {
        "countries": ["egypt", "france", "india", "china", "spain", "brazil", "nepal", "italy", "japan", "kenya"],
        "science": ["atom", "force", "energy", "plant", "human", "orbit", "matter", "neuron", "virus", "liquid"],
        "sports": ["soccer", "tennis", "cricket", "boxing", "rugby", "golf", "cycling", "sailing", "judo", "karate"]
    },
    "hard": {
        "literature": ["metaphor", "hyperbole", "sonnet", "dialogue", "irony", "satire", "prologue", "epilogue", "anecdote", "allegory"],
        "technology": ["algorithm", "database", "encryption", "hardware", "software", "biometrics", "bandwidth", "firewall", "malware", "protocol"],
        "astronomy": ["nebula", "galaxy", "asteroid", "universe", "satellite", "cosmos", "eclipse", "parallax", "quasar", "supernova"]
    }
}

def get_random_word(difficulty, theme):
    """ Get a random word based on the chosen difficulty and theme. """
    words = word_dict.get(difficulty, {}).get(theme, [])
    if not words:
        raise ValueError("No words available for the selected difficulty and theme.")
    return random.choice(words).upper()


def getThemesByDifficulty(difficulty):
    """ Get available themes for a given difficulty. """
    themes = word_dict.get(difficulty, {}).keys()
    return list(themes)




