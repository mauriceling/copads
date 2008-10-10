"""
File containing functions for use in calculating distances between 2 objects.
Distances are common measures of differences (dissimilarity) rather than 
similarity. That is, 2 identical objects will have 0 distance.

Copyright (c) Maurice H.T. Ling <mauriceling@acm.org>
Date created: 17th August 2005
"""

import math
from CopadsExceptions import DistanceInputSizeError
from Operations import summation

def setCompare(original, test, absent):
    """Used for processing set-based (unordered or nominal) distance of 
    categorical data.
    
    @param original: list of original data
    @param test: list of data to test against original
    @param absent: indicator to define absent data"""
    original_only = float(len([x for x in original if x not in test]))
    test_only = float(len([x for x in test if x not in original]))
    both = float(len([x for x in original if x in test]))
    return (original_only, test_only, both)

def listCompare(original, test, absent):
    """
    Used for processing list-based (ordered or ordinal) distance of categorical 
    data.
    
    @param original: list of original data
    @param test: list of data to test against original
    @param absent: indicator to define absent data"""
    original = list(original)
    test = list(test)
    original_only = 0.0
    test_only = 0.0
    both = 0.0
    for i in range(len(original)):
        if original[i] == absent and test[i] == absent: pass
        elif original[i] == test[i]: both = both + 1
        elif original[i] <> absent and test[i] == absent:
            original_only = original_only + 1
        elif original[i] == absent and test[i] <> absent: 
            test_only = test_only + 1
        else: pass
    return (original_only, test_only, both)
        
def Jaccard(original = '', test = '', absent = 0, type = 'Set'):
    """
    Jaccard Distance is distance measure for nominal or ordinal data.
    
    Given 2 lists (original and test), calculates the Jaccard Distance 
    (1 - Jaccard Index) based on the formula,
    
    1 - [(number of regions where both species are present)/
    (number of regions where at least one species is present)]
        
    @see: Jaccard P (1908) Nouvelles recherches sur la distribution florale. 
    Bull Soc Vaud Sci Nat 44:223-270
    
    @param original: list of original data
    @param test: list of data to test against original
    @param absent: user-defined identifier for absent of region, default = 0
    @param type: {Set | List}, define whether use Set comparison (unordered) or 
    list comparison (ordered), default = Set
    """
    if type == 'Set':
        (original_only, test_only, both) = setCompare(original, test, absent)
    else:
        (original_only, test_only, both) = listCompare(original, test, absent)
    return 1-(both/(both+original_only+test_only))
    
def Nei_Li(original = '', test = '', absent = 0, type = 'Set'):
    """
    Nei and Li Distance is distance measure for nominal or ordinal data.
    
    Given 2 lists (original and test), calculates the Nei and Li Distance 
    based on the formula,
    
    1 - [2 x (number of regions where both species are present)/
    [(2 x (number of regions where both species are present)) + 
    (number of regions where only one species is present)]]
        
    @see: Nei M, Li WH (1979) Mathematical models for studying genetic variation 
    in terms of restriction endonucleases. Proc Natl Acad Sci USA 76:5269-5273
    
    @param original: list of original data
    @param test: list of data to test against original
    @param absent: user-defined identifier for absent of region, default = 0
    @param type: {Set | List}, define whether use Set comparison (unordered) or
        list comparison (ordered), default = Set
    """
    if type == 'Set':
        (original_only, test_only, both) = setCompare(original, test, absent)
    else:
        (original_only, test_only, both) = listCompare(original, test, absent)
    return 1-((2*both)/((2*both)+original_only+test_only))
    
def Sokal_Michener(original = '', test = ''):
    """
    Sokal and Michener Distance is distance measure for nominal or ordinal data.
    
    Given 2 lists (original and test), calculates the Sokal and Michener 
    Distance based on the formula,
    
    1 - [(number of regions where both species are present or absent)/
    (number of regions where both species are absent different)]
         
    @see: Sokal RR, Michener CD (1958) A statistical method for evaluating 
    systematic relationships. Univ Kansas Sci Bull 38:1409-1438
        
    @param original: list of original data
    @param test: list of data to test against original
    """
    if len(original) <> len(test): 
        raise DistanceInputSizeError("Size (length) of inputs must be \
                equal for Sokal & Michener's distance")
    in_original = 0.0
#    in_test = 0.0
    in_both = 0.0
    for index in range(len(original)):
        if original[index] == test[index]: in_both = in_both + 1
        if original[index] != test[index]: in_original = in_original + 1
