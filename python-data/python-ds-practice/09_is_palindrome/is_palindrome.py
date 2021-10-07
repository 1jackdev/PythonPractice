def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    trimmed_phrase = phrase.replace(" ", "")

    lower_phrase = trimmed_phrase.lower()
    reversed_phrase = lower_phrase[::-1]
    if trimmed_phrase.lower() == reversed_phrase:
        return True
    else:
        return False
