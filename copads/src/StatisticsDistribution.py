"""
File containing the functions for various statistical distributions.
References:
1. Regress+ A compendium of common probability distributions (version 2.3)
by Michael P. McLaughlin (mpmcl@mitre.org)
http://www.causascientia.org/math_stat/Dists/Compendium.pdf
2. Hand-book on statistical distributions for experimentalists
Internal report SUF-PFY/96-01. University of Stockholms
by Christian Walck (walck@physto.se)

Copyright (c) Maurice H.T. Ling <mauriceling@acm.org>
Date created: 17th August 2005
"""

import math
import random
from CopadsExceptions import DistributionParameterError
from CopadsExceptions import DistributionFunctionError
from CopadsExceptions import NormalDistributionTypeError
import NRPy
from Constants import *

class Distribution:
    """
    Abstract class for all statistical distributions.
    Due to the large variations of parameters for each distribution, it is 
    unlikely to be able to standardize a parameter list for each method that 
    is meaningful for all distributions. Instead, the parameters to construct 
    each distribution is to be given as keyword arguments.
    """
    def __init__(self, **parameters): 
        """Constructor method. The parameters are used to construct the 
        probability distribution."""
        raise DistributionFunctionError
    def CDF(self, x): 
        """
        Cummulative Distribution Function, which gives the cummulative 
        probability (area under the probability curve) from -infinity or 0 to 
        a give x-value on the x-axis where y-axis is the probability. CDF is 
        also known as density function."""
        raise DistributionFunctionError
    def PDF(self, x): 
        """
        Partial Distribution Function, which gives the probability for the 
        particular value of x, or the area under probability distribution from 
        x-h to x+h for continuous distribution."""
        raise DistributionFunctionError
    def inverseCDF(self, probability, start = 0.0, step =0.01): 
        """
        It does the reverse of CDF() method, it takes a probability value and 
        returns the corresponding value on the x-axis."""
        raise DistributionFunctionError
    def mean(self): 
        """Gives the arithmetic mean of the sample."""
        raise DistributionFunctionError
    def mode(self): 
        """Gives the mode of the sample, if closed-form is available."""
        raise DistributionFunctionError
    def kurtosis(self): 
        """Gives the kurtosis of the sample."""
        raise DistributionFunctionError
    def skew(self): 
        """Gives the skew of the sample."""
        raise DistributionFunctionError
    def variance(self): 
        """Gives the variance of the sample."""
        raise DistributionFunctionError
    def quantile1(self): 
        """Gives the 1st quantile of the sample, if closed-form is available."""
        raise DistributionFunctionError
    def quantile3(self): 
        """Gives the 3rd quantile of the sample, if closed-form is available."""
        raise DistributionFunctionError
    def qmean(self): 
        """Gives the quantile of the arithmetic mean of the sample, if 
        closed-form is available."""
        raise DistributionFunctionError
    def qmode(self): 
        """Gives the quantile of the mode of the sample, if closed-form is 
        available."""
        raise DistributionFunctionError
    def random(self):
        """Gives a random number based on the distribution."""
        raise DistributionFunctionError
        

class BetaDistribution(Distribution):
    def __init__(self, **parameters): 
        """Constructor method. The parameters are used to construct the 
        probability distribution."""
        try:
            self.location = parameters['location']
            self.scale = parameters['scale']
            self.p = parameters['p']
            self.q = parameters['q']
        except KeyError: 
            raise DistributionParameterError('Beta distribution requires \
        location, scale (upper bound), p and q (shape parameters)')
    def CDF(self, x): 
        """
        Cummulative Distribution Function, which gives the cummulative 
        probability (area under the probability curve) from -infinity or 0 to 
        a give x-value on the x-axis where y-axis is the probability."""
        return NRPy.betai(self.p, self.q, (x - self.location)/ 
                                            (self.scale - self.location))
    def PDF(self, x): 
        """
        Partial Distribution Function, which gives the probability for the 
        particular value of x, or the area under probability distribution from 
        x-h to x+h for continuous distribution."""
        n = (self.scale - self.location) ** (self.p + self.q - 1)
        n = NRPy.gammln(self.p) * NRPy.gammln(self.q) * n
        n = NRPy.gammln(self.p + self.q)/n
        p = (x - self.location) ** (self.p - 1)
        q = (self.scale - x) ** (self.q - 1)
        return n * p * q
    def inverseCDF(self, probability, start = 0.0, step = 0.01): 
        """
        It does the reverse of CDF() method, it takes a probability value and 
        returns the corresponding value on the x-axis."""
        cprob = self.CDF(start)
        if probability < cprob: return (start, cprob)
        while (probability > cprob):
            start = start + step
            cprob = self.CDF(start)
            # print start, cprob
        return (start, cprob)
            
    def mean(self): 
        """Gives the arithmetic mean of the sample."""
        n = (self.location * self.q) + (self.scale * self.p)
        return n / (self.p + self.q)
    def mode(self): 
        """Gives the mode of the sample."""
        n = (self.location * (self.q - 1)) + (self.scale * (self.p - 1))
        return n / (self.p + self.q - 2)
    def kurtosis(self): 
        """Gives the kurtosis of the sample."""
        n = (self.p ** 2) * (self.q + 2) + \
            (2 * (self.q ** 2)) + \
            ((self.p * self.q) * (self.q - 2))
        n = n * (self.p + self.q + 1)
        d = self.p * self.q * (self.p + self.q + 2) * (self.p + self.q + 3)
        return 3 * ((n / d) - 1)
    def skew(self): 
        """Gives the skew of the sample."""
        d = (self.p + self.q) ** 3
        d = d * (self.p + self.q + 1) * (self.p + self.q + 2)
        e = ((self.p + self.q) ** 2) * (self.p + self.q + 1)
        e = (self.p * self.q) / e
        e = e ** 1.5
        return ((2 * self.p * self.q) * (self.q - self.q))/(d * e)
    def variance(self): 
        """Gives the variance of the sample."""
        n = self.p * self.q * ((self.scale - self.location) ** 2)
        d = (self.p + self.q + 1) * ((self.p + self.q) ** 2)
        return n/d
    def moment(self, r):
        """Gives the r-th moment of the sample."""
        return NRPy.beta(self.p + r, self.q)/NRPy.beta(self.p, self.q)
    def random(self):
        """Gives a random number based on the distribution."""
        return random.betavariate(self.p. self.q)


class BinomialDistribution(Distribution):
    def __init__(self, **parameters): 
        """Constructor method. The parameters are used to construct the 
        probability distribution."""
        try: self.success = float(parameters['success'])
        except KeyError: self.success = 0.5
        try: self.trial = int(parameters['trial'])
        except KeyError: self.trial = 1000
    def CDF(self, x): 
        """
        Cummulative Distribution Function, which gives the cummulative 
        probability (area under the probability curve) from -infinity or 0 to 
        a give x-value on the x-axis where y-axis is the probability."""
        return NRPy.cdf_binomial(x, self.trial, self.success)
    def PDF(self, x): 
        """
        Partial Distribution Function, which gives the probability for the 
        particular value of x, or the area under probability distribution from 
        x-h to x+h for continuous distribution."""
        x = int(x)
        return NRPy.bico(self.trial, x) * \
            (self.success ** x) * \
            ((1 - self.success) ** (self.trial - x))
    def inverseCDF(self, probability, start = 0, step = 1): 
        """
        It does the reverse of CDF() method, it takes a probability value and 
        returns the corresponding value on the x-axis."""
        cprob = self.CDF(start)
        if probability < cprob: return (start, cprob)
        while (probability > cprob):
            start = start + step
            cprob = self.CDF(start)
            # print start, cprob
        return (start, cprob)
    def mean(self): 
        """Gives the arithmetic mean of the sample."""
        return self.success * self.trial
    def mode(self): 
        """Gives the mode of the sample."""
        return int(self.success * (self.trial + 1))
    def kurtosis(self): 
        """Gives the kurtosis of the sample."""
        return 1 - ((6 * self.success * (1 - self.success)))/ \
            (self.trial * self.success * (1 - self.success))
    def skew(self): 
        """Gives the skew of the sample."""
        return (1 - self.success - self.success)/ \
            ((self.trial * self.success * (1 - self.success)) **0.5)
    def variance(self): 
        """Gives the variance of the sample."""
        return self.mean() * (1 - self.success)
