import sys
import os
import unittest



class testBeta(unittest.TestCase):
    def testCDF1(self):
        p = N.BetaDistribution(location = 0, scale = 1, p = 1, q = 2).CDF(1.0)
        self.assertTrue(abs(p/1.0 - 1) < 0.01)
    def testCDF2(self):
        p = N.BetaDistribution(location = 0, scale = 1, p = 6, q = 2).CDF(1.0)
        self.assertTrue(abs(p/1.0 - 1) < 0.01)  
    def testPDF(self):
        pass
    def testinverseCDF(self):
        pass

class testBinomial(unittest.TestCase):
    def testCDF1(self):
        p = N.BinomialDistribution(trial = 1000, success = 0.5).CDF(500)
        self.assertTrue(abs(p/0.5126125 - 1) < 0.01) 
    def testPDF1(self):
        p = N.BinomialDistribution(trial = 20, success = 0.5).PDF(10)
        self.assertTrue(abs(p/0.1762 - 1) < 0.01)
    def testPDF2(self):
        p = N.BinomialDistribution(trial = 20, success = 0.1).PDF(1)
        self.assertTrue(abs(p/0.27017 - 1) < 0.01)
    def testPDF3(self):
        p = N.BinomialDistribution(trial = 20, success = 0.1).PDF(3)
        self.assertTrue(abs(p/0.19012 - 1) < 0.01)
    def testPDF4(self):
        p = N.BinomialDistribution(trial = 20, success = 0.1).PDF(4)
        self.assertTrue(abs(p/0.08978 - 1) < 0.01)
##    def testinverseCDF1(self):
##        pass
        
        
class testCauchy(unittest.TestCase):
    def testCDF1(self):
        p = N.CauchyDistribution(location = 0.0, scale = 1.0).CDF(0.0)
        self.assertTrue(abs(p/0.5 - 1) < 0.01)
    def testCDF2(self):
        p = N.CauchyDistribution(location = 0.0, scale = 1.0).CDF(1.0)
        self.assertTrue(abs(p/0.75 - 1) < 0.01)
    def testCDF3(self):
        p = N.CauchyDistribution(location = 0.0, scale = 1.0).CDF(2.0)
        self.assertTrue(abs(p/0.8524163 - 1) < 0.01)
    def testPDF1(self):
        p = N.CauchyDistribution(location = 0.0, scale = 1.0).PDF(0.0)
        self.assertTrue(abs(p/0.3183098 - 1) < 0.01)
    def testPDF2(self):
        p = N.CauchyDistribution(location = 0.0, scale = 1.0).PDF(1.0)
        self.assertTrue(abs(p/0.1591549 - 1) < 0.01)
    def testPDF3(self):
        p = N.CauchyDistribution(location = 0.0, scale = 1.0).PDF(2.0)
        self.assertTrue(abs(p/0.06366197 - 1) < 0.01)
    def testinverseCDF1(self):
        p = N.CauchyDistribution(location = 0.0, scale = 1.0).inverseCDF(0.5)[0]
        self.assertTrue(abs(p) < 0.01)
    def testinverseCDF2(self):
        p = N.CauchyDistribution(location = 0.0, scale = 1.0).inverseCDF(0.75)[0]
        self.assertTrue(abs(p/1.0 - 1) < 0.01)
    def testinverseCDF3(self):
        p = N.CauchyDistribution(location = 0.0, scale = 1.0).inverseCDF(0.8524163)[0]
        self.assertTrue(abs(p/2.0 - 1) < 0.01)


