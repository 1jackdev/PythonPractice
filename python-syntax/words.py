def print_upper_words(words, starters):

    """ Take in a list of words.
        for all words that start with 
        one of the starter letters,
        print it out in uppercase 
    """
    for word in words:
        for starter in starters:
            if word.startswith(starter):
                print(word.upper())
                break


print_upper_words(["apple", "bat", "cat", "elephant"], ["e", "a"])