#    def random(self):
#        """Gives a random number based on the distribution."""
#        raise DistributionFunctionError


class CauchyDistribution(Distribution):
    def __init__(self, **parameters): 
        """Constructor method. The parameters are used to construct the 
        probability distribution."""
        try: self.location = parameter['location']
        except KeyError: self.location = 0.0
        try: self.scale = parameter['scale']
        except KeyError: self.scale = 1.0
    def CDF(self, x): 
        """
        Cummulative Distribution Function, which gives the cummulative 
        probability (area under the probability curve) from -infinity or 0 to 
        a give x-value on the x-axis where y-axis is the probability."""
        return 0.5 + 1/PI * atan((x-self.location)/self.scale)
    def PDF(self, x): 
        """
        Partial Distribution Function, which gives the probability for the 
        particular value of x, or the area under probability distribution from 
        x-h to x+h for continuous distribution."""
        return 1 / (PI * self.scale * (1 + (((x - self.location)/self.scale) ** 2)))
    def inverseCDF(self, probability, start = 0.0, step = 0.01): 
        """
        It does the reverse of CDF() method, it takes a probability value and 
        returns the corresponding value on the x-axis."""
        cprob = self.CDF(start)
        if probability < cprob: return (start, cprob)
        while (probability > cprob):
            start = start + step
            cprob = self.CDF(start)
            # print start, cprob
        return (start, cprob)
    def mean(self): 
        """Gives the arithmetic mean of the sample."""
        raise DistributionFunctionError('Mean for Cauchy Distribution is \
            undefined')
    def mode(self): 
        """Gives the mode of the sample."""
        return self.location
    def median(self): 
        """Gives the median of the sample."""
        return self.location
    def quantile1(self): 
        """Gives the 1st quantile of the sample."""
        return self.location - self.scale
    def quantile3(self): 
        """Gives the 3rd quantile of the sample."""
        return self.location + self.scale
    def qmode(self): 
        """Gives the quantile of the mode of the sample."""
        return 0.5
    def kurtosis(self): 
        """Gives the kurtosis of the sample."""
        raise DistributionFunctionError('Kurtosis for Cauchy Distribution is \
            undefined')
    def skew(self): 
        """Gives the skew of the sample."""
        raise DistributionFunctionError('Skew for Cauchy Distribution is \
            undefined')
    def variance(self): 
        """Gives the variance of the sample."""
        raise DistributionFunctionError('Variance for Cauchy Distribution is \
            undefined')
#    def random(self):
#        """Gives a random number based on the distribution."""
#        raise DistributionFunctionError


class ChiSquareDistribution(Distribution):
#    def __init__(self, **parameters): 
#        """Constructor method. The parameters are used to construct the 
#           probability distribution."""
#        raise DistributionFunctionError
#    def CDF(self, x): 
#        """
#        Cummulative Distribution Function, which gives the cummulative 
#        probability (area under the probability curve) from -infinity or 0 to 
#        a give x-value on the x-axis where y-axis is the probability."""
#        raise DistributionFunctionError
#    def PDF(self, x): 
#        """
#        Partial Distribution Function, which gives the probability for the 
#        particular value of x, or the area under probability distribution 
#        from x-h to x+h for continuous distribution."""
#        raise DistributionFunctionError
    def inverseCDF(self, probability, start = 0.0, step = 0.01): 
        """
        It does the reverse of CDF() method, it takes a probability value and 
        returns the corresponding value on the x-axis."""
        cprob = self.CDF(start)
        if probability < cprob: return (start, cprob)
        while (probability > cprob):
            start = start + step
            cprob = self.CDF(start)
            # print start, cprob
        return (start, cprob)
#    def mean(self): 
#        """Gives the arithmetic mean of the sample."""
#        raise DistributionFunctionError
#    def mode(self): 
#        """Gives the mode of the sample."""
#        raise DistributionFunctionError
#    def kurtosis(self): 
#        """Gives the kurtosis of the sample."""
#        raise DistributionFunctionError
#    def skew(self): 
#        """Gives the skew of the sample."""
#        raise DistributionFunctionError
#    def variance(self): 
#        """Gives the variance of the sample."""
#        raise DistributionFunctionError
#    def random(self):
#        """Gives a random number based on the distribution."""
#        raise DistributionFunctionError


class CosineDistribution(Distribution):
    def __init__(self, **parameters): 
        """Constructor method. The parameters are used to construct the 
        probability distribution."""
        try: self.location = parameters['location']
        except KeyError: self.location = 0.0
        try: self.scale = parameters['scale']
        except KeyError: self.scale = 1.0
    def CDF(self, x): 
        """
        Cummulative Distribution Function, which gives the cummulative 
        probability (area under the probability curve) from -infinity or 0 to 
        a give x-value on the x-axis where y-axis is the probability."""
        n = PI + (x - self.location)/self.scale + \
            math.sin((x - self.location)/self.scale)
        return (1/PI2) * n
    def PDF(self, x): 
        """
        Partial Distribution Function, which gives the probability for the 
        particular value of x, or the area under probability distribution from 
        x-h to x+h for continuous distribution."""
        return (1/(PI2 * self.scale)) * \
                (1 + math.cos((x - self.location)/self.scale))
    def inverseCDF(self, probability, start = 0.0, step = 0.01): 
        """
        It does the reverse of CDF() method, it takes a probability value and 
        returns the corresponding value on the x-axis."""
        cprob = self.CDF(start)
        if probability < cprob: return (start, cprob)
        while (probability > cprob):
            start = start + step
            cprob = self.CDF(start)
            # print start, cprob
        return (start, cprob)
    def mean(self): 
        """Gives the arithmetic mean of the sample."""
        return self.location
    def mode(self): 
        """Gives the mode of the sample."""
        return self.location
    def median(self): 
        """Gives the median of the sample."""
        return self.location
    def kurtosis(self): 
        """Gives the kurtosis of the sample."""
        return -0.5938
    def skew(self): 
        """Gives the skew of the sample."""
        return 0.0
    def variance(self): 
        """Gives the variance of the sample."""
        return (((PI * PI)/3) - 2) * (self.scale ** 2)
    def quantile1(self): 
        """Gives the 1st quantile of the sample."""
        return self.location - (0.8317 * self.scale)
    def quantile3(self): 
        """Gives the 13rd quantile of the sample."""
        return self.location + (0.8317 * self.scale)
    def qmean(self): 
        """Gives the quantile of the arithmetic mean of the sample."""
        return 0.5
    def qmode(self): 
        """Gives the quantile of the mode of the sample."""
        return 0.5
#    def random(self):
#        """Gives a random number based on the distribution."""
#        raise DistributionFunctionError


