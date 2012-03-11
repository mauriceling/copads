"""
Data Structures and Algorithms for Data Collected from One or More Samples.

The following functions were adapted from http://www.nmr.mgh.harvard.edu/
Neural_Systems_Group/gary/python/stats.py (assumes 1-dimensional list as 
input):
    - geometricMean
    - harmonicMean
    - arithmeticMean
    - median
    - medianScore
    - mode
    - moment
    - variation
    - skew
    - kurtosis

Copyright (c) Maurice H.T. Ling <mauriceling@acm.org>
"""

import math
from statisticsdistribution import Distribution
from copadsexceptions import FunctionParameterTypeError
from copadsexceptions import FunctionParameterValueError
from operations import summation
import nrpy

class SingleSample:
    data = None
    rowcount = 0
    name = None
    summary = {}
    
    def __init__(self, data, name):
        self.data = data
        self.rowcount = len(self.data)
        self.name = name
        #self.fullSummary()
        
    def geometricMean(self, inlist):
        """
        Calculates the geometric mean of the values in the passed list. That is:  
        n-th root of (x1 * x2 * ... * xn).  Assumes a '1D' list.

        Usage:   geometricMean(inlist)
        """
        mult = 1.0
        one_over_n = 1.0 / len(inlist)
        for item in inlist: mult = mult * math.pow(item, one_over_n)
        return mult
    
    def harmonicMean(self, inlist):
        """
        Calculates the harmonic mean of the values in the passed list.
        That is:  n / (1/x1 + 1/x2 + ... + 1/xn).  Assumes a '1D' list.

        Usage:   harmonicMean(inlist)
        """
        sum = 0.000001
        for item in inlist:
            if item != 0: sum = sum + 1.0/item
            else: sum = sum + 1.0/0.001
        return len(inlist) / sum
    
    def arithmeticMean(self, inlist):
        """
        Returns the arithematic mean of the values in the passed list.
        Assumes a '1D' list, but will function on the 1st dim of an array(!).

        Usage:   arithmeticMean(inlist)
        """
        sum = 0
        for item in inlist: sum = sum + item
        return sum / float(len(inlist))
    
    def moment(self, inlist, moment=1):
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
                s = s + (x - mn) ** moment
            return s / float(n)
        
    def skew(self, inlist):
        """
        Returns the skewness of a distribution, as defined in Numerical
        Recipies (alternate defn in CRC Standard Probability and Statistics, 
        p.6.)

        Usage:   skew(inlist)
        """
        return self.moment(inlist, 3) / math.pow(self.moment(inlist, 2), 1.5)

    def kurtosis(self, inlist):
        """
        Returns the kurtosis of a distribution, as defined in Numerical
        Recipies (alternate defn in CRC Standard Probability and Statistics, 
        p.6.)

        Usage:   kurtosis(inlist)
        """
        return self.moment(inlist, 4) / math.pow(self.moment(inlist, 2), 2.0)
    
    def variation(self, inlist):
        """
        Returns the coefficient of variation, as defined in CRC Standard
        Probability and Statistics, p.6.
        Ref: http://en.wikipedia.org/wiki/Coefficient_of_variation

        Usage:   variation(inlist)
        """
        return 100.0 * self.summary['stdev'] / self.summary['aMean']

    def range(self, inlist):
        inlist.sort()
        return float(inlist[-1]) - float(inlist[0])

    def midrange(self, inlist):
        inlist.sort()
        return float(inlist[int(round(len(inlist) * 0.75))]) - \
                float(inlist[int(round(len(inlist) * 0.75))])

    def variance(self, inlist, mean):
        sum = 0.0
        for item in inlist:
            sum = sum + (float(item) - float(mean)) ** 2
        return sum / float(len(inlist) - 1)
    
    def __str__(self):
        return str(self.summary)
        
    def fullSummary(self):
        self.summary['gMean'] = self.geometricMean(self.data)
        self.summary['hMean'] = self.harmonicMean(self.data)
        self.summary['aMean'] = self.arithmeticMean(self.data)
        self.summary['skew'] = self.skew(self.data)
        self.summary['kurtosis'] = self.kurtosis(self.data)
        self.summary['variance'] = self.variance(self.data,
                                        self.summary['aMean'])
        self.summary['stdev'] = self.summary['variance'] ** 0.5
        self.summary['variation'] = self.variation(self.data)
        self.summary['range'] = self.range(self.data)
        self.summary['median'] = nrpy.mdian1(self.data)
        #self.summary['midrange'] = self.midrange(self.data)
    
    
class SampleDistribution(Distribution):
    def __init__(self, sampleData):
        self.sample = sampleData

        
