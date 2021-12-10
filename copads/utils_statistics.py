"""
Collection of Statistical Utility Functions.
Date created: 8th December 2021
Licence: Python Software Foundation License version 2
"""

import random

def randomize_lists(datalists):
    """
    Function to take in a list of lists to randomize / shuffle the values. Returned shuffled list will have the same number of elements as the given list of lists. For example, if datalists is a list containing 3 lists of 4, 5, and 6 items respectively; then the returned shuffled list will be a list containing 3 lists of 4, 5, and 6 items respectively.

    @param datalists: List of lists to be shuffled.
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

def bootstrap_replicates(datalists, function, replicates=2000):
    """
    Generate bootstrap replicates and calculate the statistic for each bootstrap replicate using given function.

    @param datalists: List of lists containing the data; eg, [[sample A], [sample B]]
    @param function: Function to process the shuffled lists; eg, function(shuffled_lists)
    @param replicates: Number of bootstrap replicates. Default = 2000
    @return: Shuffled list of lists.
    """
    replicates = int(replicates)
    return [function(randomize_lists(datalists)) 
            for n in range(replicates)]
        
def randomization_test(datalists, function, replicates=2000):
    """
    Perform randomization test on the datalists.

    @param datalists: List of lists containing the data; eg, [[sample A], [sample B]]
    @param function: Function to process the datalist and shuffled lists to generate a statistic; eg, function(datalists)
    @param replicates: Number of bootstrap replicates. Default = 2000
    @return: List of (p-value, statistic, bootstrap statistics) where statistic is calculated from function on the datalists, p-value is the proportion of bootstrap statistics that is more than or equal to the statistic.
    """
    statistic = function(datalists)
    bs_replicates = bootstrap_replicates(datalists, function, replicates)
    pvalue = sum([1 for x in bs_replicates if statistic >= x]) / int(replicates)
    return (pvalue, statistic, bs_replicates)