class ExponentialDistribution(Distribution):
    def __init__(self, **parameters): 
        """Constructor method. The parameters are used to construct the 
        probability distribution."""
        try: self.location = parameters['location']
        except KeyError: self.location = 0.0
        try: self.scale = parameters['scale']
        except KeyError: self.scale = 1.0
    def CDF(self, x): 
        """
        Cummulative Distribution Function, which gives the cummulative 
        probability (area under the probability curve) from -infinity or 0 to 
        a give x-value on the x-axis where y-axis is the probability."""
        return 1 - math.exp((self.location - x)/self.scale)
    def PDF(self, x): 
        """
        Partial Distribution Function, which gives the probability for the 
        particular value of x, or the area under probability distribution from 
        x-h to x+h for continuous distribution."""
        return (1/self.scale) * math.exp((self.location - x)/self.scale)
    def inverseCDF(self, probability, start = 0.0, step = 0.01): 
        """
        It does the reverse of CDF() method, it takes a probability value and 
        returns the corresponding value on the x-axis."""
        cprob = self.CDF(start)
        if probability < cprob: return (start, cprob)
        while (probability > cprob):
            start = start + step
            cprob = self.CDF(start)
            # print start, cprob
        return (start, cprob)
    def mean(self): 
        """Gives the arithmetic mean of the sample."""
        return self.location + self.scale
    def mode(self): 
        """Gives the mode of the sample."""
        return self.location
    def median(self): 
        """Gives the median of the sample."""
        return self.location + (self.scale * math.log10(2))
    def kurtosis(self): 
        """Gives the kurtosis of the sample."""
        return 6.0
    def skew(self): 
        """Gives the skew of the sample."""
        return 2.0
    def variance(self): 
        """Gives the variance of the sample."""
        return self.scale * self.scale
    def quantile1(self): 
        """Gives the 1st quantile of the sample."""
        return self.location + (self.scale * math.log10(1.333))
    def quantile3(self): 
        """Gives the 3rd quantile of the sample."""
        return self.location + (self.scale * math.log10(4))
    def qmean(self): 
        """Gives the quantile of the arithmetic mean of the sample."""
        return 0.6321
    def qmode(self): 
        """Gives the quantile of the mode of the sample."""
        return 0.0
    def random(self):
        """Gives a random number based on the distribution."""
        return random.expovariate(1/self.location)


class FDistribution(Distribution):
#    def __init__(self, **parameters): 
#        """Constructor method. The parameters are used to construct the 
#        probability distribution."""
#        raise DistributionFunctionError
#    def CDF(self, x): 
#        """
#        Cummulative Distribution Function, which gives the cummulative 
#        probability (area under the probability curve) from -infinity or 0 to 
#        a give x-value on the x-axis where y-axis is the probability."""
#        raise DistributionFunctionError
#    def PDF(self, x): 
#        """
#        Partial Distribution Function, which gives the probability for the 
#        particular value of x, or he area under probability distribution from 
#        x-h to x+h for continuous distribution."""
#        raise DistributionFunctionError
    def inverseCDF(self, probability, start = 0.0, step = 0.01): 
        """
        It does the reverse of CDF() method, it takes a probability value and returns the corresponding 
        value on the x-axis."""
        cprob = self.CDF(start)
        if probability < cprob: return (start, cprob)
        while (probability > cprob):
            start = start + step
            cprob = self.CDF(start)
            # print start, cprob
        return (start, cprob)
#    def mean(self): 
#        """Gives the arithmetic mean of the sample."""
#        raise DistributionFunctionError
#    def mode(self): 
#        """Gives the mode of the sample."""
#        raise DistributionFunctionError
#    def kurtosis(self): 
#        """Gives the kurtosis of the sample."""
#        raise DistributionFunctionError
#    def skew(self): 
#        """Gives the skew of the sample."""
#        raise DistributionFunctionError
#    def variance(self): 
#        """Gives the variance of the sample."""
#        raise DistributionFunctionError
#    def random(self):
#        """Gives a random number based on the distribution."""
#        raise DistributionFunctionError


class GeometricDistribution(Distribution):
    pass
    def __init__(self, **parameters): 
        """Constructor method. The parameters are used to construct the 
        probability distribution."""
        try: self.prob = parameters['success']
        except KeyError: self.prob = 0.5
    def CDF(self, x): 
        """
        Cummulative Distribution Function, which gives the cummulative 
        probability (area under the probability curve) from -infinity or 0 to 
        a give x-value on the x-axis where y-axis is the probability."""
        sum = 0.0
        for i in range(int(x)): sum = sum + self.PDF(i)
        return sum
    def PDF(self, x): 
        """
        Partial Distribution Function, which gives the probability for the 
        particular value of x, or the area under probability distribution from 
        x-h to x+h for continuous distribution."""
        return self.prob * ((1 - self.prob) ** (x - 1))
    def inverseCDF(self, probability, start = 0, step = 1): 
        """
        It does the reverse of CDF() method, it takes a probability value and 
        returns the corresponding value on the x-axis."""
        cprob = self.CDF(start)
        if probability < cprob: return (start, cprob)
        while (probability > cprob):
            start = start + step
            cprob = self.CDF(start)
            # print start, cprob
        return (start, cprob)
    def mean(self): 
        """Gives the arithmetic mean of the sample."""
        return 1/self.prob
    def mode(self): 
        """Gives the mode of the sample."""
        return 1.0
#    def kurtosis(self): 
#        """Gives the kurtosis of the sample."""
#        raise DistributionFunctionError
#    def skew(self): 
#        """Gives the skew of the sample."""
#        raise DistributionFunctionError
    def variance(self): 
        """Gives the variance of the sample."""
        return (1 - self.prob) / (self.prob ** 2)
#    def random(self):
#        """Gives a random number based on the distribution."""
#        raise DistributionFunctionError


class GumbelDistribution(Distribution):
    def __init__(self, **parameters): 
        """Constructor method. The parameters are used to construct the 
        probability distribution."""
        try:
            self.location = parameters['location']
            self.scale = parameters['scale']
        except KeyError: 
            raise DistributionParameterError('Gumbel distribution requires \
                location and scale.')
    def CDF(self, x): 
        """
        Cummulative Distribution Function, which gives the cummulative 
        probability (area under the probability curve) from -infinity or 0 to 
        a give x-value on the x-axis where y-axis is the probability."""
        return math.exp(-1 * math.exp((self.location - x)/self.scale))
    def PDF(self, x): 
        """
        Partial Distribution Function, which gives the probability for the 
        particular value of x, or the area under probability distribution from 
        x-h to x+h for continuous distribution."""
        return (1/self.scale) * math.exp((self.location - x)/self.scale) * \
            self.CDF(x)
    def inverseCDF(self, probability, start = 0.0, step = 0.01): 
        """
        It does the reverse of CDF() method, it takes a probability value and 
        returns the corresponding value on the x-axis."""
        cprob = self.CDF(start)
        if probability < cprob: return (start, cprob)
        while (probability > cprob):
            start = start + step
            cprob = self.CDF(start)
            # print start, cprob
        return (start, cprob)
    def mean(self): 
        """Gives the arithmetic mean of the sample."""
        return self.location + (GAMMA * self.scale)
    def mode(self): 
        """Gives the mode of the sample."""
        return self.location
    def median(self): 
        """Gives the median of the sample."""
        return self.location - self.scale * math.log10(math.log10(2))
    def kurtosis(self): 
        """Gives the kurtosis of the sample."""
        return 2.4
    def skew(self): 
        """Gives the skew of the sample."""
        return 1.1395
    def variance(self): 
        """Gives the variance of the sample."""
        return 1.667 * ((PI * self.scale) ** 2)
    def quantile1(self): 
        """Gives the 1st quantile of the sample."""
        return self.location - self.scale * math.log10(math.log10(4))
    def quantile3(self): 
        """Gives the 3rd quantile of the sample."""
        return self.location - self.scale * math.log10(math.log10(1.333))
    def qmean(self): 
        """Gives the quantile of the arithmetic mean of the sample."""
        return 0.5704
    def qmode(self): 
        """Gives the quantile of the mode of the sample."""
        return 0.3679
#    def random(self):
#        """Gives a random number based on the distribution."""
#        raise DistributionFunctionError


class HypergeometricDistribution(Distribution):
    def __init__(self, **parameters): 
        """Constructor method. The parameters are used to construct the 
            probability distribution."""
        raise DistributionFunctionError
