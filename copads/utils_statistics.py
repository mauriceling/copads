"""
Collection of Statistical Utility Functions.
Date created: 8th December 2021
Licence: Python Software Foundation License version 2
"""

import random

def randomize_1d_lists(datalists):
    """
    Function to take in a list of lists to randomize / shuffle the values. Returned shuffled list will have the same number of elements as the given list of lists. For example, if datalists is a list containing 3 lists of 4, 5, and 6 items respectively; then the returned shuffled list will be a list containing 3 lists of 4, 5, and 6 items respectively.

    @param datalist: List of lists to be shuffled.
    @return: Shuffled list of lists.
    """
    sizes = [len(x) for x in datalists]
    combined_list = []
    for x in datalists:
        combined_list = combined_list + x
    random.shuffle(combined_list)
    shuffled_list = []
    position = 0
    for i in sizes:
        try:
            x = combined_list[position:position+i]
            shuffled_list.append(x)
            position = position + i
        except:
            x = combined_list[position:]
            shuffled_list.append(x)
    return shuffled_list
