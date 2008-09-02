"""
Collection of hypothesis testing routines.
Each routine will return a 3-element tuple: (result, statistic, critical)
where
result = True (reject null hypothesis; statistic > critical) or False (accept 
null hypothesis; statistic <= critical)
statistic = calculated statistic value
critical = value of critical region for statistical test

References:
Test 1-100: Gopal K. Kanji. 2006. 100 Statistical Tests, 3rd edition.
            Sage Publications.
"""

from StatisticsDistribution import *
from math import sqrt, log

def test(statistic, distribution, alpha):
    """
    Generates the critcal region from distribution and alpha value using
    the distribution's inverseCDF method. 
    
    Return a 3-element tuple: (result, statistic, critical)
    where
        result = True (reject null hypothesis; statistic > critical) or 
                    False (accept null hypothesis; statistic <= critical)
        statistic = calculated statistic value
        critical = value of critical region for statistical test"""
    critical = distribution.inverseCDF(alpha)
    if statistic < critical: return (False, statistic, critical)
    else: return (True, statistic, critical)
    
def Z1Mean1Variance(**kwargs):
    """
    Test 1: Z-test for a population mean (variance known)
    
    To investigate the significance of the difference between an assumed 
    population mean and sample mean when the population variance is
    known.
    
    Limitations:
    1. Requires population variance (use Test 7 if population variance unknown)
    
    Parameters:
    smean = sample mean
    pmean = population mean
    pvar = population variance
    ssize = sample size
    alpha = confidence level"""
    smean = kwargs['smean']
    pmean = kwargs['pmean']
    pvar = kwargs['pvar']
    ssize = kwargs['ssize']
    statistic = (smean - pmean)/ \
                (pvar / sqrt(ssize))
    return test(statistic, NormalDistribution(), kwargs['alpha'])

def Z2Mean1Variance(**kwargs):
    """
    Test 2: Z-test for two population means (variances known and equal)
    
    To investigate the significance of the difference between the means of two 
    samples when the variances are known and equal.
    
    Limitations:
    1. Population variances must be known and equal (use Test 8 if population
    variances unknown
    
    Parameters:
    smean1 = sample mean of sample #1
    smean2 = sample mean of sample #2
    pvar = variances of both populations (variances are equal)
    ssize1 = sample size of sample #1
    ssize2 = sample size of sample #2
    alpha = confidence level
    pmean1 = population mean of population #1 (optional)
    pmean2 = population mean of population #2 (optional)"""
    if not kwargs.has_key('pmean1'): 
        pmean1 = 0.0
    else: pmean1 = kwargs['pmean1']
    if not kwargs.has_key('pmean2'):
        pmean2 = 0.0
    else: pmean2 = kwargs['pmean2']
    smean1 = kwargs['smean1']
    smean2 = kwargs['smean2']
    pvar = kwargs['pvar']
    ssize1 = kwargs['ssize1']
    ssize2 = kwargs['ssize2']
    statistic = ((smean1 - smean2) - (pmean1 - pmean2))/ \
                (pvar * sqrt((1 / ssize1) + (1 / ssize2)))
    return test(statistic, NormalDistribution(), kwargs['alpha'])    

def Z2Mean2Variance(**kwargs):    
    """
    Test 3: Z-test for two population means (variances known and unequal)
    
    To investigate the significance of the difference between the means of two
    samples when the variances are known and unequal.
    
    Limitations:
    1. Population variances must be known(use Test 9 if population variances 
    unknown
    
    Parameters:
    smean1 = sample mean of sample #1
    smean2 = sample mean of sample #2
    pvar1 = variance of population #1
    pvar2 = variance of population #2
    ssize1 = sample size of sample #1
    ssize2 = sample size of sample #2
    alpha = confidence level
    pmean1 = population mean of population #1 (optional)
    pmean2 = population mean of population #2 (optional)"""
    if not kwargs.has_key('pmean1'): 
        pmean1 = 0.0
    else: pmean1 = kwargs['pmean1']
    if not kwargs.has_key('pmean2'):
        pmean2 = 0.0
    else: pmean2 = kwargs['pmean2']
    smean1 = kwargs['smean1']
    smean2 = kwargs['smean2']
    pvar1 = kwargs['pvar1']
    pvar2 = kwargs['pvar2']
    ssize1 = kwargs['ssize1']
    ssize2 = kwargs['ssize2']
    statistic = ((smean1 - smean2) - (pmean1 - pmean2))/ \
                sqrt((pvar1 / ssize1) + (pvar2 / ssize2))
    return test(statistic, NormalDistribution(), kwargs['alpha'])

