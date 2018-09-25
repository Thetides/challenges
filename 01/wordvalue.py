from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    f = open(DICTIONARY, 'r')
    return [word.strip() for word in f.readlines()]


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0
    for letter in word.upper().replace("-", ""):
        score += LETTER_SCORES[letter]
    return score


def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    top_value_word = {"": 0}
    if not words:
        words = load_words()
    for word in words:
        score = calc_word_value(word)
        if score > top_value_word.values()[0]:
            top_value_word = {word:score}
    return top_value_word.keys()[0]


if __name__ == "__main__":
    pass
