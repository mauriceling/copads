"""
File containing the functions for various statistical distributions.

Copyright (c) Maurice H.T. Ling <mauriceling@acm.org>
Date created: 17th August 2005
"""

import math
from CopadsExceptions import DistributionParameterError
import NRPy
from Constants import *

class Distribution:
    """
    Abstract class for all statistical distributions.
    Due to the large variations of parameters for each distribution, it is unlikely to be able to 
    standardize a parameter list for each method that is meaningful for all distributions. Instead, the 
    parameters to construct each distribution is to be given as keyword arguments.
    """
    def __init__(self, **parameters): 
        """Constructor method. The parameters are used to construct the probability distribution."""
        raise NotImplementedError
    def CDF(self, x): 
        """
        Cummulative Distribution Function, which gives the cummulative probability (area under the 
        probability curve) from -infinity or 0 to a give x-value on the x-axis where y-axis is the 
        probability. CDF is also known as density function."""
        raise NotImplementedError
    def PDF(self, x): 
        """
        Partial Distribution Function, which gives the probability for the particular value of x, or
        the area under probability distribution from x-h to x+h for continuous distribution."""
        raise NotImplementedError
    def inverseCDF(self, probability): 
        """
        It does the reverse of CDF() method, it takes a probability value and returns the corresponding 
        value on the x-axis."""
        raise NotImplementedError
    def mean(self): 
        """Gives the arithmetic mean of the sample."""
        raise NotImplementedError
    def moments(self, r): 
        """Gives the r-th moments of the sample."""
        raise NotImplementedError
    def kurtosis(self): 
        """Gives the kurtosis of the sample."""
        raise NotImplementedError
    def skew(self): 
        """Gives the skew of the sample."""
        raise NotImplementedError
    def variance(self): 
        """Gives the variance of the sample."""
        raise NotImplementedError
    def random(self):
        """Gives a random number based on the distribution."""
        raise NotImplementedError
        

class NormalDistribution(Distribution):
    def __init__(self, **parameters):
        try: self.mean = parameters['location']
        except KeyError:
            self.mean = 0.0
            self.stdev = 1.0
        try: self.stdev = parameters['scale']
        except KeyError:
            self.mean = 0.0
            self.variance = 1.0
    def CDF(self, x):
        return 1.0 - 0.5 * NRPy.erfcc(x/SQRT2)
    def PDF(self, x): 
        """
        Calculates the density (probability) at x by the formula:
        f(x) = 1/(sqrt(2 pi) sigma) e^-((x - mu)^2/(2 sigma^2))
        where mu is the mean of the distribution and sigma the standard deviation."""
        
        return (1/(math.sqrt(PI2) * self.stdev)) * \
                math.exp(-((x - self.stdev)**2/(2 * self.stdev**2)))
    def inverseCDF(self, probability):
        c0 = 2.515517
        c1 = 0.802853
        c2 = 0.010328
        d1 = 1.432788
        d2 = 0.189269
        d3 = 0.001308
        sign = -1.0
        if (p > 0.5):
            sign = 1.0
            p = 1.0 - p
        arg = -2.0 * math.log(p)
        t = math.sqrt(arg)
        g = t - (c0 + t*(c1 + t*c2)) / (1.0 + t*(d1 + t*(d2 + t*d3)))
        return sign*g
    def mean(self): 
        return self.mean
#    def moments(self, r): raise NotImplementedError
    def kurtosis(self): 
        return 0.0
    def skew(self): 
        return 0.0
    def variance(self): 
        return self.stdev * self.stdev
#    def random(self):
#        """Gives a random number based on the distribution."""
#        raise NotImplementedError
    
class ChiSquareDistribution(Distribution):
    pass
