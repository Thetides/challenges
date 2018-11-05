#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import itertools
import copy
import random

from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7


def draw_letters():
    """Pick NUM_LETTERS letters randomly. Hint: use stdlib random"""
    letters = []
    while len(letters) < NUM_LETTERS:
        choice = random.choice(POUCH)
        POUCH.remove(choice)
        letters.append(choice)
    return letters


def input_word(draw):
    """Ask player for a word and validate against draw.
    Use _validation(word, draw) helper."""
    player_word = input("Word to validate: ")
    return _validation(player_word, draw)


def _validation(word, draw):
    """Validations: 1) only use letters of draw, 2) valid dictionary word"""
    draw_copy = copy.copy(draw)
    if word.lower() not in DICTIONARY:
        raise ValueError("Word: {}, not in dictionary".format(word))

    for letter in word:
        print(letter)
        if letter.upper() not in draw_copy:
            raise ValueError("Your do not have letter: {}".format(letter))
        else:
            draw_copy.remove(letter.upper())


# From challenge 01:
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# Below 2 functions pass through the same 'draw' argument (smell?).
# Maybe you want to abstract this into a class?
# get_possible_dict_words and _get_permutations_draw would be instance methods.
# 'draw' would be set in the class constructor (__init__).
def get_possible_dict_words(draw):
    """Get all possible words from draw which are valid dictionary words.
    Use the _get_permutations_draw helper and DICTIONARY constant"""
    gpermu = _get_permutations_draw(draw)
    valid_words = list(set(gpermu).intersection(set(DICTIONARY)))
    return valid_words



def _get_permutations_draw(draw):
    """Helper for get_possible_dict_words to get all permutations of draw letters.
    Hint: use itertools.permutations"""
    permu_list = []
    mutations = []
    lower_draw = list(map(lambda x:x.lower(), draw))
    for num in range(1,len(draw)+1):
        perm = itertools.permutations(lower_draw, num)
        permu_list.extend(perm)

    for item in permu_list:
        mutations.append("".join(item))

    return mutations


# From challenge 01:
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def main():
    """Main game interface calling the previously defined methods"""
    draw = draw_letters()
    print('Letters drawn: {}'.format(', '.join(draw)))

    word = input_word(draw)
    word_score = calc_word_value(word)
    print('Word chosen: {} (value: {})'.format(word, word_score))

    possible_words = get_possible_dict_words(draw)

    max_word = max_word_value(possible_words)
    max_word_score = calc_word_value(max_word)
    print('Optimal word possible: {} (value: {})'.format(
        max_word, max_word_score))

    game_score = word_score / max_word_score * 100
    print('You scored: {:.1f}'.format(game_score))


if __name__ == "__main__":
    main()
