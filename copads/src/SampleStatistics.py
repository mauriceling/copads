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
from Matrix import Matrix
from StatisticsDistribution import Distribution
from CopadsException import FunctionParameterTypeError
from CopadsException import FunctionParameterValueError
import NRPy

class SampleData:
    def __init__(self, **kwargs):
        self.data = Matrix(kwargs['data'])
        self.rowcount = self.data.rows()
        self.colcount = self.data.cols()
        self.summary = [{} for x in range(self.colcount)]
        
    def append(self, data, summarize = 'all'):
        if not (type(data) == list or type(data) == tuple):
            raise FunctionParameterTypeError('Input must be either \
                    list or tuple, % given ' % str(type(data)))
        for x in data:
            if not (type(data) == list or type(data) == tuple):
                raise FunctionParameterTypeError('Input must be either \
                    list or tuple, % found' % str(type(data)))
            if len(x) <> self.colcount:
                raise FunctionParameterValueError('%d data elements required \
                    for each data, %d elements given' % \
                    (str(self.colcount), str(len(x))))
        for x in data: self.data.m.append(x)
        if summarize == 'all': self.fullSummary()
        
    def geometricMean (self, inlist):
        """
        Calculates the geometric mean of the values in the passed list. That is:  
        n-th root of (x1 * x2 * ... * xn).  Assumes a '1D' list.

        Usage:   geometricMean(inlist)
        """
        mult = 1.0
        one_over_n = 1.0/len(inlist)
        for item in inlist: mult = mult * pow(item,one_over_n)
        return mult
    
    def harmonicMean (self, inlist):
        """
        Calculates the harmonic mean of the values in the passed list.
        That is:  n / (1/x1 + 1/x2 + ... + 1/xn).  Assumes a '1D' list.

        Usage:   harmonicMean(inlist)
        """
        sum = 0
        for item in inlist: sum = sum + 1.0/item
        return len(inlist) / sum
    
    def arithmeticMean (self, inlist):
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
        return self.moment(inlist,3)/pow(self.moment(inlist,2),1.5)

    def kurtosis(self, inlist):
        """
        Returns the kurtosis of a distribution, as defined in Numerical
        Recipies (alternate defn in CRC Standard Probability and Statistics, 
        p.6.)

        Usage:   kurtosis(inlist)
        """
        return self.moment(inlist,4)/pow(self.moment(inlist,2),2.0)
    
    def variation(self, inlist):
        """
        Returns the coefficient of variation, as defined in CRC Standard
        Probability and Statistics, p.6.
        Ref: http://en.wikipedia.org/wiki/Coefficient_of_variation

        Usage:   variation(inlist)
        """
        return 100.0*self.stdev(inlist)/float(self.arithmeticMean(inlist))

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

    def stdev(self, inlist):
        return math.sqrt(variance(inlist, arithmeticMean(inlist)))
    
    def fullSummary(self):
        for x in range(self.colcount):
            data = self.data.col(x)
            self.summary[x]['gMean'] = self.geometricMean(data)
            self.summary[x]['hMean'] = self.harmonicMean(data)
            self.summary[x]['aMean'] = self.arithmeticMean(data)
            self.summary[x]['skew'] = self.skew(data)
            self.summary[x]['kurtosis'] = self.kurtosis(data)
            self.summary[x]['variation'] = self.variation(data)
            self.summary[x]['range'] = self.range(data)
            self.summary[x]['median'] = NRPy.mdian1(data)
            self.summary[x]['midrange'] = self.midrange(data)
            self.summary[x]['variance'] = self.variance(data,
                                            self.summary[x]['aMean'])
            self.summary[x]['stdev'] = self.summary[x]['variance'] ** 0.5
            
    def covariance(self, inlist1, inlist2):
        """
        Calculates covariance using the formula: Cov(xy)  =  E{xy}  -  E{x}E{y}
        """
        if inlist1 == inlist2: return 1.0
        mean_xy = self.arithmeticMean([inlist1[i]*inlist1[i] 
                                        for i in range(inlist1)])
        mean_x = self.arithmeticMean(inlist1)
        mean_y = self.arithmeticMean(inlist2)
        return mean_xy - (mean_x * mean_y)
    
    
class SampleDistribution(Distribution):
    def __init__(self, sampleData):
        self.sample = sampleData