def Z1Proportion(**kwargs):    
    """
    Test 4: Z-test for a proportion (binomial distribution)
    
    To investigate the significance of the difference between an assumed 
    proportion and an observed proportion.
    
    Limitations:
    1. Requires sufficiently large sample size to use Normal approximation to
    binomial
    
    Parameters:
    spro = sample proportion
    ppro = population proportion
    ssize = sample size
    alpha = confidence level"""
    spro = kwargs['spro']
    ppro = kwargs['ppro']
    ssize = kwargs['ssize']
    statistic = (abs(ppro - spro) - (1 / (2 * ssize)))/ \
                sqrt((ppro * (1 - spro)) / ssize)
    return test(statistic, NormalDistribution(), kwargs['alpha'])

def Z2Proportion(**kwargs):    
    """
    Test 5: Z-test for the equality of two proportions (binomial distribution)
    To investigate the assumption that the proportions of elements from two 
    populations are equal, based on two samples, one from each population.
    
    Limitations:
    1. Requires sufficiently large sample size to use Normal approximation to
    binomial
    
    Parameters:
    spro1 = sample proportion #1
    spro2 = sample proportion #2
    ssize1 = sample size #1
    ssize2 = sample size #2
    alpha = confidence level"""
    spro1 = kwargs['spro1']
    spro2 = kwargs['spro2']
    ssize1 = kwargs['ssize1']
    ssize2 = kwargs['ssize2']
    P = ((spro1 * ssize1) + (spro2 * ssize2)) / (ssize1 + ssize2)
    statistic = (spro1 - spro2) / \
                sqrt((P * (1 - P)) * ((1 / ssize1) * (1 / ssize2)))
    return test(statistic, NormalDistribution(), kwargs['alpha'])

def Z2Count(**kwargs):    
    """
    Test 6: Z-test for comparing two counts (Poisson distribution)
    
    To investigate the significance of the differences between two counts.
    
    Limitations:
    1. Requires sufficiently large sample size to use Normal approximation to
    binomial
    
    Parameters:
    time1 = first measurement time
    time2 = second measurement time
    count1 = counts at first measurement time
    count2 = counts at second measurement time
    alpha = confidence level"""
    time1 = kwargs['time1']
    time2 = kwargs['time2']
    R1 = kwargs['count1'] / time1
    R2 = kwargs['count2'] / time2
    statistic = (R1 - R2) / sqrt((R1 / time1) + (R2 / time2))
    return test(statistic, NormalDistribution(), kwargs['alpha'])

def t1Mean(**kwargs):
    """
    Test 7: t-test for a population mean (population variance unknown)
    
    To investigate the significance of the difference between an assumed 
    population mean and a sample mean when the population variance is 
    unknown and cannot be assumed equal or not equal.
    
    Limitations:
    1. Weaker form of Test 1
    
    Parameters:
    smean = sample mean
    pmean = population mean
    svar = sample variance
    ssize = sample size"""
    smean = kwargs['smean']
    pmean = kwargs['pmean']
    svar = kwargs['svar']
    ssize = kwargs['ssize']
    statistic = (smean - pmean) / (svar / sqrt(ssize))
    return test(statistic, TDistribution(df = ssize - 1), kwargs['alpha'])

def t2Mean2EqualVariance(**kwargs):    
    """
    Test 8: t-test for two population means (population variance unknown but 
    equal)
    
    To investigate the significance of the difference between the means of 
    two populations when the population variances are unknown but assumed
    equal.
    
    Limitations:
    1. Weaker form of Test 2
    
    Parameters:
    smean1 = sample mean of sample #1
    smean2 = sample mean of sample #2
    svar1 = variances of sample #1
    svar2 = variances of sample #2
    ssize1 = sample size of sample #1
    ssize2 = sample size of sample #2
    alpha = confidence level
    pmean1 = population mean of population #1 (optional)
    pmean2 = population mean of population #2 (optional)"""
    if not kwargs.has_key('pmean1'): 
        pmean1 = 0.0
    else: pmean1 = kwargs['pmean1']
    if not kwargs.has_key('pmean2'):
        pmean2 = 0.0
    else: pmean2 = kwargs['pmean2']
    smean1 = kwargs['smean1']
    smean2 = kwargs['smean2']
    svar1 = kwargs['svar1']
    svar2 = kwargs['svar2']
    ssize1 = kwargs['ssize1']
    ssize2 = kwargs['ssize2']
    df = ssize1 + ssize2 - 2
    pvar = (((ssize1 - 1) * svar1) + ((ssize2 - 1) * svar2)) / df
    statistic = ((smean1 - smean2) - (pmean1 - pmean2)) / \
                (pvar * sqrt((1 / ssize1) + (1 / ssize2)))
    return test(statistic, TDistribution(df = df), kwargs['alpha'])