#    def CDF(self, x): 
#       """
#        Cummulative Distribution Function, which gives the cummulative 
#        probability (area under the probability curve) from -infinity or 0 to 
#        a give x-value on the x-axis where y-axis is the probability."""
#        raise DistributionFunctionError
#    def PDF(self, x): 
#        """
#        Partial Distribution Function, which gives the probability for the 
#        particular value of x, or the area under probability distribution 
#        from x-h to x+h for continuous distribution."""
#        raise DistributionFunctionError
#    def inverseCDF(self, probability, start = 0.0, step = 0.01): 
#        """
#        It does the reverse of CDF() method, it takes a probability value 
#        and returns the corresponding value on the x-axis."""
#        cprob = self.CDF(start)
#        if probability < cprob: return (start, cprob)
#        while (probability > cprob):
#            start = start + step
#            cprob = self.CDF(start)
#            # print start, cprob
#        return (start, cprob)
#    def mean(self): 
#        """Gives the arithmetic mean of the sample."""
#        raise DistributionFunctionError
#    def mode(self): 
#        """Gives the mode of the sample."""
#        raise DistributionFunctionError
#    def kurtosis(self): 
#        """Gives the kurtosis of the sample."""
#        raise DistributionFunctionError
#    def skew(self): 
#        """Gives the skew of the sample."""
#        raise DistributionFunctionError
#    def variance(self): 
#        """Gives the variance of the sample."""
#        raise DistributionFunctionError
#    def quantile1(self): 
#        """Gives the 1st quantile of the sample."""
#        raise DistributionFunctionError
#    def quantile3(self): 
#        """Gives the 3rd quantile of the sample."""
#        raise DistributionFunctionError
#    def qmean(self): 
#        """Gives the quantile of the arithmetic mean of the sample."""
#        raise DistributionFunctionError
#    def qmode(self): 
#        """Gives the quantile of the mode of the sample."""
#        raise DistributionFunctionError
#    def random(self):
#        """Gives a random number based on the distribution."""
#        raise DistributionFunctionError
        
class LogarithmicDistribution(Distribution):
    def __init__(self, **parameters): 
        """Constructor method. The parameters are used to construct the 
        probability distribution."""
        try: self.shape = parameters['shape']
        except KeyError: 
            raise DistributionParameterError('Logarithmic distribution \
                requires share parameter')
    def CDF(self, x): 
        """
        Cummulative Distribution Function, which gives the cummulative 
        probability (area under the probability curve) from -infinity or 0 to 
        a give x-value on the x-axis where y-axis is the probability."""
        sum = 0.0
        for i in range(x): sum = sum + self.PDF(i)
        return sum
    def PDF(self, x): 
        """
        Partial Distribution Function, which gives the probability for the 
        particular value of x, or the area under probability distribution from 
        x-h to x+h for continuous distribution."""
        return (-1 * (self.shape ** x)) / (math.log10(1 - self.shape) * x)
    def inverseCDF(self, probability, start = 0.0, step = 0.01): 
        """
        It does the reverse of CDF() method, it takes a probability value and 
        returns the corresponding value on the x-axis."""
        cprob = self.CDF(start)
        if probability < cprob: return (start, cprob)
        while (probability > cprob):
            start = start + step
            cprob = self.CDF(start)
            # print start, cprob
        return (start, cprob)
    def mean(self): 
        """Gives the arithmetic mean of the sample."""
        return (-1 * self.shape)/((1 - self.shape) * \
                math.log10(1 - self.shape))
    def mode(self): 
        """Gives the mode of the sample."""
        return 1.0
#    def kurtosis(self): 
#        """Gives the kurtosis of the sample."""
#        raise DistributionFunctionError
#    def skew(self): 
#        """Gives the skew of the sample."""
#        raise DistributionFunctionError
    def variance(self): 
        """Gives the variance of the sample."""
        n = (-1 * self.shape) * (self.shape + math.log10(1 - self.shape))
        d = ((1 - self.shape) ** 2) * math.log10(1 - self.shape) * \
            math.log10(1 - self.shape)
        return n / d
#    def quantile1(self): 
#        """Gives the 1st quantile of the sample."""
#        raise DistributionFunctionError
#    def quantile3(self): 
#        """Gives the 3rd quantile of the sample."""
#        raise DistributionFunctionError
#    def qmean(self): 
#        """Gives the quantile of the arithmetic mean of the sample."""
#        raise DistributionFunctionError
#    def qmode(self): 
#        """Gives the quantile of the mode of the sample."""
#        raise DistributionFunctionError
#    def random(self):
#        """Gives a random number based on the distribution."""
#        raise DistributionFunctionError

class LogNormalDistribution(Distribution):
#    def __init__(self, **parameters): 
#        """Constructor method. The parameters are used to construct the 
#        probability distribution."""
#        raise DistributionFunctionError
#    def CDF(self, x): 
#        """
#        Cummulative Distribution Function, which gives the cummulative 
#        probability (area under the probability curve) from -infinity or 0 
#        to a give x-value on the x-axis where y-axis is the probability."""
#        raise DistributionFunctionError
#    def PDF(self, x): 
#        """
#        Partial Distribution Function, which gives the probability for the 
#        particular value of x, or the area under probability distribution 
#        from x-h to x+h for continuous distribution."""
#        raise DistributionFunctionError
    def inverseCDF(self, probability, start = 0.0, step = 0.01): 
        """
        It does the reverse of CDF() method, it takes a probability value and 
        returns the corresponding value on the x-axis."""
        cprob = self.CDF(start)
        if probability < cprob: return (start, cprob)
        while (probability > cprob):
            start = start + step
            cprob = self.CDF(start)
            # print start, cprob
        return (start, cprob)
#    def mean(self): 
#        """Gives the arithmetic mean of the sample."""
#        raise DistributionFunctionError
#    def mode(self): 
#        """Gives the mode of the sample."""
#        raise DistributionFunctionError
#    def kurtosis(self): 
#        """Gives the kurtosis of the sample."""
#        raise DistributionFunctionError
#    def skew(self): 
#        """Gives the skew of the sample."""
#        raise DistributionFunctionError
#    def variance(self): 
#        """Gives the variance of the sample."""
#        raise DistributionFunctionError
    def random(self):
        """Gives a random number based on the distribution."""
        return random.lognormalvariate(self.location, self.scale)


class NegativeBinomialDistribution(Distribution):
    def __init__(self, **parameters): 
        """Constructor method. The parameters are used to construct the 
        probability distribution."""
        try:
            self.success = parameters['success']
            self.target = parameters['target']
        except KeyError: 
            raise DistributionParameterError('Negative Binomial distribution \
            requires success and target parameters')
    def CDF(self, x): 
        """
        Cummulative Distribution Function, which gives the cummulative 
        probability (area under the probability curve) from -infinity or 0 to 
        a give x-value on the x-axis where y-axis is the probability."""
        sum = 0.0
        for i in range(x): sum = sum + self.PDF(i)
        return sum
    def PDF(self, x): 
        """
        Partial Distribution Function, which gives the probability for the 
        particular value of x, or the area under probability distribution from 
        x-h to x+h for continuous distribution."""
        return NRPy.bico(x - 1, self.target - 1) * \
                (self.success ** self.target) * \
                ((1 - self.success) ** (x - self.target))
    def inverseCDF(self, probability, start = 0, step = 1): 
        """
        It does the reverse of CDF() method, it takes a probability value and 
        returns the corresponding value on the x-axis."""
        cprob = self.CDF(start)
        if probability < cprob: return (start, cprob)
        while (probability > cprob):
            start = start + step
            cprob = self.CDF(start)
            # print start, cprob
        return (start, cprob)
    def mean(self): 
        """Gives the arithmetic mean of the sample."""
        return self.target / self.success
    def mode(self): 
        """Gives the mode of the sample."""
        return int((self.success + self.target - 1)/self.success)
