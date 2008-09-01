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
from math import sqrt

def test(statistic, critical):
    """
    Compares test statistic and critical region for alternate hypothesis 
    acceptance (returns True, reject null hypothesis and accept alternate
    hypothesis where statistic > critical) or rejection (returns false, 
    accept null hypothesis and reject alternate hypothesis where 
    statistic <= critical)"""
    if statistic < critical: return False
    else: return True
    
def Z1Mean1Variance(**kwargs):
    """
    Test 1: Z-test for a population mean (variance known)
    
    To investigate the significance of the difference between an assumed 
    population mean and sample mean when the population variance is
    known.
    
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
    Z = (smean - pmean)/ \
        (pvar / sqrt(ssize))
    distribution = NormalDistribution()
    x = distribution.inverseCDF(kwargs['alpha'])
    return (test(Z, x), Z, x)

def Z2Mean1Variance(**kwargs):
    """
    Test 2: Z-test for two population means (variances known and equal)
    
    To investigate the significance of the difference between the means of two 
    samples when the variances are known and equal.
    
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
    Z = ((smean1 - smean2) - (pmean1 - pmean2))/ \
        (pvar * sqrt((1 / ssize1) + (1 / ssize2)))
    distribution = NormalDistribution()
    x = distribution.inverseCDF(kwargs['alpha'])
    return (test(Z, x), Z, x)
    
def Z2Mean2Variance(**kwargs):    
    """
    Test 3: Z-test for two population means (variances known and unequal)
    
    To investigate the significance of the difference between the means of two
    samples when the variances are known and unequal.
    
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
    Z = ((smean1 - smean2) - (pmean1 - pmean2))/ \
        sqrt((pvar1 / ssize1) + (pvar2 / ssize2))
    distribution = NormalDistribution()
    x = distribution.inverseCDF(kwargs['alpha'])
    return (test(Z, x), Z, x)

def Z1Proportion(**kwargs):    
    """
    Test 4: Z-test for a proportion (binomial distribution)
    
    To investigate the significance of the difference between an assumed 
    proportion and an observed proportion.
    
    Parameters:
    spro = sample proportion
    ppro = population proportion
    ssize = sample size
    alpha = confidence level"""
    spro = kwargs['spro']
    ppro = kwargs['ppro']
    ssize = kwargs['ssize']
    Z = (abs(ppro - spro) - (1 / (2 * ssize)))/ \
        sqrt((ppro * (1 - spro)) / ssize)
    distribution = NormalDistribution()
    x = distribution.inverseCDF(kwargs['alpha'])
    return (test(Z, x), Z, x)

def Z2Proportion(**kwargs):    
    """
    Test 5: Z-test for the equality of two proportions (binomial distribution)
    To investigate the assumption that the proportions of elements from two 
    populations are equal, based on two samples, one from each population.
    
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
    Z = (spro1 - spro2) / \
        sqrt((P * (1 - P)) * ((1 / ssize1) * (1 / ssize2)))
    distribution = NormalDistribution()
    x = distribution.inverseCDF(kwargs['alpha'])
    return (test(Z, x), Z, x)

def Z2Count(**kwargs):    
    """
    Test 6: Z-test for comparing two counts (Poisson distribution)
    
    To investigate the significance of the differences between two counts.
    
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
    Z = (R1 - R2) / sqrt((R1 / time1) + (R2 / time2))
    distribution = NormalDistribution()
    x = distribution.inverseCDF(kwargs['alpha'])
    return (test(Z, x), Z, x)

def t1Mean(**kwargs):
    """
    Test 7: t-test for a population mean (population variance unknown)
    
    To investigate the significance of the difference between an assumed 
    population mean and a sample mean when the population variance is 
    unknown and cannot be assumed equal or not equal.
    
    Parameters:
    smean = sample mean
    pmean = population mean
    svar = sample variance
    ssize = sample size"""
    smean = kwargs['smean']
    pmean = kwargs['pmean']
    svar = kwargs['svar']
    ssize = kwargs['ssize']
    t = (smean - pmean) / (svar / sqrt(ssize))
    distribution = TDistribution(location = 0.0, scale = svar, df = ssize - 1)
    x = distribution.inverseCDF(kwargs['alpha'])
    return (test(t, x), t, x)

def t2Mean2EqualVariance(**kwargs):    
    """
    Test 8: t-test for two population means (population variance unknown but 
    equal)
    
    To investigate the significance of the difference between the means of 
    two populations when the population variances are unknown but assumed
    equal.
    
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
    t = ((smean1 - smean2) - (pmean1 - pmean2)) / \
        (pvar * sqrt((1 / ssize1) + (1 / ssize2)))
    distribution = TDistribution(df = df)
    x = distribution.inverseCDF(kwargs['alpha'])
    return (test(t, x), t, x)

def t2Mean2UnequalVariance(**kwargs):
    """
    Test 9: t-test for two population means (population variance unknown and 
    unequal)
    
    To investigate the significance of the difference between the means of 
    two populations when the population variances are unknown and unequal.
    
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
    t = ((smean1 - smean2) - (pmean1 - pmean2)) / \
        sqrt((svar1 / ssize1) + (svar2 / ssize2))
    df = (((svar1 / ssize1) + (svar2 / ssize2)) ** 2) / \
        (((svar1 ** 2) / ((ssize1 ** 2) * (ssize1 - 1))) + \
            ((svar2 ** 2) / ((ssize2 ** 2) * (ssize2 - 1))))
    distribution = TDistribution(df = df)
    x = distribution.inverseCDF(kwargs['alpha'])
    return (test(t, x), t, x)
    
    """
    Test 10: t-test for two population means (method of paired comparisons)
    
    To investigate the significance of the difference between two population
    means when no assumption is made about the population variances."""
    
    """
    Test 11: t-test of a regression coefficient
    
    To investigate the significance of the regression coefficient."""
    
    """
    Test 12: t-test of a correlation coefficient
    
    To investigate whether the difference between the sample correlation
    coefficient and zero is statistically significant."""
    
    """
    Test 13: Z-test of a correlation coefficient
    
    To investigate the significance of the difference between a correlation
    coefficient and a specified value."""
    
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
    
    