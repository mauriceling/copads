"""Collection of hypothesis testing routines.
Each routine will return a 3-element tuple: (result, statistic, critical)
where
result = True (reject null hypothesis; statistic > critical) or False (accept 
null hypothesis; statistic <= critical)
statistic = calculated statistic value
critical = value of critical region for statistical test

References:
Test 1-100: Gopal K. Kanji. 2006. 100 Statistical Tests, 3rd edition.
Sage Publications.

Copyright (c) Maurice H.T. Ling <mauriceling@acm.org>
Date created: 1st September 2008
"""

from StatisticsDistribution import *
from Operations import summation
from math import sqrt, log

def test(statistic, distribution, confidence):
    """Generates the critical value from distribution and confidence value using
    the distribution's inverseCDF method and performs 1-tailed and 2-tailed test 
    by comparing the calculated statistic with the critical value. 
    
    Returns a 5-element list:
    (left result, left critical, statistic, right critical, right result)
    where
    left result = True (statistic in lower critical region) or 
        False (statistic not in lower critical region)
    left critical = lower critical value generated from 1 - confidence
    statistic = calculated statistic value
    right critical = upper critical value generated from confidence
    right result = True (statistic in upper critical region) or
        False (statistic not in upper critical region)
        
    Therefore, null hypothesis is accepted if left result and right result are 
    both False in a 2-tailed test.
    
    @param statistic: calculated statistic (float)
    @param distribution: distribution to calculate critical value
    @type distribution: instance of a statistics distribution
    @param confidence: confidence level of a one-tail
        test (usually 0.95 or 0.99), use 0.975 or 0.995 for 2-tail test
    @type confidence: float of less than 1.0"""
    data = [None, None, statistic, None, None]
    data[1] = distribution.inverseCDF(1.0 - confidence)[0]
    if data[1] < statistic: data[0] = False
    else: data[0] = True
    data[3] = distribution.inverseCDF(confidence)[0]
    if statistic < data[3]: data[4] = False
    else: data[4] = True
    return data
    
def Z1Mean1Variance(**kwargs):
    """Test 1: Z-test for a population mean (variance known)
    
    To investigate the significance of the difference between an assumed 
    population mean and sample mean when the population variance is
    known.
    
    Limitations    
    - Requires population variance (use Test 7 if population variance unknown)
    
    @param smean: sample mean
    @param pmean: population mean
    @param pvar: population variance
    @param ssize: sample size
    @param confidence: confidence level"""
    smean = kwargs['smean']
    pmean = kwargs['pmean']
    pvar = kwargs['pvar']
    ssize = kwargs['ssize']
    statistic = abs(smean - pmean)/ \
                (pvar / sqrt(ssize))
    return test(statistic, NormalDistribution(), kwargs['confidence'])

def Z2Mean1Variance(**kwargs):
    """
    Test 2: Z-test for two population means (variances known and equal)
    
    To investigate the significance of the difference between the means of two 
    samples when the variances are known and equal.
    
    Limitations:
    1. Population variances must be known and equal (use Test 8 if population
    variances unknown
    
    @param smean1: sample mean of sample #1
    @param smean2: sample mean of sample #2
    @param pvar: variances of both populations (variances are equal)
    @param ssize1: sample size of sample #1
    @param ssize2: sample size of sample #2
    @param confidence: confidence level
    @param pmean1: population mean of population #1 (optional)
    @param pmean2: population mean of population #2 (optional)"""
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
                (pvar * sqrt((1.0 / ssize1) + (1.0 / ssize2)))
    return test(statistic, NormalDistribution(), kwargs['confidence'])    

def Z2Mean2Variance(**kwargs):    
    """
    Test 3: Z-test for two population means (variances known and unequal)
    
    To investigate the significance of the difference between the means of two
    samples when the variances are known and unequal.
    
    Limitations:
    1. Population variances must be known(use Test 9 if population variances 
    unknown
    
    @param smean1: sample mean of sample #1
    @param smean2: sample mean of sample #2
    @param pvar1: variance of population #1
    @param pvar2: variance of population #2
    @param ssize1: sample size of sample #1
    @param ssize2: sample size of sample #2
    @param confidence: confidence level
    @param pmean1: population mean of population #1 (optional)
    @param pmean2: population mean of population #2 (optional)"""
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
    return test(statistic, NormalDistribution(), kwargs['confidence'])