#        if original[index] < test[index]: in_test = in_test + 1
#    print in_original
    return 1-(in_both/(in_both+in_original))

def Matching(original = '', test = '', absent = 0, type = 'Set'):
    """
    Matching Distance is distance measure for nominal or ordinal data.
    
    Given 2 lists (original and test), calculates the Matching Distance 
    (1 - Matching Coefficient) based on the formula,
    
    1 - (number of regions where both species are present or absent
    / sum of species in each list)
    
    @param original: list of original data
    @param test: list of data to test against original
    @param absent: user-defined identifier for absent of region, default = 0
    @param type: {Set | List}, define whether use Set comparison (unordered) or
        list comparison (ordered), default = Set
    """
    if type == 'Set':
        (original_only, test_only, both) = setCompare(original, test, absent)
    else:
        (original_only, test_only, both) = listCompare(original, test, absent)
    all_region = float(len(original)) + float(len(test))
    absent_region = all_region - original_only - test_only - both
    return 1 - ((2 * (both + absent_region)) / (all_region))

def Dice(original = '', test = '', absent = 0, type = 'Set'):
    """
    Dice Distance is distance measure for nominal or ordinal data.
    
    Given 2 lists (original and test), calculates the Dice Distance 
    (1 - Dice Index) based on the formula,
    
    1 - (number of regions where both species are present
    / sum of species in each list)
    
    @param original: list of original data
    @param test: list of data to test against original
    @param absent: user-defined identifier for absent of region, default = 0
    @param type: {Set | List}, define whether use Set comparison (unordered) or
        list comparison (ordered), default = Set
    """
    if type == 'Set':
        (original_only, test_only, both) = setCompare(original, test, absent)
    else:
        (original_only, test_only, both) = listCompare(original, test, absent)
    return 1 - ((2 * both) / (float(len(original)) + float(len(test))))

def Dice_Sorensen(original = '', test = '', absent = 0, type = 'Set'):
    """
    Dice and Sorensen Distance is distance measure for nominal or ordinal data.
    
    Given 2 lists (original and test), calculates the Dice-Sorensen Distance 
    (1 - Dice-Sorensen Index) based on the formula,
    
    1 - [2 x (number of regions where both species are present) /
    (2 x (number of regions where both species are present) + 
    (number of regions where at least one species is present))]
    
    @param original: list of original data
    @param test: list of data to test against original
    @param absent: user-defined identifier for absent of region, default = 0
    @param type: {Set | List}, define whether use Set comparison (unordered) or
        list comparison (ordered), default = Set
    """
    if type == 'Set':
        (original_only, test_only, both) = setCompare(original, test, absent)
    else:
        (original_only, test_only, both) = listCompare(original, test, absent)
    return 1 - ((2 * both) / ((2*both) + test_only + original_only))

def Ochiai(original = '', test = '', absent = 0, type = 'Set'):
    """
    Ochiai Distance is distance measure for nominal or ordinal data.
    
    Given 2 lists (original and test), calculates the Ochiai Distance 
    based on the formula,
    
    1 - [(number of regions where both species are present) / (square root of 
    ((number of regions where both species are present) +
    (number of regions found in original only)) * 
    ((number of regions where both species are present) +
    (number of regions found in test only)))]
    
    @param original: list of original data
    @param test: list of data to test against original
    @param absent: user-defined identifier for absent of region, default = 0
    @param type: {Set | List}, define whether use Set comparison (unordered) or
        list comparison (ordered), default = Set
    """
    if type == 'Set':
        (original_only, test_only, both) = setCompare(original, test, absent)
    else:
        (original_only, test_only, both) = listCompare(original, test, absent)
    return 1 - (both / math.sqrt((both + original_only)*(both + test_only)))
    
def Kulczynski(original = '', test = '', absent = 0 , type = 'Set'):
    """
    Kulczynski Distance is distance measure for nominal or ordinal data.
    
    Given 2 lists (original and test), calculates the Kulczynski Distance 
    based on the formula,
    
    1-(mean of (((number of regions where both species are present)/
    (number of regions where species 1 is present)) and 
    ((number of regions where both species are present)/
    (number of regions where species 2 is present))))
        
    @param original: list of original data
    @param test: list of data to test against original
    @param absent: user-defined identifier for absent of region, default = 0
    @param type: {Set | List}, define whether use Set comparison (unordered) or
        list comparison (ordered), default = Set
    """
    if type == 'Set':
        (original_only, test_only, both) = setCompare(original, test, absent)
    else:
        (original_only, test_only, both) = listCompare(original, test, absent)
    x1 = both/original_only
    x2 = both/test_only
    return 1-((x1+x2)/2)
    
