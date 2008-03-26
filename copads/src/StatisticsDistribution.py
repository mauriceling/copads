"""
File containing the functions for various statistical distributions.

Copyright (c) Maurice H.T. Ling <mauriceling@acm.org>
Date created: 17th August 2005
"""

from CopadsExceptions import DistributionParameterError

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
        probability."""
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
        """Gives the moments of the sample."""
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
        

class NormalDistribution(Distribution):
    def __init__(self, parameters = {}):
        try: self.mean = parameters['mean']
        except KeyError:
            self.mean = 0.0
            self.variance = 1.0
        try: self.variance = parameters['variance']
        except KeyError:
            self.mean = 0.0
            self.variance = 1.0
    def CDF(self, x): raise NotImplementedError
    def PDF(self, x): raise NotImplementedError
    def inverseCDF(self, probability): raise NotImplementedError
    def mean(self): return self.mean
    def moments(self, r): raise NotImplementedError
    def kurtosis(self): raise NotImplementedError
    def skew(self): raise NotImplementedError
    def variance(self): return self.variance
    
class ChiSquareDistribution(Distribution):
    def __init__(self, **parameters): 
        """Constructor method. The parameters are used to construct the probability distribution."""
        raise NotImplementedError
    def CDF(self, x): 
        """
        Cummulative Distribution Function, which gives the cummulative probability (area under the 
        probability curve) from -infinity or 0 to a give x-value on the x-axis where y-axis is the 
        probability."""
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
        """Gives the moments of the sample."""
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
    
class TDistribution(Distribution):
    def __init__(self, **parameters): 
        """Constructor method. The parameters are used to construct the probability distribution."""
        raise NotImplementedError
    def CDF(self, x): 
        """
        Cummulative Distribution Function, which gives the cummulative probability (area under the 
        probability curve) from -infinity or 0 to a give x-value on the x-axis where y-axis is the 
        probability."""
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
        """Gives the moments of the sample."""
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
 
class FDistribution(Distribution):
    def __init__(self, **parameters): 
        """Constructor method. The parameters are used to construct the probability distribution."""
        raise NotImplementedError
    def CDF(self, x): 
        """
        Cummulative Distribution Function, which gives the cummulative probability (area under the 
        probability curve) from -infinity or 0 to a give x-value on the x-axis where y-axis is the 
        probability."""
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
        """Gives the moments of the sample."""
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
       
class BinomialDistribution(Distribution):
    def __init__(self, **parameters): 
        """Constructor method. The parameters are used to construct the probability distribution."""
        raise NotImplementedError
    def CDF(self, x): 
        """
        Cummulative Distribution Function, which gives the cummulative probability (area under the 
        probability curve) from -infinity or 0 to a give x-value on the x-axis where y-axis is the 
        probability."""
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
        """Gives the moments of the sample."""
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
    
class PoissonDistribution(Distribution):
    def __init__(self, **parameters): 
        """Constructor method. The parameters are used to construct the probability distribution."""
        self.mean = parameters['mean']
    def CDF(self, x): 
        """
        Cummulative Distribution Function, which gives the cummulative probability (area under the 
        probability curve) from -infinity or 0 to a give x-value on the x-axis where y-axis is the 
        probability."""
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
        return self.mean
    def moments(self, r): 
        """Gives the moments of the sample."""
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
    
class GeometricDistribution(Distribution):
    def __init__(self, **parameters): 
        """Constructor method. The parameters are used to construct the probability distribution."""
        raise NotImplementedError
    def CDF(self, x): 
        """
        Cummulative Distribution Function, which gives the cummulative probability (area under the 
        probability curve) from -infinity or 0 to a give x-value on the x-axis where y-axis is the 
        probability."""
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
        """Gives the moments of the sample."""
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
    
class LogNormalDistribution(Distribution):
    def __init__(self, **parameters): 
        """Constructor method. The parameters are used to construct the probability distribution."""
        raise NotImplementedError
    def CDF(self, x): 
        """
        Cummulative Distribution Function, which gives the cummulative probability (area under the 
        probability curve) from -infinity or 0 to a give x-value on the x-axis where y-axis is the 
        probability."""
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
        """Gives the moments of the sample."""
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
        
class BetaDistribution(Distribution):
    def __init__(self, **parameters): 
        """Constructor method. The parameters are used to construct the probability distribution."""
        raise NotImplementedError
    def CDF(self, x): 
        """
        Cummulative Distribution Function, which gives the cummulative probability (area under the 
        probability curve) from -infinity or 0 to a give x-value on the x-axis where y-axis is the 
        probability."""
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
        """Gives the moments of the sample."""
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
    
class WeiBullDistribution(Distribution):
    def __init__(self, **parameters): 
        """Constructor method. The parameters are used to construct the probability distribution."""
        raise NotImplementedError
    def CDF(self, x): 
        """
        Cummulative Distribution Function, which gives the cummulative probability (area under the 
        probability curve) from -infinity or 0 to a give x-value on the x-axis where y-axis is the 
        probability."""
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
        """Gives the moments of the sample."""
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
    
class ParetoDistribution(Distribution):
    def __init__(self, **parameters): 
        """Constructor method. The parameters are used to construct the probability distribution."""
        raise NotImplementedError
    def CDF(self, x): 
        """
        Cummulative Distribution Function, which gives the cummulative probability (area under the 
        probability curve) from -infinity or 0 to a give x-value on the x-axis where y-axis is the 
        probability."""
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
        """Gives the moments of the sample."""
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
    
class CauchyDistribution(Distribution):
    def __init__(self, **parameters): 
        """Constructor method. The parameters are used to construct the probability distribution."""
        raise NotImplementedError
    def CDF(self, x): 
        """
        Cummulative Distribution Function, which gives the cummulative probability (area under the 
        probability curve) from -infinity or 0 to a give x-value on the x-axis where y-axis is the 
        probability."""
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
        """Gives the moments of the sample."""
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
    
class ExponentialDistribution(Distribution):
    def __init__(self, **parameters): 
        """Constructor method. The parameters are used to construct the probability distribution."""
        raise NotImplementedError
    def CDF(self, x): 
        """
        Cummulative Distribution Function, which gives the cummulative probability (area under the 
        probability curve) from -infinity or 0 to a give x-value on the x-axis where y-axis is the 
        probability."""
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
        """Gives the moments of the sample."""
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
    def CDF(self, x): 
        """
        Cummulative Distribution Function, which gives the cummulative probability (area under the 
        probability curve) from -infinity or 0 to a give x-value on the x-axis where y-axis is the 
        probability."""
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
        return self.mean
    def moments(self, r): 
        """Gives the moments of the sample."""
        raise NotImplementedError
    def kurtosis(self): 
        """Gives the kurtosis of the sample."""
        raise NotImplementedError
    def skew(self): 
        """Gives the skew of the sample."""
        raise NotImplementedError
    def variance(self): 
        """Gives the variance of the sample."""
        return self.variance
    def update(self, datalist):
        from CentralTendency import ArithmeticMean
        from DistributionSpread import variance
        self.data.append(datalist)
        self.n = len(self.data)
        self.mean = ArithmeticMean(self.data)
        self.variance = variance(self.data, self.mean)
        