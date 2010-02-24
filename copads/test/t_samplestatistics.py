import sys
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'copads'))
import samplestatistics as S

data1 = [1, 2, 3, 4, 5]
name1 = 'data1'
data2 = [2, 3, 4, 5, 6]
name2 = 'data2'

class testSingleSample(unittest.TestCase):
    def setUp(self):
        self.data = S.SingleSample(data1, name1)
        self.data.fullSummary()
    def testInit(self):
        self.assertEqual(self.data.data, data1)
        self.assertEqual(self.data.name, name1)
        self.assertEqual(self.data.rowcount, len(data1))
    def testhMean(self):
        self.assertAlmostEqual(self.data.summary['hMean'], 2.18978, places=4) 
    def testaMean(self):
        self.assertAlmostEqual(self.data.summary['aMean'], 3.00000, places=4)
    def testgMean(self):
        self.assertAlmostEqual(self.data.summary['gMean'], 2.60517, places=4)
    def testSkew(self):
        self.assertAlmostEqual(self.data.summary['skew'], 0.00000, places=4)
    def testKurtosis(self):
        self.assertAlmostEqual(self.data.summary['kurtosis'], 1.70000, places=4)
    def testSTDEV(self):
        self.assertAlmostEqual(self.data.summary['stdev'], 1.58114, places=4)
    def testMedian(self):
        self.assertAlmostEqual(self.data.summary['median'], 3.00000, places=4)
    def testVariation(self):
        self.assertAlmostEqual(self.data.summary['variation'], 52.70462, 
                                places=4)
    def testVariance(self):
        self.assertAlmostEqual(self.data.summary['variance'], 2.50000, places=4)
    def testRange(self):
        self.assertAlmostEqual(self.data.summary['range'], 4.00000, places=4)    
    
class testTwoSample(unittest.TestCase):
    def setUp(self):
        self.data = S.TwoSample(data1, name1, data2, name2)
    def testInit(self):
        self.assertEqual(self.data.listSamples(), ['data1', 'data2'])
        self.assertEqual(self.data.getSample('data1'), data1)
        self.assertEqual(self.data.getSample('data2'), data2)
        self.assertEqual(self.data.getSample('nodata'), [])
    def testCovariance(self):
        self.assertAlmostEqual(self.data.covariance(), 2.00000, places=4)
    def testPearson1(self):
        self.assertAlmostEqual(self.data.pearson(), 1.00000, places=4)
    def testLM1(self):
        self.assertAlmostEqual(self.data.linear_regression()[0], 
                                1.00000, places=4)
        self.assertAlmostEqual(self.data.linear_regression()[1], 
                                1.00000, places=4)
        
if __name__ == '__main__':
    unittest.main()