#    def __init__(self, **parameters): 
#        """Constructor method. The parameters are used to construct the probability distribution."""
#        raise NotImplementedError
#    def CDF(self, x): 
#        """
#        Cummulative Distribution Function, which gives the cummulative probability (area under the 
#        probability curve) from -infinity or 0 to a give x-value on the x-axis where y-axis is the 
#        probability."""
#        raise NotImplementedError
#    def PDF(self, x): 
#        """
#        Partial Distribution Function, which gives the probability for the particular value of x, or
#        the area under probability distribution from x-h to x+h for continuous distribution."""
#        raise NotImplementedError
#    def inverseCDF(self, probability): 
#        """
#        It does the reverse of CDF() method, it takes a probability value and returns the corresponding 
#        value on the x-axis."""
#        raise NotImplementedError
#    def mean(self): 
#        """Gives the arithmetic mean of the sample."""
#        raise NotImplementedError
#    def moments(self, r): 
#        """Gives the moments of the sample."""
#        raise NotImplementedError
#    def kurtosis(self): 
#        """Gives the kurtosis of the sample."""
#        raise NotImplementedError
#    def skew(self): 
#        """Gives the skew of the sample."""
#        raise NotImplementedError
#    def variance(self): 
#        """Gives the variance of the sample."""
#        raise NotImplementedError
#    def random(self):
#        """Gives a random number based on the distribution."""
#        raise NotImplementedError
    
class TDistribution(Distribution):
    def __init__(self, **parameters): 
        """Constructor method. The parameters are used to construct the probability distribution."""
        try: self.mean = parameter['location']
        except KeyError: self.mean = 0.0
        try: self.stdev = parameter['scale']
        except KeyError: self.stdev = 1.0
        try: self.df = parameter['shape']
        except KeyError: self.df = 2
#    def CDF(self, x): 
#        """
#       """
#        raise NotImplementedError
#    def PDF(self, x): 
#        """
#        Calculates the density (probability) at x with n-th degrees of freedom as:
#        f(x) = Gamma((n+1)/2) / (sqrt(n pi) Gamma(n/2)) (1 + x^2/n)^-((n+1)/2)
#        for all real x. It has mean 0 (for n > 1) and variance n/(n-2) (for n > 2)."""
#        raise NotImplementedError
#    def inverseCDF(self, probability): 
#        """
#        It does the reverse of CDF() method, it takes a probability value and returns the corresponding 
#        value on the x-axis."""
#        raise NotImplementedError
    def mean(self): 
        """Gives the arithmetic mean of the sample."""
        return self.mean
#    def moments(self, r): 
#        """Gives the moments of the sample."""
#        raise NotImplementedError
#    def kurtosis(self): 
#        """Gives the kurtosis of the sample."""
#        raise NotImplementedError
    def skew(self): 
        """Gives the skew of the sample."""
        return 0.0
    def variance(self): 
        """Gives the variance of the sample."""
        return (self.df / (self.df - 2)) * self.stdev * self.stdev
#    def random(self):
#        """Gives a random number based on the distribution."""
#        raise NotImplementedError
 
class FDistribution(Distribution):
    pass
#    def __init__(self, **parameters): 
#        """Constructor method. The parameters are used to construct the probability distribution."""
#        raise NotImplementedError
#    def CDF(self, x): 
#        """
#        Cummulative Distribution Function, which gives the cummulative probability (area under the 
#        probability curve) from -infinity or 0 to a give x-value on the x-axis where y-axis is the 
#        probability."""
#        raise NotImplementedError
#    def PDF(self, x): 
#        """
#        Partial Distribution Function, which gives the probability for the particular value of x, or
#        the area under probability distribution from x-h to x+h for continuous distribution."""
#        raise NotImplementedError
#    def inverseCDF(self, probability): 
#        """
#        It does the reverse of CDF() method, it takes a probability value and returns the corresponding 
#        value on the x-axis."""
#        raise NotImplementedError
#    def mean(self): 
#        """Gives the arithmetic mean of the sample."""
#        raise NotImplementedError
#    def moments(self, r): 
#        """Gives the moments of the sample."""
#        raise NotImplementedError
#    def kurtosis(self): 
#        """Gives the kurtosis of the sample."""
#        raise NotImplementedError
#    def skew(self): 
#        """Gives the skew of the sample."""
#        raise NotImplementedError
#    def variance(self): 
#        """Gives the variance of the sample."""
#        raise NotImplementedError
#    def random(self):
#        """Gives a random number based on the distribution."""
#        raise NotImplementedError
       
