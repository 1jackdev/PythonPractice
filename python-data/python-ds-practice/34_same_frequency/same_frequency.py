def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1_str = str(num1)
    num2_str = str(num2)
    freq_tracker = []
    for num in num1_str:
        if num1_str.count(num) == num2_str.count(num):
            freq_tracker+= num
    for num in num2_str:
        if num2_str.count(num) == num1_str.count(num):
            if len(freq_tracker) == len(num1_str):
                return True
    return False
    