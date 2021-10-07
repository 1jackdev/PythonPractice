def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """
    if start == None:
        if sought in collection:
            return True
        for k in collection:
            if collection[k] == sought:
                return True
    else:
        if type(collection) is str or type(collection) is list:
            if sought in collection:
                if collection[start] < collection[sought]:
                    return True
        if type(collection) is tuple:
            if sought in collection:
                if collection.index(sought) < collection[start]:
                    return True
        if type(collection) is set or type(collection) is dict:
            if sought in collection:
                return True
            for k in collection:
                if collection[k] == sought:
                    return True
    return False
