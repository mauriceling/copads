"""
This file hold the functions to calculate descriptive statistics of a data set.

The following functions were adapted from http://www.nmr.mgh.harvard.edu/Neural_Systems_Group/gary/
python/stats.py (assumes 1-dimensional list as input):
    1. GeometricMean
    2. HarmonicMean
    3. ArithmeticMean
    4. Median
    5. MedianScore
    6. Mode
    7. Moment
    8. Variation
    9. Skew
    10. Kurtosis
    11. Describe
    """
    
def GeometricMean (inlist):
    """
    Calculates the geometric mean of the values in the passed list. That is:  n-th root of 
    (x1 * x2 * ... * xn).  Assumes a '1D' list.

    Usage:   GeometricMean(inlist)
    """
    mult = 1.0
    one_over_n = 1.0/len(inlist)
    for item in inlist: mult = mult * pow(item,one_over_n)
    return mult


def HarmonicMean (inlist):
    """
Calculates the harmonic mean of the values in the passed list.
That is:  n / (1/x1 + 1/x2 + ... + 1/xn).  Assumes a '1D' list.

Usage:   HarmonicMean(inlist)
"""
    sum = 0
    for item in inlist: sum = sum + 1.0/item
    return len(inlist) / sum


def ArithmeticMean (inlist):
    """
Returns the arithematic mean of the values in the passed list.
Assumes a '1D' list, but will function on the 1st dim of an array(!).

Usage:   ArithmeticMean(inlist)
"""
    sum = 0
    for item in inlist: sum = sum + item
    return sum/float(len(inlist))


def Median (inlist,numbins=1000):
    """
Returns the computed median value of a list of numbers, given the
number of bins to use for the histogram (more bins brings the computed value
closer to the median score, default number of bins = 1000).  See G.W.
Heiman's Basic Stats (1st Edition), or CRC Probability & Statistics.

Usage:   Median (inlist, numbins=1000)
"""
    (hist, smallest, binsize, extras) = histogram(inlist,numbins) # make histog
    cumhist = cumsum(hist)              # make cumulative histogram
    for i in range(len(cumhist)):        # get 1st(!) index holding 50%ile score
        if cumhist[i]>=len(inlist)/2.0:
            cfbin = i
            break
    LRL = smallest + binsize*cfbin        # get lower read limit of that bin
    cfbelow = cumhist[cfbin-1]
    freq = float(hist[cfbin])                # frequency IN the 50%ile bin
    median = LRL + ((len(inlist)/2.0 - cfbelow)/float(freq))*binsize  # median formula
    return median


def MedianScore (inlist):
    """
Returns the 'middle' score of the passed list.  If there is an even
number of scores, the mean of the 2 middle scores is returned.

Usage:   MedianScore(inlist)
"""

    newlist = copy.deepcopy(inlist)
    newlist.sort()
    if len(newlist) % 2 == 0:   # if even number of scores, average middle 2
        index = len(newlist)/2  # integer division correct
        median = float(newlist[index] + newlist[index-1]) /2
    else:
        index = len(newlist)/2  # int divsion gives mid value when count from 0
        median = newlist[index]
    return median


def Mode(inlist):
    """
Returns a list of the modal (most common) score(s) in the passed
list.  If there is more than one such score, all are returned.  The
bin-count for the mode(s) is also returned.

Usage:   Mode(inlist)
Returns: bin-count for mode(s), a list of modal value(s)
"""

    scores = pstat.unique(inlist)
    scores.sort()
    freq = []
    for item in scores:
        freq.append(inlist.count(item))
    maxfreq = max(freq)
    mode = []
    stillmore = 1
    while stillmore:
        try:
            indx = freq.index(maxfreq)
            mode.append(scores[indx])
            del freq[indx]
            del scores[indx]
        except ValueError:
            stillmore=0
    return maxfreq, mode



def Moment(inlist,moment=1):
    """
Calculates the nth moment about the mean for a sample (defaults to
the 1st moment).  Used to calculate coefficients of skewness and kurtosis.

Usage:   Moment(inlist,moment=1)
Returns: appropriate moment (r) from ... 1/n * SUM((inlist(i)-mean)**r)
"""
    if moment == 1:
        return 0.0
    else:
        mn = mean(inlist)
        n = len(inlist)
        s = 0
        for x in inlist:
            s = s + (x-mn)**moment
        return s/float(n)


def Variation(inlist):
    """
Returns the coefficient of variation, as defined in CRC Standard
Probability and Statistics, p.6.

Usage:   Variation(inlist)
"""
    return 100.0*samplestdev(inlist)/float(mean(inlist))


def Skew(inlist):
    """
Returns the skewness of a distribution, as defined in Numerical
Recipies (alternate defn in CRC Standard Probability and Statistics, p.6.)

Usage:   Skew(inlist)
"""
    return moment(inlist,3)/pow(moment(inlist,2),1.5)


def Kurtosis(inlist):
    """
Returns the kurtosis of a distribution, as defined in Numerical
Recipies (alternate defn in CRC Standard Probability and Statistics, p.6.)

Usage:   Kurtosis(inlist)
"""
    return moment(inlist,4)/pow(moment(inlist,2),2.0)


def range(inlist):
    inlist.sort()
    return float(inlist[-1])-float(inlist[0])

def midrange(inlist):
    inlist.sort()
    return float(inlist[int(round(len(inlist)*0.75))])-float(inlist[int(round(len(inlist)*0.75))])

def variance(inlist, mean):
    sum = 0.0
    for item in inlist:
        sum = sum + (float(item)-float(mean))**2
    return sum/float(len(inlist)-1)

def standarddeviation(inlist, mean):
    return math.sqrt(variance(inlist, mean))

def Describe(inlist):
    """
Returns some descriptive statistics of the passed list (assumed to be 1D).

Usage:   Describe(inlist)
Returns: n, mean, standard deviation, skew, kurtosis
"""
    n = len(inlist)
    mm = (min(inlist),max(inlist))
    m = mean(inlist)
    sd = stdev(inlist)
    sk = skew(inlist)
    kurt = kurtosis(inlist)
    return n, mm, m, sd, sk, kurt