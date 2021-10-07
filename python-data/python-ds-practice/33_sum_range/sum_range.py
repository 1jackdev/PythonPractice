def sum_range(nums, start=0, end=None):
    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> nums = [1, 2, 3, 4]

        >>> sum_range(nums)
        10

        >>> sum_range(nums, 1)
        9

        >>> sum_range(nums, end=2)
        6

        >>> sum_range(nums, 1, 3)
        9

    If end is after end of list, just go to end of list:

        >>> sum_range(nums, 1, 99)
        9
    """
    range_nums = []

    if start != 0:
        if end != None and end <= len(nums):
            for x in range(nums[start], nums[end] + 1):
                range_nums.append(x)
        elif end == None or end > len(nums):
            for x in range(nums[start], nums[-1] + 1):
                range_nums.append(x)
    else:
        if end != None and end <= len(nums):
            for x in range(nums[0], nums[end] + 1):
                range_nums.append(x)
        elif end == None or end > len(nums):
            for x in range(nums[0], nums[-1] + 1):
                range_nums.append(x)       
                      
    return sum(range_nums)
