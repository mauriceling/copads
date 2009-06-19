"""
This file hold the functions to calculate descriptive statistics of a data set.

The following functions were adapted from http://www.nmr.mgh.harvard.edu/
Neural_Systems_Group/gary/python/stats.py (assumes 1-dimensional list as 
input):
    1. geometricMean
    2. harmonicMean
    3. arithmeticMean
    4. median
    5. medianScore
    6. mode
    7. moment
    8. variation
    9. skew
    10. kurtosis
    """

import math
from StatisticsDistribution import Distribution
from CopadsExceptions import FunctionParameterTypeError
from CopadsExceptions import FunctionParameterValueError
import NRPy

class SingleSample:
    data = None
    rowcount = 0
    name = None
    summary = {}
    
    def __init__(self, **kwargs):
        self.data = kwargs['data']
        self.rowcount = len(self.data)
        self.name = kwargs['name']
        self.summary = self.fullSummary()
        
    def append(self, data):
        if not (type(data) == list or type(data) == tuple):
            raise FunctionParameterTypeError('Input must be either \
                    list or tuple, % given ' % str(type(data)))
        self.data = self.data + list(data)
        self.summary = self.fullSummary()
        
    def geometricMean(self, inlist):
        """
        Calculates the geometric mean of the values in the passed list. That is:  
        n-th root of (x1 * x2 * ... * xn).  Assumes a '1D' list.

        Usage:   geometricMean(inlist)
        """
        mult = 1.0
        one_over_n = 1.0/len(inlist)
        for item in inlist: mult = mult * math.pow(item,one_over_n)
        return mult
    
    def harmonicMean(self, inlist):
        """
        Calculates the harmonic mean of the values in the passed list.
        That is:  n / (1/x1 + 1/x2 + ... + 1/xn).  Assumes a '1D' list.

        Usage:   harmonicMean(inlist)
        """
        sum = 0
        for item in inlist: sum = sum + 1.0/item
        return len(inlist) / sum
    
    def arithmeticMean(self, inlist):
        """
        Returns the arithematic mean of the values in the passed list.
        Assumes a '1D' list, but will function on the 1st dim of an array(!).

        Usage:   arithmeticMean(inlist)
        """
        sum = 0
        for item in inlist: sum = sum + item
        return sum/float(len(inlist))
    
    def moment(self, inlist,moment=1):
        """
        Calculates the nth moment about the mean for a sample (defaults to
        the 1st moment).  Used to calculate coefficients of skewness and 
        kurtosis.

        Usage:   moment(inlist,moment=1)
        Returns: appropriate moment (r) from ... 1/n * SUM((inlist(i)-mean)**r)
        """
        if moment == 1:
            return 0.0
        else:
            mn = self.arithmeticMean(inlist)
            n = len(inlist)
            s = 0
            for x in inlist:
                s = s + (x-mn)**moment
            return s/float(n)
        
    def skew(self, inlist):
        """
        Returns the skewness of a distribution, as defined in Numerical
        Recipies (alternate defn in CRC Standard Probability and Statistics, 
        p.6.)

        Usage:   skew(inlist)
        """
        return self.moment(inlist,3)/math.pow(self.moment(inlist,2),1.5)

    def kurtosis(self, inlist):
        """
        Returns the kurtosis of a distribution, as defined in Numerical
        Recipies (alternate defn in CRC Standard Probability and Statistics, 
        p.6.)

        Usage:   kurtosis(inlist)
        """
        return self.moment(inlist,4)/math.pow(self.moment(inlist,2),2.0)
    
    def variation(self, inlist):
        """
        Returns the coefficient of variation, as defined in CRC Standard
        Probability and Statistics, p.6.
        Ref: http://en.wikipedia.org/wiki/Coefficient_of_variation

        Usage:   variation(inlist)
        """
        return 100.0*self.summary['stdev']/self.summary['aMean']

    def range(self, inlist):
        inlist.sort()
        return float(inlist[-1])-float(inlist[0])

    def midrange(self, inlist):
        inlist.sort()
        return float(inlist[int(round(len(inlist)*0.75))]) - \
                float(inlist[int(round(len(inlist)*0.75))])

    def variance(self, inlist, mean):
        sum = 0.0
        for item in inlist:
            sum = sum + (float(item)-float(mean))**2
        return sum/float(len(inlist)-1)
    
    def fullSummary(self):
        self.summary['gMean'] = self.geometricMean(self.data)
        self.summary['hMean'] = self.harmonicMean(self.data)
        self.summary['aMean'] = self.arithmeticMean(self.data)
        self.summary['skew'] = self.skew(self.data)
        self.summary['kurtosis'] = self.kurtosis(self.data)
        self.summary['variation'] = self.variation(self.data)
        self.summary['range'] = self.range(self.data)
        self.summary['median'] = NRPy.mdian1(self.data)
        self.summary['midrange'] = self.midrange(self.data)
        self.summary['variance'] = self.variance(self.data,
                                        self.summary['aMean'])
        self.summary['stdev'] = self.summary['variance'] ** 0.5
    
    
class SampleDistribution(Distribution):
    def __init__(self, sampleData):
        self.sample = sampleData
        
class MultiSample:
    sample = {}
    def __init__(self): pass
    
    def addSample(self, sample, name = None):
        if type(sample) == list or type(sample) == tuple:
            sample = SingleSample(data = list(sample), name = name)
            self.sample[name] = sample
        else:
            self.sample[sample.name] = sample
            
    
    def covariance(self, inlist1, inlist2):
        """
        Calculates covariance using the formula: Cov(xy)  =  E{xy}  -  E{x}E{y}
        """
        if inlist1 == inlist: return 1.0
        mean_xy = self.arithmeticMean([inlist1[i]*inlist1[i] 
                                                     for i in range(inlist1)])
        mean_x = self.arithmeticMean(inlist1)
        mean_y = self.arithmeticMean(inlist2)
        return mean_xy - (mean_x * mean_y)
    
    def pearson(self, inlist1, inlist2):
        """
        Calculates the Pearson's product-moment coefficient by dividing the
        covariance by the product of the 2 standard deviations.
        """
        return self.covariance(inlist1, inlist2) / \
            (self.stdev(inlist1) * self.stdev(inlist2))
    
    