class BinomialDistribution(Distribution):
    def __init__(self, **parameters): 
        """Constructor method. The parameters are used to construct the probability distribution."""
        try: self.success = parameter['success']
        except KeyError: self.success = 0.5
        try: self.trial = parameter['trial']
        except KeyError: self.trial = 1000
#    def CDF(self, x): 
#        """
#        Cummulative Distribution Function, which gives the cummulative probability (area under the 
#        probability curve) from -infinity or 0 to a give x-value on the x-axis where y-axis is the 
#        probability."""
#        raise NotImplementedError
#    def PDF(self, x): 
#        """
#        Partial Distribution Function, which gives the probability for the particular value of x, or
#        the area under probability distribution from x-h to x+h for continuous distribution."""
#        raise NotImplementedError
#    def inverseCDF(self, probability): 
#        """
#        It does the reverse of CDF() method, it takes a probability value and returns the corresponding 
#        value on the x-axis."""
#        raise NotImplementedError
    def mean(self): 
        """Gives the arithmetic mean of the sample."""
        return self.success * self.trial
#    def moments(self, r): 
#        """Gives the moments of the sample."""
#        raise NotImplementedError
#    def kurtosis(self): 
#        """Gives the kurtosis of the sample."""
#        raise NotImplementedError
#    def skew(self): 
#        """Gives the skew of the sample."""
#        raise NotImplementedError
    def variance(self): 
        """Gives the variance of the sample."""
        return self.mean() * (1 - self.success)
#    def random(self):
#        """Gives a random number based on the distribution."""
#        raise NotImplementedError
    
class PoissonDistribution(Distribution):
    def __init__(self, **parameters): 
        """Constructor method. The parameters are used to construct the probability distribution."""
        self.mean = parameters['expectation']
#    def CDF(self, x): 
#        """
#        Cummulative Distribution Function, which gives the cummulative probability (area under the 
#        probability curve) from -infinity or 0 to a give x-value on the x-axis where y-axis is the 
#        probability."""
#        raise NotImplementedError
#    def PDF(self, x): 
#        """
#        Partial Distribution Function, which gives the probability for the particular value of x, or
#        the area under probability distribution from x-h to x+h for continuous distribution."""
#        raise NotImplementedError
#    def inverseCDF(self, probability): 
#        """
#        It does the reverse of CDF() method, it takes a probability value and returns the corresponding 
#        value on the x-axis."""
#        raise NotImplementedError
    def mean(self): 
        """Gives the arithmetic mean of the sample."""
        return self.mean
#    def moments(self, r): 
#        """Gives the moments of the sample."""
#        raise NotImplementedError
#    def kurtosis(self): 
#        """Gives the kurtosis of the sample."""
#        raise NotImplementedError
#    def skew(self): 
#        """Gives the skew of the sample."""
#        raise NotImplementedError
    def variance(self): 
        """Gives the variance of the sample."""
        return self.mean
#    def random(self):
#        """Gives a random number based on the distribution."""
#        raise NotImplementedError
    
class GeometricDistribution(Distribution):
    pass
#    def __init__(self, **parameters): 
#        """Constructor method. The parameters are used to construct the probability distribution."""
#        raise NotImplementedError
#    def CDF(self, x): 
#        """
#        Cummulative Distribution Function, which gives the cummulative probability (area under the 
#        probability curve) from -infinity or 0 to a give x-value on the x-axis where y-axis is the 
#        probability."""
#        raise NotImplementedError
#    def PDF(self, x): 
#        """
#        Partial Distribution Function, which gives the probability for the particular value of x, or
#        the area under probability distribution from x-h to x+h for continuous distribution."""
#        raise NotImplementedError
#    def inverseCDF(self, probability): 
#        """
#        It does the reverse of CDF() method, it takes a probability value and returns the corresponding 
#        value on the x-axis."""
#        raise NotImplementedError
#    def mean(self): 
#        """Gives the arithmetic mean of the sample."""
#        raise NotImplementedError
#    def moments(self, r): 
#        """Gives the moments of the sample."""
#        raise NotImplementedError
#    def kurtosis(self): 
#        """Gives the kurtosis of the sample."""
#        raise NotImplementedError
#    def skew(self): 
#        """Gives the skew of the sample."""
#        raise NotImplementedError
#    def variance(self): 
#        """Gives the variance of the sample."""
#        raise NotImplementedError
#    def random(self):
#        """Gives a random number based on the distribution."""
#        raise NotImplementedError
    