class testChiSquare(unittest.TestCase):
    def testCDF0_1(self):
        p = N.ChiSquareDistribution(df = 1).CDF(2.706)
        self.assertTrue(abs(p/0.9 - 1) < 0.01)
    def testCDF0_2(self):
        p = N.ChiSquareDistribution(df = 1).CDF(3.841)
        self.assertTrue(abs(p/0.95 - 1) < 0.01)
    def testCDF0_3(self):
        p = N.ChiSquareDistribution(df = 1).CDF(10.828)
        self.assertTrue(abs(p/0.999 - 1) < 0.01)
    def testCDF10_1(self):
        p = N.ChiSquareDistribution(df = 10).CDF(15.987)
        self.assertTrue(abs(p/0.9 - 1) < 0.01)
    def testCDF10_2(self):
        p = N.ChiSquareDistribution(df = 10).CDF(18.307)
        self.assertTrue(abs(p/0.95 - 1) < 0.01)
    def testCDF10_3(self):
        p = N.ChiSquareDistribution(df = 10).CDF(29.588)
        self.assertTrue(abs(p/0.999 - 1) < 0.01)
    def testPDF(self):
        pass
    def testinverseCDF1(self):
        p = N.ChiSquareDistribution(df = 10).inverseCDF(0.9)[0]
        self.assertTrue(abs(p/15.987 - 1) < 0.01)
    def testinverseCDF2(self):
        p = N.ChiSquareDistribution(df = 10).inverseCDF(0.95)[0]
        self.assertTrue(abs(p/18.307 - 1) < 0.01)
    def testinverseCDF3(self):
        p = N.ChiSquareDistribution(df = 10).inverseCDF(0.999)[0]
        self.assertTrue(abs(p/29.588 - 1) < 0.01)

##class testCosine(unittest.TestCase):
##    def testCDF(self):
##        pass
##    def testPDF(self):
##        pass
##    def testinverseCDF(self):
##        pass
##          
##class testExponential(unittest.TestCase):
##    def testCDF(self):
##        pass
##    def testPDF(self):
##        pass
##    def testinverseCDF(self):
##        pass

class testF(unittest.TestCase):
    def testCDF1(self):
        p = N.FDistribution(df1 = 3, df2 = 5).CDF(1.0)
        self.assertTrue(abs(p/0.535145 - 1) < 0.01)
    def testCDF2(self):
        p = N.FDistribution(df1 = 3, df2 = 5).CDF(2.0)
        self.assertTrue(abs(p/0.767376 - 1) < 0.01)
    def testCDF3(self):
        p = N.FDistribution(df1 = 3, df2 = 5).CDF(3.0)
        self.assertTrue(abs(p/0.866145 - 1) < 0.01)
    def testPDF1(self):
        p = N.FDistribution(df1 = 3, df2 = 5).PDF(1.0)
        self.assertTrue(abs(p/0.361174 - 1) < 0.01)
    def testPDF2(self):
        p = N.FDistribution(df1 = 3, df2 = 5).PDF(2.0)
        self.assertTrue(abs(p/0.1428963 - 1) < 0.01)
    def testPDF3(self):
        p = N.FDistribution(df1 = 3, df2 = 5).PDF(3.0)
        self.assertTrue(abs(p/0.066699 - 1) < 0.01)
    def testinverseCDF1(self):
        p = N.FDistribution(df1 = 3, df2 = 5).inverseCDF(0.535145)[0]
        self.assertTrue(abs(p/1.0 - 1) < 0.01)
    def testinverseCDF2(self):
        p = N.FDistribution(df1 = 3, df2 = 5).inverseCDF(0.767376)[0]
        self.assertTrue(abs(p/2.0 - 1) < 0.01)
    def testinverseCDF3(self):
        p = N.FDistribution(df1 = 3, df2 = 5).inverseCDF(0.866145)[0]
        self.assertTrue(abs(p/3.0 - 1) < 0.01)

class testGamma(unittest.TestCase):
    def testCDF1(self):
        p = N.GammaDistribution(location = 0, scale = 4, shape = 4).CDF(7.0)
        self.assertTrue(abs(p/0.1008103 - 1) < 0.01)
    def testCDF2(self):
        p = N.GammaDistribution(location = 0, scale = 4, shape = 4).CDF(7.5)
        self.assertTrue(abs(p/0.1210543 - 1) < 0.01)
    def testCDF3(self):
        p = N.GammaDistribution(location = 0, scale = 4, shape = 4).CDF(8.0)
        self.assertTrue(abs(p/0.1428765 - 1) < 0.01)
    def testPDF(self):
        pass
    def testinverseCDF1(self):
        p = N.GammaDistribution(location = 0, scale = 4, 
                                shape = 4).inverseCDF(0.1008103)[0]
        self.assertTrue(abs(p/7.0 - 1) < 0.01)
    def testinverseCDF2(self):
        p = N.GammaDistribution(location = 0, scale = 4, 
                                shape = 4).inverseCDF(0.1210543)[0]
        self.assertTrue(abs(p/7.5 - 1) < 0.01)
    def testinverseCDF3(self):
        p = N.GammaDistribution(location = 0, scale = 4, 
                                shape = 4).inverseCDF(0.1428765)[0]
        self.assertTrue(abs(p/8.0 - 1) < 0.01)
