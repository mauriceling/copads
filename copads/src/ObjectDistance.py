"""
File containing functions for use in calculating distances between 2 objects.
Distances are common measures of differences (dissimilarity) rather than 
similarity. That is, 2 identical objects will have 0 distance.

Copyright (c) Maurice H.T. Ling <mauriceling@acm.org>
Date created: 17th August 2005
"""

import math
from CopadsExceptions import DistanceInputSizeError

def setCompare(original, test, absent):
    original_only = float(len([x for x in original if x not in test]))
    test_only = float(len([x for x in test if x not in original]))
    both = float(len([x for x in original if x in test]))
    return (original_only, test_only, both)

def listCompare(original, test, absent):
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
        
def Jaccard(original = '', test = '', absent = 0, type = 'Set'):
    """
    Given 2 lists (original and test), calculates the Jaccard Distance 
    (1 - Jaccard Index) based on the formula,
    
    1 - [(number of regions where both species are present)/
         (number of regions where at least one species is present)]
    
    absent: user-defined identifier for absent of region, default = 0
    type: {Set | List}, define whether use Set comparison (unordered) or
          list comparison (ordered), default = Set
         
    Ref: Jaccard P (1908) Nouvelles recherches sur la distribution florale. 
         Bull Soc Vaud Sci Nat 44:223-270
    """
    if type == 'Set':
        (original_only, test_only, both) = setCompare(original, test, absent)
    else:
        (original_only, test_only, both) = listCompare(original, test, absent)
    return 1-(both/(both+original_only+test_only))
    
def Nei_Li(original = '', test = '', absent = 0, type = 'Set'):
    """
    Given 2 lists (original and test), calculates the Nei and Li Distance 
    based on the formula,
    
    1 - [2 x (number of regions where both species are present)/
         [(2 x (number of regions where both species are present)) + 
          (number of regions where only one species is present)]]
    
    absent: user-defined identifier for absent of region, default = 0
    type: {Set | List}, define whether use Set comparison (unordered) or
          list comparison (ordered), default = Set
                
    Ref: Nei M, Li WH (1979) Mathematical models for studying genetic variation 
        in terms of restriction endonucleases. Proc Natl Acad Sci USA 76:5269-5273
    """
    if type == 'Set':
        (original_only, test_only, both) = setCompare(original, test, absent)
    else:
        (original_only, test_only, both) = listCompare(original, test, absent)
    return 1-((2*both)/((2*both)+original_only+test_only))
    
def Sokal_Michener(original = '', test = ''):
    """
    Given 2 lists (original and test), calculates the Sokal and Michener 
    Distance based on the formula,
    
    1 - [(number of regions where both species are present or absent)/
         (number of regions where both species are absent different)]
         
    Ref: Sokal RR, Michener CD (1958) A statistical method for evaluating 
        systematic relationships. Univ Kansas Sci Bull 38:1409-1438
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

def Dice(original = '', test = '', type = 'Set'):
    """
    Given 2 lists (original and test), calculates the Dice Distance 
    (1 - Dice Index) based on the formula,
    
    1 - (number of regions where both species / sum of species in each list)
    
    type: {Set | List}, define whether use Set comparison (unordered) or
          list comparison (ordered), default = Set
    """
    if type == 'Set':
        (original_only, test_only, both) = setCompare(original, test, absent = 0)
    else:
        (original_only, test_only, both) = listCompare(original, test, absent = 0)
    return 1 - ((2 * both) / (float(len(original)) + float(len(test))))

def Dice_Sorensen(original = '', test = '', absent = 0, type = 'Set'):
    """
    Given 2 lists (original and test), calculates the Dice-Sorensen Distance 
    (1 - Dice-Sorensen Index) based on the formula,
    
    1 - [2 x (number of regions where both species are present) /
        (2 x (number of regions where both species are present) + 
            (number of regions where at least one species is present))]
    
    absent: user-defined identifier for absent of region, default = 0
    type: {Set | List}, define whether use Set comparison (unordered) or
          list comparison (ordered), default = Set
    """
    if type == 'Set':
        (original_only, test_only, both) = setCompare(original, test, absent)
    else:
        (original_only, test_only, both) = listCompare(original, test, absent)
    return 1 - ((2 * both) / ((2*both) + test_only + original_only))

def Ochiai(original = '', test = '', absent = 0, type = 'Set'):
    """
    Given 2 lists (original and test), calculates the Dice-Sorensen Distance 
    (1 - Dice-Sorensen Index) based on the formula,
    
    1 - [(number of regions where both species are present) / 
         (square root of 
            ((number of regions where both species are present) +
                 (number of regions found in original only)) * 
            ((number of regions where both species are present) +
                 (number of regions found in test only))
        )]
    
    absent: user-defined identifier for absent of region, default = 0
    type: {Set | List}, define whether use Set comparison (unordered) or
          list comparison (ordered), default = Set
    """
    if type == 'Set':
        (original_only, test_only, both) = setCompare(original, test, absent)
    else:
        (original_only, test_only, both) = listCompare(original, test, absent)
    return 1 - (both / math.sqrt((both + original_only)*(both + test_only)))
    
def Kulczynski(original = '', test = '', absent = 0 , type = 'Set'):
    """
    Given 2 lists (original and test), calculates the Kulczynski Distance 
    based on the formula,
    
    1-(mean of (
       ((number of regions where both species are present)/
        (number of regions where species 1 is present)) 
       and 
       ((number of regions where both species are present)/
        (number of regions where species 2 is present))))
        
    absent: user-defined identifier for absent of region, default = 0
    type: {Set | List}, define whether use Set comparison (unordered) or
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
    Given 2 lists (original and test), calculates the Hamming Distance by 
    counting the number of ordered differences between the 2 lists.
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
    Calculates the Levenshtein distance between a and b. This routine is 
    implemented by Magnus Lie Hetland (http://www.hetland.org/python/distance.py)"""
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
    """euclidean_py(x, y) -> euclidean distance between x and y
    Adapted from BioPython"""
    # lightly modified from implementation by Thomas Sicheritz-Ponten.
    # This works faster than the Numeric implementation on shorter
    # vectors.
    if len(x) != len(y):
        raise DistanceInputSizeError("Size (length) of inputs must be \
            equal for Euclidean distance")
    sum = 0
    for i in range(len(x)):
        sum += (x[i]-y[i])**2
    return math.sqrt(sum)