def Z1Proportion(**kwargs):    
    """
    Test 4: Z-test for a proportion (binomial distribution)
    
    To investigate the significance of the difference between an assumed 
    proportion and an observed proportion.
    
    Limitations:
    1. Requires sufficiently large sample size to use Normal approximation to
    binomial
    
    @param spro: sample proportion
    @param ppro: population proportion
    @param ssize: sample size
    @param confidence: confidence level"""
    spro = kwargs['spro']
    ppro = kwargs['ppro']
    ssize = kwargs['ssize']
    statistic = (abs(ppro - spro) - (1 / (2 * ssize)))/ \
                sqrt((ppro * (1 - spro)) / ssize)
    return test(statistic, NormalDistribution(), kwargs['confidence'])

def Z2Proportion(**kwargs):    
    """
    Test 5: Z-test for the equality of two proportions (binomial distribution)
    To investigate the assumption that the proportions of elements from two 
    populations are equal, based on two samples, one from each population.
    
    Limitations:
    1. Requires sufficiently large sample size to use Normal approximation to
    binomial
    
    @param spro1: sample proportion #1
    @param spro2: sample proportion #2
    @param ssize1: sample size #1
    @param ssize2: sample size #2
    @param confidence: confidence level"""
    spro1 = kwargs['spro1']
    spro2 = kwargs['spro2']
    ssize1 = kwargs['ssize1']
    ssize2 = kwargs['ssize2']
    P = ((spro1 * ssize1) + (spro2 * ssize2)) / (ssize1 + ssize2)
    statistic = (spro1 - spro2) / \
                (P * (1.0 - P) * ((1.0 / ssize1) + (1.0 / ssize2))) ** 0.5
    return test(statistic, NormalDistribution(), kwargs['confidence'])

def Z2Count(**kwargs):    
    """
    Test 6: Z-test for comparing two counts (Poisson distribution)
    
    To investigate the significance of the differences between two counts.
    
    Limitations:
    1. Requires sufficiently large sample size to use Normal approximation to
    binomial
    
    @param time1: first measurement time
    @param time2: second measurement time
    @param count1: counts at first measurement time
    @param count2: counts at second measurement time
    @param confidence: confidence level"""
    time1 = kwargs['time1']
    time2 = kwargs['time2']
    R1 = kwargs['count1'] / float(time1)
    R2 = kwargs['count2'] / float(time2)
    statistic = (R1 - R2) / sqrt((R1 / time1) + (R2 / time2))
    return test(statistic, NormalDistribution(), kwargs['confidence'])

def t1Mean(**kwargs):
    """
    Test 7: t-test for a population mean (population variance unknown)
    
    To investigate the significance of the difference between an assumed 
    population mean and a sample mean when the population variance is 
    unknown and cannot be assumed equal or not equal.
    
    Limitations:
    1. Weaker form of Test 1
    
    @param smean: sample mean
    @param pmean: population mean
    @param svar: sample variance
    @param ssize: sample size"""
    smean = kwargs['smean']
    pmean = kwargs['pmean']
    svar = kwargs['svar']
    ssize = kwargs['ssize']
    statistic = (smean - pmean) / (svar / sqrt(ssize))
    return test(statistic, TDistribution(df = ssize - 1), kwargs['confidence'])

def t2Mean2EqualVariance(**kwargs):    
    """
    Test 8: t-test for two population means (population variance unknown but 
    equal)
    
    To investigate the significance of the difference between the means of 
    two populations when the population variances are unknown but assumed
    equal.
    
    Limitations:
    1. Weaker form of Test 2
    
    @param smean1: sample mean of sample #1
    @param smean2: sample mean of sample #2
    @param svar1: variances of sample #1
    @param svar2: variances of sample #2
    @param ssize1: sample size of sample #1
    @param ssize2: sample size of sample #2
    @param confidence: confidence level
    @param pmean1: population mean of population #1 (optional)
    @param pmean2: population mean of population #2 (optional)"""
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
    return test(statistic, TDistribution(df = df), kwargs['confidence'])

