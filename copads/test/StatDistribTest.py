import sys
import os
import unittest



class testBeta(unittest.TestCase):
    def testCDF1(self):
        self.assertAlmostEqual(N.BetaDistribution(location = 0,
                                                  scale = 1,
                                                  p = 1, q = 2).CDF(1.0), 1.0)
    def testCDF2(self):
        self.assertAlmostEqual(N.BetaDistribution(location = 0,
                                                  scale = 1,
                                                  p = 6, q = 2).CDF(1.0), 1.0)  

class testBinomial(unittest.TestCase):
    def testCDF1(self):
        self.assertAlmostEqual(N.BinomialDistribution().CDF(500), 0.5126125) 
                
class testNormal(unittest.TestCase):
    def testCDF1(self):
        self.assertAlmostEqual(N.NormalDistribution().CDF(0), 0.5)
#    def testPDF1(self):
#        self.assertAlmostEqual(N.NormalDistribution().PDF(0), 0.3989423)
#    def testinverseCDF1(self):
#        self.assertAlmostEqual(N.NormalDistribution().inverseCDF(0.5), 0)
  
    
    
if __name__ == '__main__':
    sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'src'))
    import StatisticsDistribution as N
    unittest.main()