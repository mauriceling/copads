import sys
import os
import unittest



class testNormal(unittest.TestCase):
    def testCDF1(self):
        self.assertAlmostEqual(N.NormalDistribution().CDF(0), 0.5)
    def testCDF2(self):
        self.assertAlmostEqual(N.NormalDistribution().CDF(2), 0.9772499)
#    def testPDF1(self):
#        self.assertAlmostEqual(N.NormalDistribution().PDF(0), 0.3989423)
#    def testinverseCDF1(self):
#        self.assertAlmostEqual(N.NormalDistribution().inverseCDF(0.5), 0)
  
class testBinomial(unittest.TestCase):
    def testCDF1(self):
        self.assertAlmostEqual(N.BinomialDistribution().CDF(500), 0.5126125)
    def testCDF2(self):
        self.assertAlmostEqual(N.BinomialDistribution().CDF(550), 0.9993041)  
    
    
if __name__ == '__main__':
    sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'src'))
    import StatisticsDistribution as N
    unittest.main()