def t2Mean2UnequalVariance(**kwargs):
    """
    Test 9: t-test for two population means (population variance unknown and 
    unequal)
    
    To investigate the significance of the difference between the means of 
    two populations when the population variances are unknown and unequal.
    
    Limitations:
    1. Weaker form of Test 3
    
    Parameters:
    smean1 = sample mean of sample #1
    smean2 = sample mean of sample #2
    svar1 = variances of sample #1
    svar2 = variances of sample #2
    ssize1 = sample size of sample #1
    ssize2 = sample size of sample #2
    alpha = confidence level
    pmean1 = population mean of population #1 (optional)
    pmean2 = population mean of population #2 (optional)"""
    if not kwargs.has_key('pmean1'): 
        pmean1 = 0.0
    else: pmean1 = kwargs['pmean1']
    if not kwargs.has_key('pmean2'):
        pmean2 = 0.0
    else: pmean2 = kwargs['pmean2']
    smean1 = kwargs['smean1']
    smean2 = kwargs['smean2']
    svar1 = kwargs['svar1']
    svar2 = kwargs['svar2']
    ssize1 = kwargs['ssize1']
    ssize2 = kwargs['ssize2']
    statistic = ((smean1 - smean2) - (pmean1 - pmean2)) / \
                sqrt((svar1 / ssize1) + (svar2 / ssize2))
    df = (((svar1 / ssize1) + (svar2 / ssize2)) ** 2) / \
        (((svar1 ** 2) / ((ssize1 ** 2) * (ssize1 - 1))) + \
            ((svar2 ** 2) / ((ssize2 ** 2) * (ssize2 - 1))))
    return test(statistic, TDistribution(df = df), kwargs['alpha'])

def tPaired(**kwargs):    
    """
    Test 10: t-test for two population means (method of paired comparisons)
    
    To investigate the significance of the difference between two population
    means when no assumption is made about the population variances.
    
    Parameters:
    smean1 = sample mean of sample #1
    smean2 = sample mean of sample #2
    svar = variance of differences between pairs
    ssize = sample size
    alpha = confidence level"""
    smean1 = kwargs['smean1']
    smean2 = kwargs['smean2']
    svar = kwargs['svar']
    ssize = kwargs['ssize']
    statistic = (smean1 - smean2) / sqrt(svar / ssize)
    return test(statistic, TDistribution(df = ssize - 1), kwargs['alpha'])
    
    """
    Test 11: t-test of a regression coefficient
    
    To investigate the significance of the regression coefficient.
    
    Limitations:
    1. Homoedasticity of values"""

def tPearsonCorrelation(**kwargs):    
    """
    Test 12: t-test of a correlation coefficient
    
    To investigate whether the difference between the sample correlation
    coefficient and zero is statistically significant.
    
    Limitations:
    1. Assumes population correlation coefficient to be zero (use Test 13 for 
    testing other population correlation coefficient
    2. Assumes a linear relationship (regression line as Y = MX + C)
    3. Independence of x-values and y-values
    
    Use Test 59 when these conditions cannot be met
    
    Parameters:
    r = calculated Pearson's product-moment correlation coefficient
    ssize = sample size"""
    ssize = kwargs['ssize']
    r = kwargs['r']
    statistic = (r * sqrt(ssize - 2)) / sqrt(1 - (r **2))
    return test(statistic, TDistribution(df = ssize - 2), kwargs['alpha'])

def ZPearsonCorrelation(**kwargs):    
    """
    Test 13: Z-test of a correlation coefficient
    
    To investigate the significance of the difference between a correlation
    coefficient and a specified value.
    
    Limitations:
    1. Assumes a linear relationship (regression line as Y = MX + C)
    2. Independence of x-values and y-values
    
    Use Test 59 when these conditions cannot be met
    
    Parameters:
    sr = calculated sample Pearson's product-moment correlation coefficient
    pr = specified Pearson's product-moment correlation coefficient to test
    ssize = sample size"""
    ssize = kwargs['ssize']
    sr = kwargs['sr']
    pr = kwargs['pr']
    Z1 = 0.5 * log((1 + sr) / (1 - sr))
    meanZ1 = 0.5 * log((1 + pr) / (1 - pr))
    sigmaZ1 = 1 / sqrt(ssize - 3)
    statistic = (Z1 - meanZ1) / sigmaZ1
    return test(statistic, NormalDistribution(), kwargs['alpha'])
    
    """
    Test 14: Z-test for two correlation coefficients
    
    To investigate the significance of the difference between the correlation
    coefficients for a pair variables occurring from two difference 
    populations."""
    
    """
    Test 15: Chi-square test for a population variance
    
    To investigate the difference between a sample variance and an assumed
    population variance."""
    
    """
    Test 16: F-test for two population variances (variance ratio test)
    
    To investigate the significance of the difference between two population
    variances."""
    
    