class LogNormalDistribution(Distribution):
    pass
#    def __init__(self, **parameters): 
#        """Constructor method. The parameters are used to construct the probability distribution."""
#        raise NotImplementedError
#    def CDF(self, x): 
#        """
#        Cummulative Distribution Function, which gives the cummulative probability (area under the 
#        probability curve) from -infinity or 0 to a give x-value on the x-axis where y-axis is the 
#        probability."""
#        raise NotImplementedError
#    def PDF(self, x): 
#        """
#        Partial Distribution Function, which gives the probability for the particular value of x, or
#        the area under probability distribution from x-h to x+h for continuous distribution."""
#        raise NotImplementedError
#    def inverseCDF(self, probability): 
#        """
#        It does the reverse of CDF() method, it takes a probability value and returns the corresponding 
#        value on the x-axis."""
#        raise NotImplementedError
#    def mean(self): 
#        """Gives the arithmetic mean of the sample."""
#        raise NotImplementedError
#    def moments(self, r): 
#        """Gives the moments of the sample."""
#        raise NotImplementedError
#    def kurtosis(self): 
#        """Gives the kurtosis of the sample."""
#        raise NotImplementedError
#    def skew(self): 
#        """Gives the skew of the sample."""
#        raise NotImplementedError
#    def variance(self): 
#        """Gives the variance of the sample."""
#        raise NotImplementedError
#    def random(self):
#        """Gives a random number based on the distribution."""
#        raise NotImplementedError
        
class BetaDistribution(Distribution):
    pass
#    def __init__(self, **parameters): 
#        """Constructor method. The parameters are used to construct the probability distribution."""
#        raise NotImplementedError
#    def CDF(self, x): 
#        """
#        Cummulative Distribution Function, which gives the cummulative probability (area under the 
#        probability curve) from -infinity or 0 to a give x-value on the x-axis where y-axis is the 
#        probability."""
#        raise NotImplementedError
#    def PDF(self, x): 
#        """
#        Partial Distribution Function, which gives the probability for the particular value of x, or
#        the area under probability distribution from x-h to x+h for continuous distribution."""
#        raise NotImplementedError
#    def inverseCDF(self, probability): 
#        """
#        It does the reverse of CDF() method, it takes a probability value and returns the corresponding 
#        value on the x-axis."""
#        raise NotImplementedError
#    def mean(self): 
#        """Gives the arithmetic mean of the sample."""
#        raise NotImplementedError
#    def moments(self, r): 
#        """Gives the moments of the sample."""
#        raise NotImplementedError
#    def kurtosis(self): 
#        """Gives the kurtosis of the sample."""
#        raise NotImplementedError
#    def skew(self): 
#        """Gives the skew of the sample."""
#        raise NotImplementedError
#    def variance(self): 
#        """Gives the variance of the sample."""
#        raise NotImplementedError
#    def random(self):
#        """Gives a random number based on the distribution."""
#        raise NotImplementedError
    
class WeiBullDistribution(Distribution):
    pass
#    def __init__(self, **parameters): 
#        """Constructor method. The parameters are used to construct the probability distribution."""
#        raise NotImplementedError
#    def CDF(self, x): 
#        """
#        Cummulative Distribution Function, which gives the cummulative probability (area under the 
#        probability curve) from -infinity or 0 to a give x-value on the x-axis where y-axis is the 
#        probability."""
#        raise NotImplementedError
#    def PDF(self, x): 
#        """
#        Partial Distribution Function, which gives the probability for the particular value of x, or
#        the area under probability distribution from x-h to x+h for continuous distribution."""
#        raise NotImplementedError
#    def inverseCDF(self, probability): 
#        """
#        It does the reverse of CDF() method, it takes a probability value and returns the corresponding 
#        value on the x-axis."""
#        raise NotImplementedError
#    def mean(self): 
#        """Gives the arithmetic mean of the sample."""
#        raise NotImplementedError
#    def moments(self, r): 
#        """Gives the moments of the sample."""
#        raise NotImplementedError
#    def kurtosis(self): 
#        """Gives the kurtosis of the sample."""
#        raise NotImplementedError
#    def skew(self): 
#        """Gives the skew of the sample."""
#        raise NotImplementedError
#    def variance(self): 
#        """Gives the variance of the sample."""
#        raise NotImplementedError
#    def random(self):
#        """Gives a random number based on the distribution."""
#        raise NotImplementedError
    