##
##class testGumbel(unittest.TestCase):
##    def testCDF(self):
##        pass
##    def testPDF(self):
##        pass
##    def testinverseCDF(self):
##        pass
##      
##class testLogarithmic(unittest.TestCase):
##    def testCDF(self):
##        pass
##    def testPDF(self):
##        pass
##    def testinverseCDF(self):
##        pass
##
##class testLogNormal(unittest.TestCase):
##    def testCDF(self):
##        pass
##    def testPDF(self):
##        pass
##    def testinverseCDF(self):
##        pass
##
##class testNegativeBinomial(unittest.TestCase):
##    def testCDF(self):
##        pass
##    def testPDF(self):
##        pass
##    def testinverseCDF(self):
##        pass

class testGeometric(unittest.TestCase):
    def testCDF1(self):
        p = N.GeometricDistribution(success = 0.4).CDF(1)
        self.assertTrue(abs(p/0.4 - 1) < 0.01)
    def testCDF2(self):
        p = N.GeometricDistribution(success = 0.4).CDF(4)
        self.assertTrue(abs(p/0.8704 - 1) < 0.01)
    def testCDF3(self):
        p = N.GeometricDistribution(success = 0.4).CDF(6)
        self.assertTrue(abs(p/0.953344 - 1) < 0.01)
    def testPDF1(self):
        p = N.GeometricDistribution(success = 0.4).PDF(1)
        self.assertTrue(abs(p/0.4 - 1) < 0.01)
    def testPDF2(self):
        p = N.GeometricDistribution(success = 0.4).PDF(4)
        self.assertTrue(abs(p/0.0864 - 1) < 0.01)
    def testPDF3(self):
        p = N.GeometricDistribution(success = 0.4).PDF(6)
        self.assertTrue(abs(p/0.031104 - 1) < 0.01)
    def testinverseCDF1(self):
        p = N.GeometricDistribution(success = 0.4).inverseCDF(0.4)[0]
        self.assertTrue(abs(p/1.0 - 1) < 0.01)
    def testinverseCDF2(self):
        p = N.GeometricDistribution(success = 0.4).inverseCDF(0.8704)[0]
        self.assertTrue(abs(p/4.0 - 1) < 0.01)
    def testinverseCDF3(self):
        p = N.GeometricDistribution(success = 0.4).inverseCDF(0.953344)[0]
        self.assertTrue(abs(p/6.0 - 1) < 0.01)

class testNormal(unittest.TestCase):
    def testCDF1(self):
        p = N.NormalDistribution().CDF(0)
        self.assertTrue(abs(p/0.5 - 1) < 0.01)
    def testPDF1(self):
        p = N.NormalDistribution().PDF(0)
        self.assertTrue(abs(p/0.3989423 - 1) < 0.01)
    def testinverseCDF1(self):
        p = N.NormalDistribution().inverseCDF(0.5)[0]
        self.assertTrue(abs(p) < 0.01)
  
##class testPareto(unittest.TestCase):
##    def testCDF(self):
##        pass
##    def testPDF(self):
##        pass
##    def testinverseCDF(self):
##        pass

class testPoisson(unittest.TestCase):
    def testCDF5_1(self):
        p = N.PoissonDistribution(expectation = 5).CDF(1)
        self.assertTrue(abs(p/0.04 - 1) < 0.05)
    def testCDF5_2(self):
        p = N.PoissonDistribution(expectation = 5).CDF(10)
        self.assertTrue(abs(p/0.986 - 1) < 0.01)
    def testCDF7_1(self):
        p = N.PoissonDistribution(expectation = 7).CDF(10)
        self.assertTrue(abs(p/0.901 - 1) < 0.01)
    def testCDF7_2(self):
        p = N.PoissonDistribution(expectation = 7).CDF(13)
        self.assertTrue(abs(p/0.987 - 1) < 0.01)
    def testPDF(self):
        pass
    def testinverseCDF5_1(self):
        x = N.PoissonDistribution(expectation = 5).inverseCDF(0.04)[0]
        self.assertTrue(abs(x - 1)/1 < 0.01)
    def testinverseCDF5_2(self):
        x = N.PoissonDistribution(expectation = 5).inverseCDF(0.986)[0]
        self.assertTrue(abs(x - 10)/10 < 0.01)
    def testinverseCDF7_1(self):
        x = N.PoissonDistribution(expectation = 7).inverseCDF(0.901)[0]
        self.assertTrue(abs(x - 10)/10 < 0.01)