#    def kurtosis(self): 
#        """Gives the kurtosis of the sample."""
#        raise DistributionFunctionError
#    def skew(self): 
#        """Gives the skew of the sample."""
#        raise DistributionFunctionError
#    def variance(self): 
#        """Gives the variance of the sample."""
#        raise DistributionFunctionError
#    def quantile1(self): 
#        """Gives the 1st quantile of the sample."""
#        raise DistributionFunctionError
#    def quantile3(self): 
#        """Gives the 3rd quantile of the sample."""
#        raise DistributionFunctionError
#    def qmean(self): 
#        """Gives the quantile of the arithmetic mean of the sample."""
#        raise DistributionFunctionError
#    def qmode(self): 
#        """Gives the quantile of the mode of the sample."""
#        raise DistributionFunctionError
#    def random(self):
#        """Gives a random number based on the distribution."""
#        raise DistributionFunctionError


class NormalDistribution(Distribution):
    def __init__(self, **kwargs):
        self.mean = 0.0
        self.stdev = 1.0
    def CDF(self, x):
        return 1.0 - 0.5 * NRPy.erfcc(x/SQRT2)
    def PDF(self, x): 
        """
        Calculates the density (probability) at x by the formula:
        f(x) = 1/(sqrt(2 pi) sigma) e^-((x - mu)^2/(2 sigma^2))
        where mu is the mean of the distribution and sigma the standard 
        deviation."""        
        return (1/(math.sqrt(PI2) * self.stdev)) * \
                math.exp(-((x - self.stdev)**2/(2 * self.stdev**2)))
    def inverseCDF(self, probability, start = -10.0, step = 0.01): 
        """
        It does the reverse of CDF() method, it takes a probability value and 
        returns the corresponding value on the x-axis."""
        cprob = self.CDF(start)
        if probability < cprob: return (start, cprob)
        while (probability > cprob):
            start = start + step
            cprob = self.CDF(start)
#            print start, cprob
        return (start, cprob)
    def mean(self): 
        return self.mean
    def mode(self):
        return self.mean
    def kurtosis(self): 
        return 0.0
    def skew(self): 
        return 0.0
    def variance(self): 
        return self.stdev * self.stdev
    def random(self):
        """Gives a random number based on the distribution."""
        return random.gauss(self.mean, self.stdev)
       

class ParetoDistribution(Distribution):
    pass
    def __init__(self, **parameters): 
        """Constructor method. The parameters are used to construct the 
        probability distribution."""
        try: self.location = parameters['location']
        except KeyError: self.location = 1.0
        try: self.shape = parameters['shape']
        except KeyError: self.shape = 1.0
    def CDF(self, x): 
        """
        Cummulative Distribution Function, which gives the cummulative 
        probability (area under the probability curve) from -infinity or 0 to 
        a give x-value on the x-axis where y-axis is the probability."""
        return 1 - (self.location/x) ** self.shape
    def PDF(self, x): 
        """
        Partial Distribution Function, which gives the probability for the 
        particular value of x, or the area under probability distribution from 
        x-h to x+h for continuous distribution."""
        return (self.shape * (self.location ** self.shape)) / \
                (x ** (self.shape + 1))
    def inverseCDF(self, probability, start = 0.0, step = 0.01): 
        """
        It does the reverse of CDF() method, it takes a probability value and 
        returns the corresponding value on the x-axis."""
        cprob = self.CDF(start)
        if probability < cprob: return (start, cprob)
        while (probability > cprob):
            start = start + step
            cprob = self.CDF(start)
            # print start, cprob
        return (start, cprob)
    def mean(self): 
        """Gives the arithmetic mean of the sample."""
        return (self.location * self.shape) / (self.shape - 1)
    def mode(self): 
        """Gives the mode of the sample."""
        return self.location
    def median(self): 
        """Gives the median of the sample."""
        return self.location * (2 ** (1/self.shape))
    def kurtosis(self): 
        """Gives the kurtosis of the sample."""
        n = 6 * (self.shape ** 3 + self.shape ** 2 + 6 * self.shape - 2)
        d = self.shape * (self.shape ** 2 - 7 * self.shape + 12)
        return n/d
    def skew(self): 
        """Gives the skew of the sample."""
        n = 2 * (self.shape + 1) * math.sqrt(self.shape - 2)
        d = (self.shape - 3) * math.sqrt(self.shape)
        return n/d
    def variance(self): 
        """Gives the variance of the sample."""
        n = (self.location ** 2) * self.shape
        d = (self.shape - 2) * ((self.shape - 1) ** 2)
        return n/d
    def quantile1(self): 
        """Gives the 1st quantile of the sample."""
        return self.location * (1.333 ** (1/self.shape))
    def quantile3(self): 
        """Gives the 3rd quantile of the sample."""
        return self.location * (4 ** (1/self.shape))
    def qmean(self): 
        """Gives the quantile of the arithmetic mean of the sample."""
        return 1 - (((self.shape - 1)/self.shape) ** self.shape)
    def qmode(self): 
        """Gives the quantile of the mode of the sample."""
        return 0.0
    def random(self):
        """Gives a random number based on the distribution."""
        return random.paretovariate(self.shape)   

    
class PoissonDistribution(Distribution):
    def __init__(self, **parameters): 
        """Constructor method. The parameters are used to construct the 
        probability distribution."""
        try: self.mean = parameters['expectation']
        except KeyError: 
            raise DistributionParameterError('Poisson distribution requires \
            expectation (lambda)')
    def CDF(self, x): 
        """
        Cummulative Distribution Function, which gives the cummulative 
        probability (area under the probability curve) from -infinity or 0 to 
        a give x-value on the x-axis where y-axis is the probability."""
        return NRPy.cdf_poisson(x, self.mean)
    def PDF(self, x): 
        """
        Partial Distribution Function, which gives the probability for the 
        particular value of x, or the area under probability distribution from 
        x-h to x+h for continuous distribution."""
        return (math.exp(-1 ** self.mean) * \
                (self.mean ** x)) / NRPy.factrl(x)
    def inverseCDF(self, probability, start = 0.0, step = 0.01): 
        """
        It does the reverse of CDF() method, it takes a probability value and 
        returns the corresponding value on the x-axis."""
        cprob = self.CDF(start)
        if probability < cprob: return (start, cprob)
        while (probability > cprob):
            start = start + step
            cprob = self.CDF(start)
            # print start, cprob
        return (start, cprob)
    def mean(self): 
        """Gives the arithmetic mean of the sample."""
        return self.mean
    def mode(self): 
        """Gives the mode of the sample."""
        return int(self.mean)
#    def kurtosis(self): 
#        """Gives the kurtosis of the sample."""
#        raise DistributionFunctionError
#    def skew(self): 
#        """Gives the skew of the sample."""
#        raise DistributionFunctionError
    def variance(self): 
        """Gives the variance of the sample."""
        return self.mean
#    def random(self):
#        """Gives a random number based on the distribution."""
#        raise DistributionFunctionError    


class RademacherDistribution(Distribution):
    def __init__(self, **parameters): 
        """Constructor method. The parameters are used to construct the 
            probability distribution."""
        pass
    def CDF(self, x): 
        """
        Cummulative Distribution Function, which gives the cummulative 
        probability (area under the probability curve) from -infinity or 0 to 
        a give x-value on the x-axis where y-axis is the probability."""
        if x < -1: return 0.0
        elif x > -1 and x < 1: return 0.5
        else: return 1.0
    def PDF(self, x): 
        """
        Partial Distribution Function, which gives the probability for the 
        particular value of x, or the area under probability distribution 
        from x-h to x+h for continuous distribution."""
        if x == -1 or x == 1: return 0.5
        else: return 0.0
    def inverseCDF(self, probability, start = 0.0, step = 0.01): 
        """
        It does the reverse of CDF() method, it takes a probability value 
        and returns the corresponding value on the x-axis."""
        if probability == 0.0: return (-1.0001, 0.0)
        if probability == 1.0: return (1.0, 1.0)
        else: return (0.999, 0.5)
    def mean(self): 
        """Gives the arithmetic mean of the sample."""
        return 0
