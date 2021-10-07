"""Word Finder: finds random words from a dictionary."""
import random


class WordFinder:
    """finds random words from a dictionary file

    >>> wf = WordFinder("words.txt")
    3 words were read

    >>> wf.get_random_word()
    'cat'

    >>> wf.get_random_word()
    'porcupine'

    >>> wf.get_random_word()
    'dog'

    """

    def __init__(self, file_name):
        """read from dictionary and tell us how many words were read"""
        dict_file = open(file_name)
        self.words = self.parse(dict_file)
        print(f"{len(self.words)} words were read")

    def parse(self, dict_file):
        """Parse the dictionary file into a list of words"""
        return [word.strip() for word in dict_file]

    def get_random_word(self):
        """return a random word from dictionary"""
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """Like regular wordfinder, but ignores blank lines and comments.

    >>> specialwf = SpecialWordFinder("spaces.txt")
    3 words were read

    >>> specialwf.get_random_word()
    'toucan'

    >>> specialwf.get_random_word()
    '#'

    >>> specialwf.get_random_word()
    '  '

    """

    def parse(self, dict_file):
        """Parse the dictionary file into a list of words, 
        but ignore comment lines and blank lines.
        """
        return [word.strip() for word in dict_file if word.strip() and not word.startswith("#")]