class TwoSample:
    sample = {}
    sample_name = []
    def __init__(self, data1, name1, data2, name2):
        if name1 == '': name1 = 'Sample 1'
        if name2 == '': name2 = 'Sample 2'
        self.sample_name = [name1, name2]
        self.sample[name1] = SingleSample(list(data1), name1)
        self.sample[name2] = SingleSample(list(data2), name2)

    def getSample(self, name):
        try: return self.sample[name].data
        except KeyError: return []

    def listSamples(self):
        return self.sample_name

    def covariance(self):
        """
        Calculates covariance using the formula: Cov(xy) = E(xy) - E(x)E(y)
        """
        sname = self.listSamples()
        if self.sample[sname[0]].data == self.sample[sname[1]].data: return 1.0
        if self.sample[sname[0]].rowcount == self.sample[sname[1]].rowcount:
            slen = self.sample[sname[0]].rowcount
        elif self.sample[sname[0]].rowcount > self.sample[sname[1]].rowcount:
            slen = self.sample[sname[1]].rowcount
        else: slen = self.sample[sname[0]].rowcount
        xy = SingleSample([self.sample[sname[0]].data[i] * \
                            self.sample[sname[1]].data[i]
                            for i in range(slen)], 'temporary')
        mean_xy = xy.arithmeticMean(xy.data)
        mean_x = self.sample[sname[0]]. \
                    arithmeticMean(self.sample[sname[0]].data)
        mean_y = self.sample[sname[1]]. \
                    arithmeticMean(self.sample[sname[1]].data)
        return mean_xy - (mean_x * mean_y)
    
    def linear_regression(self):
        sname = self.listSamples()
        if self.sample[sname[0]].rowcount == self.sample[sname[1]].rowcount:
            slen = self.sample[sname[0]].rowcount
        elif self.sample[sname[0]].rowcount > self.sample[sname[1]].rowcount:
            slen = self.sample[sname[1]].rowcount
        else: slen = self.sample[sname[0]].rowcount
        mean_x = self.sample[sname[0]]. \
                    arithmeticMean(self.sample[sname[0]].data)
        mean_y = self.sample[sname[1]]. \
                    arithmeticMean(self.sample[sname[1]].data)
        error_x = [self.sample[sname[0]].data[i] - mean_x 
                   for i in range(slen)]
        error_y = [self.sample[sname[1]].data[i] - mean_y 
                   for i in range(slen)]
        gradient = sum([error_x[index] * error_y[index]
                        for index in range(len(error_x))]) / \
                   sum([error_x[index] * error_x[index]
                        for index in range(len(error_x))])
        intercept = mean_y - (gradient * mean_x)
        return (gradient, intercept)
    
    def pearson(self):
        """
        Calculates the Pearson's product-moment coefficient by the formula
        
        (N * sum_xy) - (sum_x * sum_y)
        --------------------------------------------------------------
        ((N * sum_x2 - (sum_x)**2) * (N * sum_y2 - (sum_y)**2)) ** 0.5
        """
        sname = self.listSamples()
        if self.sample[sname[0]].rowcount == self.sample[sname[1]].rowcount:
            slen = self.sample[sname[0]].rowcount
        elif self.sample[sname[0]].rowcount > self.sample[sname[1]].rowcount:
            slen = self.sample[sname[1]].rowcount
        else: slen = self.sample[sname[0]].rowcount
        sum_x = summation([self.sample[sname[0]].data[i] 
                            for i in range(slen)])
        sum_x2 = summation([self.sample[sname[0]].data[i] * \
                            self.sample[sname[0]].data[i] 
                            for i in range(slen)])
        sum_y = summation([self.sample[sname[1]].data[i] 
                            for i in range(slen)])
        sum_y2 = summation([self.sample[sname[1]].data[i] * \
                            self.sample[sname[1]].data[i]
                            for i in range(slen)])
        sum_xy = summation([self.sample[sname[0]].data[i] * \
                            self.sample[sname[1]].data[i]
                            for i in range(slen)])
        numerator = (slen * sum_xy) - (sum_x * sum_y)
        denominator_x = (slen * sum_x2) - (sum_x * sum_x)
        denominator_y = (slen * sum_y2) - (sum_y * sum_y)
        return float(numerator / ((denominator_x * denominator_y) ** 0.5))
    
        
class MultiSample:
    sample = {}
    def __init__(self): pass
    
    def addSample(self, data, name):
        if name == '':
            try:
                temp = self.sample['Sample ' + str(len(self.sample))]
                import random
                name = 'Sample ' + str(int(random.random() * 1000000))
            except KeyError:
                name = 'Sample ' + str(len(self.sample) + 1)
        if type(sample) == list or type(sample) == tuple:
            sample = SingleSample(list(sample), name)
            self.sample[name] = sample
        else:
            self.sample[sample.name] = sample
            
    def getSample(self, name):
        try: return self.sample[name].data
        except KeyError: return []

    def listSamples(self):
        return self.sample.keys()
    
    