class ParetoDistribution(Distribution):
    pass
#    def __init__(self, **parameters): 
#        """Constructor method. The parameters are used to construct the probability distribution."""
#        raise NotImplementedError
#    def CDF(self, x): 
#        """
#        Cummulative Distribution Function, which gives the cummulative probability (area under the 
#        probability curve) from -infinity or 0 to a give x-value on the x-axis where y-axis is the 
#        probability."""
#        raise NotImplementedError
#    def PDF(self, x): 
#        """
#        Partial Distribution Function, which gives the probability for the particular value of x, or
#        the area under probability distribution from x-h to x+h for continuous distribution."""
#        raise NotImplementedError
#    def inverseCDF(self, probability): 
#        """
#        It does the reverse of CDF() method, it takes a probability value and returns the corresponding 
#        value on the x-axis."""
#        raise NotImplementedError
#    def mean(self): 
#        """Gives the arithmetic mean of the sample."""
#        raise NotImplementedError
#    def moments(self, r): 
#        """Gives the moments of the sample."""
#        raise NotImplementedError
#    def kurtosis(self): 
#        """Gives the kurtosis of the sample."""
#        raise NotImplementedError
#    def skew(self): 
#        """Gives the skew of the sample."""
#        raise NotImplementedError
#    def variance(self): 
#        """Gives the variance of the sample."""
#        raise NotImplementedError
#    def random(self):
#        """Gives a random number based on the distribution."""
#        raise NotImplementedError
    
class CauchyDistribution(Distribution):
    pass
#    def __init__(self, **parameters): 
#        """Constructor method. The parameters are used to construct the probability distribution."""
#        raise NotImplementedError
#    def CDF(self, x): 
#        """
#        Cummulative Distribution Function, which gives the cummulative probability (area under the 
#        probability curve) from -infinity or 0 to a give x-value on the x-axis where y-axis is the 
#        probability."""
#        raise NotImplementedError
#    def PDF(self, x): 
#        """
#        Partial Distribution Function, which gives the probability for the particular value of x, or
#        the area under probability distribution from x-h to x+h for continuous distribution."""
#        raise NotImplementedError
#    def inverseCDF(self, probability): 
#        """
#        It does the reverse of CDF() method, it takes a probability value and returns the corresponding 
#        value on the x-axis."""
#        raise NotImplementedError
#    def mean(self): 
#        """Gives the arithmetic mean of the sample."""
#        raise NotImplementedError
#    def moments(self, r): 
#        """Gives the moments of the sample."""
#        raise NotImplementedError
#    def kurtosis(self): 
#        """Gives the kurtosis of the sample."""
#        raise NotImplementedError
#    def skew(self): 
#        """Gives the skew of the sample."""
#        raise NotImplementedError
#    def variance(self): 
#        """Gives the variance of the sample."""
#        raise NotImplementedError
#    def random(self):
#        """Gives a random number based on the distribution."""
#        raise NotImplementedError
    
class ExponentialDistribution(Distribution):
    pass
