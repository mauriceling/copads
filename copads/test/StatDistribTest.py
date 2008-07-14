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
    def testPDF(self):
        pass
    def testinverseCDF(self):
        pass

class testBinomial(unittest.TestCase):
    def testCDF1(self):
        self.assertAlmostEqual(N.BinomialDistribution().CDF(500), 0.5126125) 
    def testPDF(self):
        pass
    def testinverseCDF(self):
        pass
        
class testCauchy(unittest.TestCase):
    def testCDF(self):
        pass
    def testPDF(self):
        pass
    def testinverseCDF(self):
        pass

class testChiSquare(unittest.TestCase):
    def testCDF(self):
        pass
    def testPDF(self):
        pass
    def testinverseCDF(self):
        pass

class testCosine(unittest.TestCase):
    def testCDF(self):
        pass
    def testPDF(self):
        pass
    def testinverseCDF(self):
        pass
          
class testExponential(unittest.TestCase):
    def testCDF(self):
        pass
    def testPDF(self):
        pass
    def testinverseCDF(self):
        pass

class testF(unittest.TestCase):
    def testCDF(self):
        pass
    def testPDF(self):
        pass
    def testinverseCDF(self):
        pass

class testGeometric(unittest.TestCase):
    def testCDF(self):
        pass
    def testPDF(self):
        pass
    def testinverseCDF(self):
        pass

class testGumbel(unittest.TestCase):
    def testCDF(self):
        pass
    def testPDF(self):
        pass
    def testinverseCDF(self):
        pass
      
class testLogarithmic(unittest.TestCase):
    def testCDF(self):
        pass
    def testPDF(self):
        pass
    def testinverseCDF(self):
        pass

class testLogNormal(unittest.TestCase):
    def testCDF(self):
        pass
    def testPDF(self):
        pass
    def testinverseCDF(self):
        pass

class testNegativeBinomial(unittest.TestCase):
    def testCDF(self):
        pass
    def testPDF(self):
        pass
    def testinverseCDF(self):
        pass

class testNormal(unittest.TestCase):
    def testCDF1(self):
        self.assertAlmostEqual(N.NormalDistribution().CDF(0), 0.5)
    def testPDF1(self):
        self.assertAlmostEqual(N.NormalDistribution().PDF(0), 0.3989423)
    def testinverseCDF1(self):
        self.assertAlmostEqual(N.NormalDistribution().inverseCDF(0.5)[0], 0)
  
class testPareto(unittest.TestCase):
    def testCDF(self):
        pass
    def testPDF(self):
        pass
    def testinverseCDF(self):
        pass

class testPoisson(unittest.TestCase):
    def testCDF(self):
        pass
    def testPDF(self):
        pass
    def testinverseCDF(self):
        pass

class testSemicircular(unittest.TestCase):
    def testCDF(self):
        pass
    def testPDF(self):
        pass
    def testinverseCDF(self):
        pass
    
class testT(unittest.TestCase):
    def testCDF(self):
        pass
    def testPDF(self):
        pass
    def testinverseCDF(self):
        pass
    
class testUniform(unittest.TestCase):
    def testCDF(self):
        pass
    def testPDF(self):
        pass
    def testinverseCDF(self):
        pass

class testWeibull(unittest.TestCase):
    def testCDF(self):
        pass
    def testPDF(self):
        pass
    def testinverseCDF(self):
        pass
    
if __name__ == '__main__':
    sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'src'))
    import StatisticsDistribution as N
    unittest.main()