##class testSemicircular(unittest.TestCase):
##    def testCDF(self):
##        pass
##    def testPDF(self):
##        pass
##    def testinverseCDF(self):
##        pass
    
class testT(unittest.TestCase):
##    def testCDF(self):
##        pass
##    def testPDF(self):
##        pass
    def testinverseCDF1_1(self):
        x = N.TDistribution(location = 0.0, scale = 1.0, 
                            shape = 2).inverseCDF(0.9)[0]
        self.assertTrue(abs(x/1.886 - 1) < 0.01)
    def testinverseCDF1_2(self):
        x = N.TDistribution(location = 0.0, scale = 1.0, 
                            shape = 2).inverseCDF(0.95)[0]
        self.assertTrue(abs(x/2.920 - 1) <0.01)
    def testinverseCDF1_3(self):
        x = N.TDistribution(location = 0.0, scale = 1.0, 
                            shape = 2).inverseCDF(0.99)[0]
        self.assertTrue(abs(x/6.965 - 1) <0.01)
    def testinverseCDF1_4(self):
        x = N.TDistribution(location = 0.0, scale = 1.0, 
                            shape = 2).inverseCDF(0.999)[0]
        self.assertTrue(abs(x/22.328 - 1) <0.01)
    def testinverseCDF5_1(self):
        x = N.TDistribution(location = 0.0, scale = 1.0, 
                            shape = 5).inverseCDF(0.9)[0]
        self.assertTrue(abs(x/1.476 - 1) < 0.01)
    def testinverseCDF5_2(self):
        x = N.TDistribution(location = 0.0, scale = 1.0, 
                            shape = 5).inverseCDF(0.95)[0]
        self.assertTrue(abs(x/2.015 - 1) <0.01)
    def testinverseCDF5_3(self):
        x = N.TDistribution(location = 0.0, scale = 1.0, 
                            shape = 5).inverseCDF(0.99)[0]
        self.assertTrue(abs(x/3.365 - 1) <0.01)
    def testinverseCDF5_4(self):
        x = N.TDistribution(location = 0.0, scale = 1.0, 
                            shape = 5).inverseCDF(0.999)[0]
        self.assertTrue(abs(x/5.894 - 1) <0.01)
        
    
class testUniform(unittest.TestCase):
    def testCDF1(self):
        p = N.UniformDistribution(location = 1.0, scale = 3.0).CDF(1.5)
        self.assertTrue(abs(p/0.25 - 1) <0.01)
    def testCDF2(self):
        p = N.UniformDistribution(location = 1.0, scale = 3.0).CDF(2.5)
        self.assertTrue(abs(p/0.75 - 1) <0.01)
    def testPDF1(self):
        p = N.UniformDistribution(location = 1.0, scale = 3.0).PDF(1.5)
        self.assertTrue(p == 0.5)
    def testPDF2(self):
        p = N.UniformDistribution(location = 1.0, scale = 3.0).PDF(2.5)
        self.assertTrue(p == 0.5)
    def testinverseCDF1(self):
        p = N.UniformDistribution(location = 1.0, scale = 3.0).inverseCDF(0.25)[0]
        self.assertTrue(abs(p/1.5 - 1) <0.01)
    def testinverseCDF2(self):
        p = N.UniformDistribution(location = 1.0, scale = 3.0).inverseCDF(0.75)[0]
        self.assertTrue(abs(p/2.5 - 1) <0.01)

##class testWeibull(unittest.TestCase):
##    def testCDF(self):
##        pass
##    def testPDF(self):
##        pass
##    def testinverseCDF(self):
##        pass
    
if __name__ == '__main__':
    sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'copads'))
    import StatisticsDistribution as N
    unittest.main()