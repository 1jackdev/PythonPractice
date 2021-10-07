def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    words = phrase.lower().split(" ")
    word_list = []
    for word in words:
        word_list.append(word.capitalize())
    new_phrase = " ".join(word_list)
    return new_phrase
