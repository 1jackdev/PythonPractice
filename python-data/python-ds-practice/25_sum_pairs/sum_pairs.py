def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    sums = []
    good_pairs = []
    best_pairs = []
    for x in range(0, len(nums) - 1):
        for y in range(0, len(nums) - 1):
            sums.append([nums[x], nums[y + 1]])
    for pair in sums:
        if sum(pair) == goal:
            good_pairs.append(pair)

    for candidate in good_pairs:
        if nums.index(candidate[0]) < nums.index(candidate[1]):
            best_pairs.append([nums.index(candidate[1]), candidate])

    best_pairs.sort()
    if not good_pairs:
        return ()
    if len(best_pairs) > 1:
        return tuple(best_pairs[0][1])
    else:
        return tuple(good_pairs[0])
