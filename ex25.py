def break_words(stuff):
    words = stuff.split()
    return words
def sort_words(words):
    """sorts the words"""
    return sorted(words)
def print_first_word(words):
    """ Print the first word after popping of"""
    word = words.pop(0)
    return word
def print_last_word(words):
    """Print the last word after popping it of"""
    word = words.pop(-1)
    return (word)
def sort_sentence(sentence):
    """ Takes in a full sentence and returns the sorted words"""
    words = break_words(sentence)
    return sort_words(words)
def print_the_last_and_first(sentence):
    """ prints the last and first word of the sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    return print_the_last_and_first

def print_first_and_last_sorted(sentence):
    """sorts the words and prints the first and last ine."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
    return print_first_and_last_sorted