#    def mode(self): 
#        """Gives the mode of the sample."""
#        raise DistributionFunctionError
#    def kurtosis(self): 
#        """Gives the kurtosis of the sample."""
#        raise DistributionFunctionError
    def skew(self): 
        """Gives the skew of the sample."""
        return 0
    def variance(self): 
        """Gives the variance of the sample."""
        return 1
#    def quantile1(self): 
#        """Gives the 1st quantile of the sample."""
#        raise DistributionFunctionError
#    def quantile3(self): 
#        """Gives the 3rd quantile of the sample."""
#        raise DistributionFunctionError
#    def qmean(self): 
#        """Gives the quantile of the arithmetic mean of the sample."""
#        raise DistributionFunctionError
#    def qmode(self): 
#        """Gives the quantile of the mode of the sample."""
#        raise DistributionFunctionError
#    def random(self):
#        """Gives a random number based on the distribution."""
#        raise DistributionFunctionError

class SemicircularDistribution(Distribution):
    def __init__(self, **parameters): 
        """Constructor method. The parameters are used to construct the 
        probability distribution."""
        try:
            self.scale = parameters['scale']
            self.location = parameters['location']
        except KeyError: 
            raise DistributionParameterError('Semicircular distribution \
            requires location and scale parameters')
    def CDF(self, x): 
        """
        Cummulative Distribution Function, which gives the cummulative 
        probability (area under the probability curve) from -infinity or 0 to 
        a give x-value on the x-axis where y-axis is the probability."""
        t = ((x - self.location)/self.scale)**2
        return 0.5 + (1/PI) * (t * math.srqt(1 - (t ** 2)) + math.asin(t))
    def PDF(self, x): 
        """
        Partial Distribution Function, which gives the probability for the 
        particular value of x, or the area under probability distribution from 
        x-h to x+h for continuous distribution."""
        return (2/(self.scale * PI)) * \
                math.sqrt(1 - ((x - self.location)/self.scale)**2)
    def inverseCDF(self, probability, start = 0.0, step = 0.01): 
        """
        It does the reverse of CDF() method, it takes a probability value and 
        returns the corresponding value on the x-axis."""
        cprob = self.CDF(start)
        if probability < cprob: return (start, cprob)
        while (probability > cprob):
            start = start + step
            cprob = self.CDF(start)
            # print start, cprob
        return (start, cprob)
    def mean(self): 
        """Gives the arithmetic mean of the sample."""
        return self.location
    def mode(self): 
        """Gives the mode of the sample."""
        return self.location
    def kurtosis(self): 
        """Gives the kurtosis of the sample."""
        return -1.0
    def skew(self): 
        """Gives the skew of the sample."""
        return 0.0
    def variance(self): 
        """Gives the variance of the sample."""
        return 0.25 * (self.scale ** 2)
    def quantile1(self): 
        """Gives the 1st quantile of the sample."""
        return self.location - (0.404 * self.scale)
    def quantile3(self): 
        """Gives the 3rd quantile of the sample."""
        return self.location + (0.404 * self.scale)
    def qmean(self): 
        """Gives the quantile of the arithmetic mean of the sample."""
        return 0.5
    def qmode(self): 
        """Gives the quantile of the mode of the sample."""
        return 0.5
#    def random(self):
#        """Gives a random number based on the distribution."""
#        raise DistributionFunctionError
        
class TDistribution(Distribution):
    def __init__(self, **parameters): 
        """Constructor method. The parameters are used to construct the 
        probability distribution."""
        try: self.mean = parameter['location']
        except KeyError: self.mean = 0.0
        try: self.stdev = parameter['scale']
        except KeyError: self.stdev = 1.0
        try: self.df = parameter['shape']
        except KeyError: self.df = 2
#    def CDF(self, x): 
#        """
#       """
#        raise DistributionFunctionError
#    def PDF(self, x): 
#        """
#        Calculates the density (probability) at x with n-th degrees of freedom as:
#        f(x) = Gamma((n+1)/2) / (sqrt(n pi) Gamma(n/2)) (1 + x^2/n)^-((n+1)/2)
#        for all real x. It has mean 0 (for n > 1) and variance n/(n-2) (for n > 2)."""
#        raise DistributionFunctionError
    def inverseCDF(self, probability, start = 0.0, step = 0.01): 
        """
        It does the reverse of CDF() method, it takes a probability value and 
        returns the corresponding value on the x-axis."""
        cprob = self.CDF(start)
        if probability < cprob: return (start, cprob)
        while (probability > cprob):
            start = start + step
            cprob = self.CDF(start)
            # print start, cprob
        return (start, cprob)
    def mean(self): 
        """Gives the arithmetic mean of the sample."""
        return self.mean
#    def mode(self): 
#        """Gives the mode of the sample."""
#        raise DistributionFunctionError
#    def kurtosis(self): 
#        """Gives the kurtosis of the sample."""
#        raise DistributionFunctionError
    def skew(self): 
        """Gives the skew of the sample."""
        return 0.0
    def variance(self): 
        """Gives the variance of the sample."""
        return (self.df / (self.df - 2)) * self.stdev * self.stdev
#    def random(self):
#        """Gives a random number based on the distribution."""
#        raise DistributionFunctionError


class UniformDistribution(Distribution):
    def __init__(self, **parameters): 
        """Constructor method. The parameters are used to construct the 
        probability distribution."""
        try: 
            self.location = parameters['location']
            self.scale = parameters['scale']
        except KeyError: 
            raise DistributionParameterError('Uniform distribution requires \
            location and scale parameters')
    def CDF(self, x): 
        """
        Cummulative Distribution Function, which gives the cummulative 
        probability (area under the probability curve) from -infinity or 0 to 
        a give x-value on the x-axis where y-axis is the probability."""
        return (x - self.location)/(self.scale - self.location)
    def PDF(self, x): 
        """
        Partial Distribution Function, which gives the probability for the 
        particular value of x, or the area under probability distribution from 
        x-h to x+h for continuous distribution."""
        return 1/(self.scale - self.location)
    def inverseCDF(self, probability, start = 0.0, step = 0.01): 
        """
        It does the reverse of CDF() method, it takes a probability value and 
        returns the corresponding value on the x-axis."""
        cprob = self.CDF(start)
        if probability < cprob: return (start, cprob)
        while (probability > cprob):
            start = start + step
            cprob = self.CDF(start)
            # print start, cprob
        return (start, cprob)
    def mean(self): 
        """Gives the arithmetic mean of the sample."""
        return (self.location + self.scale)/2
    def median(self): 
        """Gives the median of the sample."""
        return (self.location + self.scale)/2
    def kurtosis(self): 
        """Gives the kurtosis of the sample."""
        return -1.2
    def skew(self): 
        """Gives the skew of the sample."""
        return 0.0
    def variance(self): 
        """Gives the variance of the sample."""
        return ((self.scale - self.location) ** 2)/12
    def quantile1(self): 
        """Gives the 1st quantile of the sample."""
        return ((3 * self.location) + self.scale)/4
    def quantile3(self): 
        """Gives the 3rd quantile of the sample."""
        return (self.location + (3 * self.scale))/4
    def qmean(self): 
        """Gives the quantile of the arithmetic mean of the sample."""
        return 0.5
#    def qmode(self): 
#        """Gives the quantile of the mode of the sample."""
#        raise DistributionFunctionError
    def random(self, lower, upper):
        """Gives a random number based on the distribution."""
        return random.uniform(lower, upper)

    