def t2Mean2UnequalVariance(**kwargs):
    """
    Test 9: t-test for two population means (population variance unknown and 
    unequal)
    
    To investigate the significance of the difference between the means of 
    two populations when the population variances are unknown and unequal.
    
    Limitations:
    1. Weaker form of Test 3
    
    @param smean1: sample mean of sample #1
    @param smean2: sample mean of sample #2
    @param svar1: variances of sample #1
    @param svar2: variances of sample #2
    @param ssize1: sample size of sample #1
    @param ssize2: sample size of sample #2
    @param confidence: confidence level
    @param pmean1: population mean of population #1 (optional)
    @param pmean2: population mean of population #2 (optional)"""
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
    return test(statistic, TDistribution(df = df), kwargs['confidence'])

def tPaired(**kwargs):    
    """
    Test 10: t-test for two population means (method of paired comparisons)
    
    To investigate the significance of the difference between two population
    means when no assumption is made about the population variances.
    
    @param smean1: sample mean of sample #1
    @param smean2: sample mean of sample #2
    @param svar: variance of differences between pairs
    @param ssize: sample size
    @param confidence: confidence level"""
    smean1 = kwargs['smean1']
    smean2 = kwargs['smean2']
    svar = kwargs['svar']
    ssize = kwargs['ssize']
    statistic = (smean1 - smean2) / sqrt(svar / ssize)
    return test(statistic, TDistribution(df = ssize - 1), kwargs['confidence'])
    
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
    
    @param r: calculated Pearson's product-moment correlation coefficient
    @param ssize: sample size
    @param confidence: confidence level"""
    ssize = kwargs['ssize']
    r = kwargs['r']
    statistic = (r * sqrt(ssize - 2)) / sqrt(1 - (r **2))
    return test(statistic, TDistribution(df = ssize - 2), kwargs['confidence'])

def ZPearsonCorrelation(**kwargs):    
    """
    Test 13: Z-test of a correlation coefficient
    
    To investigate the significance of the difference between a correlation
    coefficient and a specified value.
    
    Limitations:
    1. Assumes a linear relationship (regression line as Y = MX + C)
    2. Independence of x-values and y-values
    
    Use Test 59 when these conditions cannot be met
    
    @param sr: calculated sample Pearson's product-moment correlation coefficient
    @param pr: specified Pearson's product-moment correlation coefficient to test
    @param ssize: sample size
    @param confidence: confidence level"""
    ssize = kwargs['ssize']
    sr = kwargs['sr']
    pr = kwargs['pr']
    Z1 = 0.5 * log((1 + sr) / (1 - sr))
    meanZ1 = 0.5 * log((1 + pr) / (1 - pr))
    sigmaZ1 = 1.0 / sqrt(ssize - 3)
    statistic = (Z1 - meanZ1) / sigmaZ1
    return test(statistic, NormalDistribution(), kwargs['confidence'])
    
def Z2PearsonCorrelation(**kwargs):    
    """
    Test 14: Z-test for two correlation coefficients
    
    To investigate the significance of the difference between the correlation
    coefficients for a pair variables occurring from two difference 
    populations.
    
    @param r1: Pearson correlation coefficient of sample #1
    @param r2: Pearson correlation coefficient of sample #2
    @param ssize1: Sample size #1
    @param ssize2: Sample size #2
    @param confidence: confidence level"""
    z1 = 0.5 * log((1.0 + kwargs['r1']) /(1.0 - kwargs['r1']))
    z2 = 0.5 * log((1.0 + kwargs['r2']) /(1.0 - kwargs['r2']))
    sigma1 = 1.0 / sqrt(kwargs['ssize1'] - 3)
    sigma2 = 1.0 / sqrt(kwargs['ssize2'] - 3)
    sigma = sqrt((sigma1 ** 2) + (sigma2 ** 2))
    statistic = abs(z1 - z2) / sigma
    return test(statistic, NormalDistribution(), kwargs['confidence'])

def t15(**kwargs):    
    """
    Test 15: Chi-square test for a population variance
    
    To investigate the difference between a sample variance and an assumed
    population variance."""
    return test(statistic, Distribution(), kwargs['confidence'])

def t16(**kwargs):    
    """
    Test 16: F-test for two population variances (variance ratio test)
    
    To investigate the significance of the difference between two population
    variances."""
    return test(statistic, Distribution(), kwargs['confidence'])
    
def t17(**kwargs):
	"""
	Test 17: F-test for two population variances (with correlated observations)
    
    To investigate the difference between two population variances when there 
    is correlation between the pairs of observations."""
	return test(statistic, Distribution(), kwargs['confidence'])

def t18(**kwargs):
	"""
	Test 18: Hotelling's T-square test for two series of population means
    
    To compare the results of two experiments, each of which yields a
    multivariate result. In another words, we wish to know if the mean pattern
    obtained from the first experiment agrees with the mean pattern obtained
    for the second."""
	return test(statistic, Distribution(), kwargs['confidence'])

def t19(**kwargs):
	"""
	Test 19: Discriminant test for the origin of a p-fold sample
    
    To investigate the origin of one species of values for p random variates,
    when one of two markedly different populations may have produced that
    particular series."""
	return test(statistic, Distribution(), kwargs['confidence'])

def t20(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t21(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t22(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def ZCorrProportion(**kwargs):
    """
    Test 23: Z-test for correlated proportions
    
    To investigate the significance of the difference between two correlated 
    proportions in opinion surveys. It can also be used for more general
    applications.
    
    Limitations:
    1. The same people are questioned both times (correlated property).
    2. Sample size must be quite large.
    
    @param ssize: sample size
    @param ny: number answered 'no' in first poll and 'yes' in second poll
    @param yn: number answered 'yes' in first poll and 'no' in second poll
    @param confidence: confidence level
    """    
    ssize = kwargs['ssize']
    ny = kwargs['ny']
    yn = kwargs['yn']
    sigma = (ny + yn) - (((ny - yn) ** 2.0) / ssize)
    sigma = sqrt(sigma / (ssize * (ssize - 1.0)))
    statistic = (ny - yn) / (sigma * ssize)
    return test(statistic, NormalDistribution(), kwargs['confidence'])

def Chisq2Variance(**kwargs):
    """
	Test 24: Chi-square test for an assumed population variance
    
    To investigate the significance of the difference between a population
    variance and an assumed variance value.
    
    Limitations:
    1. Sample from normal distribution
    
    @param ssize: sample size
    @param svar: sample variance
    @param pvar: population variance (assumed)
    @param confidence: confidence level"""
    ssize = kwargs['ssize']
    svar = kwargs['svar']
    pvar = kwargs['pvar']
    statistic = (svar / pvar) * (ssize - 1)
    return test(statistic, ChiSquareDistribution(df = ssize - 1), 
                kwargs['confidence'])

def F2Count(**kwargs):
    """
	Test 25: F-test for two counts (Poisson distribution)
    
    To investigate the significance of the difference between two counted
    results (based on a Poisson distribution).
    
    Limitations:
    1. Counts must satisfy a Poisson distribution
    2. Samples obtained under same conditions.

    @param count1: count of first sample
    @param count2: count of second sample
    @param repeat: flag for repeated sampling (default = False)
    @param time1: time at which first sample is taken 
        (only needed if repeat = True)
    @param time2:time at which second sample is taken 
        (only needed if repeat = True)
    """
    count1 = kwargs['count1']
    count2 = kwargs['count2']
    if not kwargs.has_key('repeat'): kwargs['repeat'] = False
    if kwargs['repeat'] == False:
        statistic = count1 / (count2 + 1)
        numerator = 2 * (count2 + 1)
        denominator = 2 * count1
    else:
        time1 = kwargs['time1']
        time2 = kwargs['time2']
        statistic = ((count1 + 0.5) / time1) / ((count2 + 0.5) / time2)
        numerator = 2 * count1 + 1
        denominator = 2 * count2 + 1
    return test(statistic, FDistribution(numerator = numerator,
                                denominator = denominator), kwargs['confidence'])

def t26(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t27(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t28(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t29(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t30(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t31(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t32(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t33(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t34(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t35(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t36(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def ChisqFit(**kwargs):
    """
	Test 37: Chi-square test for goodness of fit
    
    To investigate the significance of the differences between observed data
    arranged in K classes, and the theoretical expected frequencies in the
    K classes.
    
    Limitations:
    1. Observed and theoretical distributions should have same number of 
    elements
    2. Same class division for both distributions
    3. Expected frequency of each class should be at least 5
    
    @param observed: list of observed frequencies (index matched with expected)
    @param expected: list of expected frequencies (index matched with observed)
    @param confidence: confidence level""" 
    freq = [float(((observed[i] - expected[i]) ** 2) / expected[i])
            for i in range(len(observed))]
    statistic = 0.0
    for x in freq: statistic = statistic + x
    return test(statistic, ChiSqDistribution(df = len(observed) - 1), 
                kwargs['confidence'])

def t38(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t39(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def Chisq2x2(**kwargs):
    """
	Test 40: Chi-square test for consistency in 2x2 table
    
    To investigate the significance of the differences between observed
    frequencies for two dichotomous distributions.
    
    Limitations:
    1. Total sample size (sample 1 + sample 2) must be more than 20
    2. Each cell frequency more than 3
    
    @param s1: 2-element list or tuple of frequencies for sample #1
    @param s2: 2-element list or tuple of frequencies for sample #2
    @param confidence: confidence level"""
    s1c1 = kwargs['s1'][0]
    s1c2 = kwargs['s1'][1]
    s2c1 = kwargs['s2'][0]
    s2c2 = kwargs['s2'][1]
    statistic = (s1c1 + s1c2 + s2c1 + s2c2 - 1)
    statistic = statistic * (((s1c1 * s2c2) - (s1c2 * s2c1)) ** 2)
    statistic = statistic / ((s1c1 + s1c2)*(s2c1 + s2c2)* \
                            (s1c1 + s2c1)*(s1c2 + s2c2))
    return test(statistic, ChisqDistribution(df = 1), kwargs['confidence'])

def t41(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t42(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t43(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t44(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t45(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t46(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t47(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t48(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t49(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t50(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t51(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t52(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t53(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t54(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t55(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t56(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t57(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def SpearmanCorrelation(**kwargs):
    """Test 58: Spearman rank correlation test (paired observations)
    To investigate the significance of the correlation between two series of 
    observations obtained in pairs.
    
    Limitations:
    1. Assumes the two population distributions to be continuous
    2. Sample size must be more than 10
    
    @param R: sum of squared ranks differences
    @param ssize: sample size
    @param series1: ranks of series #1 (not used if R is given)
    @param series2: ranks of series #2 (not used if R is given)
    @param confidence: confidence level"""
    ssize = kwargs['ssize']
    if not kwargs.has_key('R'):
        series1 = kwargs['series1']
        series2 = kwargs['series2']
        R = [((series1[i] - series2[i]) ** 2) for i in range(len(series1))]
        R = summation(R)
    else:
        R = kwargs['R']
    statistic = (6.0 * R) - (ssize * ((ssize ** 2) - 1.0))
    statistic = statistic / (ssize * (ssize + 1.0) * sqrt(ssize - 1.0))
    return test(statistic, NormalDistribution(), kwargs['confidence'])

def t59(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t60(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t61(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t62(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t63(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t64(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t65(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t66(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t67(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t68(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t69(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t70(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t71(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t72(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t73(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t74(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t75(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t76(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t77(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t78(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t79(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t80(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t81(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t82(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t83(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t84(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t85(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t86(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t87(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t88(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t89(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t90(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t91(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t92(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t93(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t94(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t95(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t96(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t97(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t98(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t99(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

def t100(**kwargs):
	"""
	"""
	return test(statistic, Distribution(), kwargs['confidence'])