#    def __init__(self, **parameters): 
#        """Constructor method. The parameters are used to construct the probability distribution."""
#        raise NotImplementedError
#    def CDF(self, x): 
#        """
#        Cummulative Distribution Function, which gives the cummulative probability (area under the 
#        probability curve) from -infinity or 0 to a give x-value on the x-axis where y-axis is the 
#        probability."""
#        raise NotImplementedError
#    def PDF(self, x): 
#        """
#        Partial Distribution Function, which gives the probability for the particular value of x, or
#        the area under probability distribution from x-h to x+h for continuous distribution."""
#        raise NotImplementedError
#    def inverseCDF(self, probability): 
#        """
#        It does the reverse of CDF() method, it takes a probability value and returns the corresponding 
#        value on the x-axis."""
#        raise NotImplementedError
#    def mean(self): 
#        """Gives the arithmetic mean of the sample."""
#        raise NotImplementedError
#    def moments(self, r): 
#        """Gives the moments of the sample."""
#        raise NotImplementedError
#    def kurtosis(self): 
#        """Gives the kurtosis of the sample."""
#        raise NotImplementedError
#    def skew(self): 
#        """Gives the skew of the sample."""
#        raise NotImplementedError
#    def variance(self): 
#        """Gives the variance of the sample."""
#        raise NotImplementedError
#    def random(self):
#        """Gives a random number based on the distribution."""
#        raise NotImplementedError
    
class SampleDistribution(Distribution):
    def __init__(self, **parameters): 
        """Constructor method. The parameters are used to construct the probability distribution."""
        from SampleStatistics import ArithmeticMean
        from SampleStatistics import variance
        try: 
            self.data = list(parameters['data'])
            self.n = len(self.data)
            self.mean = ArithmeticMean(self.data)
            self.variance = variance(self.data, self.mean)
        except KeyError: 
            self.data = []
            self.n = 0
            self.mean = None
            self.variance = None
#    def CDF(self, x): 
#        """
#        Cummulative Distribution Function, which gives the cummulative probability (area under the 
#        probability curve) from -infinity or 0 to a give x-value on the x-axis where y-axis is the 
#        probability."""
#        raise NotImplementedError
#    def PDF(self, x): 
#        """
#        Partial Distribution Function, which gives the probability for the particular value of x, or
#        the area under probability distribution from x-h to x+h for continuous distribution."""
#        raise NotImplementedError
#    def inverseCDF(self, probability): 
#        """
#        It does the reverse of CDF() method, it takes a probability value and returns the corresponding 
#        value on the x-axis."""
#        raise NotImplementedError
    def mean(self): 
        """Gives the arithmetic mean of the sample."""
        return self.mean
#    def moments(self, r): 
#        """Gives the moments of the sample."""
#        raise NotImplementedError
#    def kurtosis(self): 
#        """Gives the kurtosis of the sample."""
#        raise NotImplementedError
#    def skew(self): 
#        """Gives the skew of the sample."""
#        raise NotImplementedError
    def variance(self): 
        """Gives the variance of the sample."""
        return self.variance
    def update(self, datalist):
        from SampleStatistics import arithmeticMean, variance
        self.data.append(datalist)
        self.n = len(self.data)
        self.mean = arithmeticMean(self.data)
        self.variance = variance(self.data, self.mean)
        
#class DummyDistribution(Distribution):
#    def __init__(self, **parameters): 
#        """Constructor method. The parameters are used to construct the probability distribution."""
#        raise NotImplementedError
#    def CDF(self, x): 
#        """
#        Cummulative Distribution Function, which gives the cummulative probability (area under the 
#        probability curve) from -infinity or 0 to a give x-value on the x-axis where y-axis is the 
#        probability."""
#        raise NotImplementedError
#    def PDF(self, x): 
#        """
#        Partial Distribution Function, which gives the probability for the particular value of x, or
#        the area under probability distribution from x-h to x+h for continuous distribution."""
#        raise NotImplementedError
#    def inverseCDF(self, probability): 
#        """
#        It does the reverse of CDF() method, it takes a probability value and returns the corresponding 
#        value on the x-axis."""
#        raise NotImplementedError
#    def mean(self): 
#        """Gives the arithmetic mean of the sample."""
#        raise NotImplementedError
#    def moments(self, r): 
#        """Gives the moments of the sample."""
#        raise NotImplementedError
#    def kurtosis(self): 
#        """Gives the kurtosis of the sample."""
#        raise NotImplementedError
#    def skew(self): 
#        """Gives the skew of the sample."""
#        raise NotImplementedError
#    def variance(self): 
#        """Gives the variance of the sample."""
#        raise NotImplementedError
#    def random(self):
#        """Gives a random number based on the distribution."""
#        raise NotImplementedError
        