class WeiBullDistribution(Distribution):
#    def __init__(self, **parameters): 
#        """Constructor method. The parameters are used to construct the 
#        probability distribution."""
#        raise DistributionFunctionError
#    def CDF(self, x): 
#        """
#        Cummulative Distribution Function, which gives the cummulative 
#        probability (area under the  probability curve) from -infinity or 0 
#        to a give x-value on the x-axis where y-axis is the probability."""
#        raise DistributionFunctionError
#    def PDF(self, x): 
#        """
#        Partial Distribution Function, which gives the probability for the 
#        particular value of x, or the area under probability distribution 
#        from x-h to x+h for continuous distribution."""
#        raise DistributionFunctionError
    def inverseCDF(self, probability, start = 0.0, step = 0.01): 
        """
        It does the reverse of CDF() method, it takes a probability value and 
        returns the corresponding value on the x-axis."""
        cprob = self.CDF(start)
        if probability < cprob: return (start, cprob)
        while (probability > cprob):
            start = start + step
            cprob = self.CDF(start)
            # print start, cprob
        return (start, cprob)
#    def mean(self): 
#        """Gives the arithmetic mean of the sample."""
#        raise DistributionFunctionError
#    def mode(self): 
#        """Gives the mode of the sample."""
#        raise DistributionFunctionError
#    def kurtosis(self): 
#        """Gives the kurtosis of the sample."""
#        raise DistributionFunctionError
#    def skew(self): 
#        """Gives the skew of the sample."""
#        raise DistributionFunctionError
#    def variance(self): 
#        """Gives the variance of the sample."""
#        raise DistributionFunctionError
    def random(self):
        """Gives a random number based on the distribution."""
        return random.weibullvariate(self.scale, self.shape)


# -------------------------------------------------------------------
# Special case distributions
# -------------------------------------------------------------------

class BernoulliDistribution(Distribution):
    def __init__(self, **parameters): 
        """Constructor method. The parameters are used to construct the 
        probability distribution."""
        try: self.distribution = BinomialDistribution(parameters['success'], 
                                                        1)
        except KeyError: 
            raise DistributionParameterError('Bernoulli distribution \
            requires success parameter')
    def CDF(self, x): 
        """
        Cummulative Distribution Function, which gives the cummulative 
        probability (area under the probability curve) from -infinity or 0 to 
        a give x-value on the x-axis where y-axis is the probability."""
        return self.distribution.CDF(x)
    def PDF(self, x): 
        """
        Partial Distribution Function, which gives the probability for the 
        particular value of x, or the area under probability distribution from 
        x-h to x+h for continuous distribution."""
        return self.distribution.PDF(x)
    def inverseCDF(self, probability, start = 0, step = 1): 
        """
        It does the reverse of CDF() method, it takes a probability value and 
        returns the corresponding value on the x-axis."""
        return self.distribution.inverseCDF(probability, start, step)
    def mean(self): 
        """Gives the arithmetic mean of the sample."""
        return self.distribution.mean()
    def mode(self): 
        """Gives the mode of the sample."""
        return self.distribution.mode()
    def kurtosis(self): 
        """Gives the kurtosis of the sample."""
        return self.distribution.kurtosis()
    def skew(self): 
        """Gives the skew of the sample."""
        return self.distribution.skew()
    def variance(self): 
        """Gives the variance of the sample."""
        return self.distribution.variance()
#    def random(self):
#        """Gives a random number based on the distribution."""
#        return self.distribution.random()


class HalfNormalDistribution(Distribution):
    def __init__(self, **parameters): 
        """Constructor method. The parameters are used to construct the 
        probability distribution."""
        try: self.distribution = ChiDistribution(parameters['location'],
                                                 parameters['scale'],
                                                 1)
        except KeyError: 
            raise DistributionParameterError('Halfnormal distribution \
            requires location and scale parameters')
    def CDF(self, x): 
        """
        Cummulative Distribution Function, which gives the cummulative 
        probability (area under the probability curve) from -infinity or 0 to 
        a give x-value on the x-axis where y-axis is the probability."""
        return self.distribution.CDF(x)
    def PDF(self, x): 
        """
        Partial Distribution Function, which gives the probability for the 
        particular value of x, or the area under probability distribution from 
        x-h to x+h for continuous distribution."""
        return self.distribution.PDF(x)
    def inverseCDF(self, probability, start = 0.0, step =0.01): 
        """
        It does the reverse of CDF() method, it takes a probability value and 
        returns the corresponding value on the x-axis."""
        return self.distribution.inverseCDF(probability, start, step)
    def mean(self): 
        """Gives the arithmetic mean of the sample."""
        return self.distribution.mean()
    def mode(self): 
        """Gives the mode of the sample."""
        return self.distribution.mode()
    def kurtosis(self): 
        """Gives the kurtosis of the sample."""
        return self.distribution.kurtosis()
    def skew(self): 
        """Gives the skew of the sample."""
        return self.distribution.skew()
    def variance(self): 
        """Gives the variance of the sample."""
        return self.distribution.variance()
#    def random(self):
#        """Gives a random number based on the distribution."""
#        return self.distribution.random()


class MaxwellDistribution(Distribution):
    def __init__(self, **parameters): 
        """Constructor method. The parameters are used to construct the 
        probability distribution."""
        try: self.distribution = ChiDistribution(0, parameters['scale'], 3)
        except KeyError: 
            raise DistributionParameterError('Maxwell distribution requires \
            scale parameter')
    def CDF(self, x): 
        """
        Cummulative Distribution Function, which gives the cummulative 
        probability (area under the probability curve) from -infinity or 0 to 
        a give x-value on the x-axis where y-axis is the probability."""
        return self.distribution.CDF(x)
    def PDF(self, x): 
        """
        Partial Distribution Function, which gives the probability for the 
        particular value of x, or the area under probability distribution from 
        x-h to x+h for continuous distribution."""
        return self.distribution.PDF(x)
    def inverseCDF(self, probability, start = 0.0, step = 0.01): 
        """
        It does the reverse of CDF() method, it takes a probability value and
        the corresponding value on the x-axis."""
        return self.distribution.inverseCDF(probability, start, step)
    def mean(self): 
        """Gives the arithmetic mean of the sample."""
        return self.distribution.mean()
    def mode(self): 
        """Gives the mode of the sample."""
        return self.distribution.mode()
    def kurtosis(self): 
        """Gives the kurtosis of the sample."""
        return self.distribution.kurtosis()
    def skew(self): 
        """Gives the skew of the sample."""
        return self.distribution.skew()
    def variance(self): 
        """Gives the variance of the sample."""
        return self.distribution.variance()
#    def random(self):
#        """Gives a random number based on the distribution."""
#        return self.distribution.random()


class PascalDistribution(Distribution):
    def __init__(self, **parameters): 
        """Constructor method. The parameters are used to construct the 
        probability distribution."""
        try: self.distribution = NegativeBinomialDistribution(
                                    parameters['success'],
                                    int(parameters['target']))
        except KeyError: 
            raise DistributionParameterError('Pascal distribution requires \
            success and target parameters')
    def CDF(self, x): 
        """
        Cummulative Distribution Function, which gives the cummulative 
        probability (area under the probability curve) from -infinity or 0 to 
        a give x-value on the x-axis where y-axis is the probability."""
        return self.distribution.CDF(x)
    def PDF(self, x): 
        """
        Partial Distribution Function, which gives the probability for the 
        particular value of x, or the area under probability distribution from 
        x-h to x+h for continuous distribution."""
        return self.distribution.PDF(x)
    def inverseCDF(self, probability, start = 0.0, step =0.01): 
        """
        It does the reverse of CDF() method, it takes a probability value and 
        returns the corresponding value on the x-axis."""
        return self.distribution.inverseCDF(probability, start, step)
    def mean(self): 
        """Gives the arithmetic mean of the sample."""
        return self.distribution.mean()
    def mode(self): 
        """Gives the mode of the sample."""
        return self.distribution.mode()
    def kurtosis(self): 
        """Gives the kurtosis of the sample."""
        return self.distribution.kurtosis()
    def skew(self): 
        """Gives the skew of the sample."""
        return self.distribution.skew()
    def variance(self): 
        """Gives the variance of the sample."""
        return self.distribution.variance()