def Hamming(original = '', test = ''):
    """
    Hamming Distance is distance measure for ordinal data - only for ordered
    data.
    
    Given 2 lists (original and test), calculates the Hamming Distance by 
    counting the number of ordered differences between the 2 lists.
    
    @param original: list of original data
    @param test: list of data to test against original
    """
    if len(original) <> len(test): 
        raise DistanceInputSizeError("Size (length) of inputs must be \
            equal for Hamming's distance")
    mismatch = 0
    for index in range(len(original)):
        if original[index] <> test[index]: mismatch = mismatch + 1
    return mismatch
    
def Levenshtein(a = '', b = ''):
    """
    Levenshtein Distance is distance measure for interval or ratio data.
    Calculates the Levenshtein distance between a and b. This routine is 
    implemented by Magnus Lie Hetland (http://www.hetland.org/python/distance.py)
    
    @param a: list of original data
    @param b: list of data to test against original"""
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a,b = b,a
        n,m = m,n
        
    current = range(n+1)
    for i in range(1,m+1):
        previous, current = current, [i]+[0]*m
        for j in range(1,n+1):
            add, delete = previous[j]+1, current[j-1]+1
            change = previous[j-1]
            if a[j-1] != b[i-1]:
                change = change + 1
            current[j] = min(add, delete, change)
            
def Euclidean(x = '', y = ''):
    """
    Euclidean Distance is distance measure for interval or ratio data.
    
    euclidean_py(x, y) -> euclidean distance between x and y
    Adapted from BioPython
    
    @param x: list of original data
    @param y: list of data to test against original"""
    # lightly modified from implementation by Thomas Sicheritz-Ponten.
    # This works faster than the Numeric implementation on shorter
    # vectors.
    if len(x) != len(y):
        raise DistanceInputSizeError("Size (length) of inputs must be \
            equal for Euclidean distance")
    sum = 0
    for i in range(len(x)):
        sum = sum + (x[i]-y[i])**2
    return math.sqrt(sum)

def Minkowski(x = '', y = '', power = 3):
    """
    Minkowski Distance is distance measure for interval or ratio data.
    
    Minkowski Distance is a generalized absolute form of Euclidean Distance.
    Minkowski Distance = Euclidean Distance when power = 2
    
    @param x: list of original data
    @param y: list of data to test against original
    @param power: expontential variable
    @type power: integer"""
    if len(x) != len(y):
        raise DistanceInputSizeError("Size (length) of inputs must be \
            equal for Minkowski distance")
    sum = 0
    for i in range(len(x)):
        sum = sum + abs(x[i]-y[i])**power
    return sum**(1/float(power))

def Manhattan(x = '', y = ''):
    """
    Manhattan Distance is distance measure for interval or ratio data.
    
    Manhattan Distance is also known as City Block Distance. It is essentially
    summation of the absolute difference between each element.
    
    @param x: list of original data
    @param y: list of data to test against original"""
    if len(x) != len(y):
        raise DistanceInputSizeError("Size (length) of inputs must be \
            equal for Manhattan distance")
    sum = 0
    for i in range(len(x)):
        sum = sum + abs(x[i]-y[i])
    return sum

def Canberra(x = '', y = ''):
    """
    Canberra Distance is distance measure for interval or ratio data.
    
    @see: Lance GN and Williams WT. 1966 Computer programs for hierarchical 
    polythetic classification. Computer Journal 9: 60-64.
    
    @param x: list of original data
    @param y: list of data to test against original"""
    if len(x) != len(y):
        raise DistanceInputSizeError("Size (length) of inputs must be \
            equal for Canberra distance")
    sum = 0
    for i in range(len(x)):
        sum = sum + (abs(x[i]-y[i]) / abs(x[i]+y[i]))
    return sum

def Bray_Curtis(x = '', y = ''):
    """
    Bray-Curtis Distance is distance measure for interval or ratio data.
    
    @see: Bray JR and Curtis JT. 1957. An ordination of the upland forest
    communities of S. Winconsin. Ecological Monographs27: 325-349.
    
    @param x: list of original data
    @param y: list of data to test against original"""
    if len(x) != len(y):
        raise DistanceInputSizeError("Size (length) of inputs must be \
            equal for Bray-Curtis distance")
    return Manhattan(x, y) / (summation(x) + summation(y))