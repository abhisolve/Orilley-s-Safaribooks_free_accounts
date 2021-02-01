"""
generates random emails, name
https://stackoverflow.com/questions/59231343/how-to-make-random-email-generator
"""
import itertools
import random

def generatemail():
    """
        generate and return random email
    """
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
               "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",]

    all_combos = list(itertools.combinations(letters, 7)) # make all 7 letter combinations
    all_combos = [''.join(combo) for combo in all_combos] # make them strings
    email = random.sample(all_combos, 1)[0]+'@gmail.com' # grab a random one, add @gmail.com

    return email