#    def random(self):
#        """Gives a random number based on the distribution."""
#        return self.distribution.random()

class PowerFunctionDistribution(Distribution):
    def __init__(self, **parameters): 
        """Constructor method. The parameters are used to construct the 
        probability distribution."""
        try: self.distribution = BetaDistribution(0, 1, parameters['shape'], 
                                                    1)
        except KeyError: 
            raise DistributionParameterError('Power Function distribution \
            require shape parameter')
    def CDF(self, x): 
        """
        Cummulative Distribution Function, which gives the cummulative 
        probability (area under the probability curve) from -infinity or 0 to 
        a give x-value on the x-axis where y-axis is the probability."""
        return self.distribution.CDF(x)
    def PDF(self, x): 
        """
        Partial Distribution Function, which gives the probability for the 
        particular value of x, or the area under probability distribution from 
        x-h to x+h for continuous distribution."""
        return self.distribution.PDF(x)
    def inverseCDF(self, probability, start = 0.0, step =0.01): 
        """
        It does the reverse of CDF() method, it takes a probability value and 
        returns the corresponding value on the x-axis."""
        return self.distribution.inverseCDF(probability, start, step)
    def mean(self): 
        """Gives the arithmetic mean of the sample."""
        return self.distribution.mean()
    def mode(self): 
        """Gives the mode of the sample."""
        return self.distribution.mode()
    def kurtosis(self): 
        """Gives the kurtosis of the sample."""
        return self.distribution.kurtosis()
    def skew(self): 
        """Gives the skew of the sample."""
        return self.distribution.skew()
    def variance(self): 
        """Gives the variance of the sample."""
        return self.distribution.variance()
#    def random(self):
#        """Gives a random number based on the distribution."""
#        return self.distribution.random()


class RayleighDistribution(Distribution):
    def __init__(self, **parameters): 
        """Constructor method. The parameters are used to construct the 
        probability distribution."""
        try: self.distribution = ChiDistribution(0, parameters['scale'], 2)
        except KeyError: 
            raise DistributionParameterError('Rayleigh distribution requires \
            scale parameter')
    def CDF(self, x): 
        """
        Cummulative Distribution Function, which gives the cummulative 
        probability (area under the probability curve) from -infinity or 0 to 
        a give x-value on the x-axis where y-axis is the probability."""
        return self.distribution.CDF(x)
    def PDF(self, x): 
        """
        Partial Distribution Function, which gives the probability for the 
        particular value of x, or the area under probability distribution from 
        x-h to x+h for continuous distribution."""
        return self.distribution.PDF(x)
    def inverseCDF(self, probability, start = 0.0, step =0.01): 
        """
        It does the reverse of CDF() method, it takes a probability value and 
        returns the corresponding value on the x-axis."""
        return self.distribution.inverseCDF(probability, start, step)
    def mean(self): 
        """Gives the arithmetic mean of the sample."""
        return self.distribution.mean()
    def mode(self): 
        """Gives the mode of the sample."""
        return self.distribution.mode()
    def kurtosis(self): 
        """Gives the kurtosis of the sample."""
        return self.distribution.kurtosis()
    def skew(self): 
        """Gives the skew of the sample."""
        return self.distribution.skew()
    def variance(self): 
        """Gives the variance of the sample."""
        return self.distribution.variance()
#    def random(self):
#        """Gives a random number based on the distribution."""
#        return self.distribution.random()
    


# -------------------------------------------------------------------
# Distribution alias
# -------------------------------------------------------------------

def AntiLogNormalDistribution(**parameters):
    """
    Anti-Lognormal distribution is an alias of Lognormal distribution."""
    return LogNormalDistribution(**parameters)

def CobbDouglasDistribution(**parameters):
    """
    Cobb-Douglas distribution is an alias of Lognormal distribution."""
    return LogNormalDistribution(**parameters)

def ErlangDistribution(**parameters):
    """
    Erlang distribution is an alias of Gamma distribution where the shape
    parameter is an integer."""
    try: parameters['shape'] = int(parameters['shape'])
    except KeyError: 
            raise DistributionParameterError('Erlang distribution requires \
            shape parameter')
    return GammaDistribution(**parameters)

def FisherTippettDistribution(**parameters):
    """
    Fisher-Tippett distribution is an alias of Gumbel distribution."""
    return GumbelDistribution(**parameters)

def FurryDistribution(**parameters):
    """
    Furry distribution is an alias of Gamma distribution."""
    return GammaDistribution(**parameters)

def GompertzDistribution(**parameters):
    """
    Gompertz distribution is an alias of Gumbel distribution."""
    return GumbelDistribution(**parameters)

def LogWeibullDistribution(**parameters):
    """
    Log-Weibull distribution is an alias of Gumbel distribution."""
    return GumbelDistribution(**parameters)

def LorentzDistribution(**parameters):
    """
    Lorentz distribution is an alias of Cauchy distribution."""
    return CauchyDistribution(**parameters)

def NegativeExponentialDistribution(**parameters):
    """
    Negative-exponential distribution is an alias of Exponential distribution."""
    return ExponentialDistribution(**parameters)

def PolyaDistribution(**parameters):
    """
    Polya distribution is an alias of Negative-binomial distribution."""
    return NegativeBinomialDistribution(**parameters)

def RectangularDistribution(**parameters):
    """
    Rectangular distribution is an alias of Uniform distribution."""
    return UniformDistribution(**parameters)
        
#class DummyDistribution(Distribution):
#    def __init__(self, **parameters): 
#        """Constructor method. The parameters are used to construct the 
#            probability distribution."""
#        raise DistributionFunctionError
#    def CDF(self, x): 
#       """
#        Cummulative Distribution Function, which gives the cummulative 
#        probability (area under the probability curve) from -infinity or 0 to 
#        a give x-value on the x-axis where y-axis is the probability."""
#        raise DistributionFunctionError
#    def PDF(self, x): 
#        """
#        Partial Distribution Function, which gives the probability for the 
#        particular value of x, or the area under probability distribution 
#        from x-h to x+h for continuous distribution."""
#        raise DistributionFunctionError
#    def inverseCDF(self, probability, start = 0.0, step = 0.01): 
#        """
#        It does the reverse of CDF() method, it takes a probability value 
#        and returns the corresponding value on the x-axis."""
#        cprob = self.CDF(start)
#        if probability < cprob: return (start, cprob)
#        while (probability > cprob):
#            start = start + step
#            cprob = self.CDF(start)
#            # print start, cprob
#        return (start, cprob)
#    def mean(self): 
#        """Gives the arithmetic mean of the sample."""
#        raise DistributionFunctionError
#    def mode(self): 
#        """Gives the mode of the sample."""
#        raise DistributionFunctionError
#    def kurtosis(self): 
#        """Gives the kurtosis of the sample."""
#        raise DistributionFunctionError
#    def skew(self): 
#        """Gives the skew of the sample."""
#        raise DistributionFunctionError
#    def variance(self): 
#        """Gives the variance of the sample."""
#        raise DistributionFunctionError
#    def quantile1(self): 
#        """Gives the 1st quantile of the sample."""
#        raise DistributionFunctionError
#    def quantile3(self): 
#        """Gives the 3rd quantile of the sample."""
#        raise DistributionFunctionError
#    def qmean(self): 
#        """Gives the quantile of the arithmetic mean of the sample."""
#        raise DistributionFunctionError
#    def qmode(self): 
#        """Gives the quantile of the mode of the sample."""
#        raise DistributionFunctionError
#    def random(self):
#        """Gives a random number based on the distribution."""
#        raise DistributionFunctionError
        