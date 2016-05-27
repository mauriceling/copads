import sys, os
sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'copads'))

import random

import randomize as r
import hypothesis as h

n = 10000
nbins = 15

def binning(value=None, bins=None, nbins=10, lower=0.0, upper=1.0):
    if not bins:
        bins = {}
        bins['bins'] = [0] * int(nbins)
        bins['width'] = (float(upper) - float(lower)) / int(nbins)
    if value:
        bin_number = float(value) / bins['width']
        bin_number = int(round(bin_number))
        if bin_number == len(bins['bins']):
            bin_number = len(bins['bins']) - 1
        try: bins['bins'][bin_number] = bins['bins'][bin_number] + 1
        except IndexError: pass
    return bins


randomizer = r.LCG(None, 'mmix')

count = 0
expected = binning(None, None, nbins, 0.0, 1.0)
observed = binning(None, None, nbins, 0.0, 1.0)

while count < n:
    observed = binning(randomizer.random(), observed)
    expected = binning(random.random(), expected)
    count = count + 1

print sum(expected['bins']), expected['bins']
print sum(observed['bins']), observed['bins']
print h.ChisqFit(expected['bins'], observed['bins'], 0.99)
