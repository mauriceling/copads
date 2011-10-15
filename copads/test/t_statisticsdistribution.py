import sys
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'copads'))
import statisticsdistribution as N

class testBeta(unittest.TestCase):
    """
    @see: Ling, MHT. 2009. Compendium of Distributions, I: Beta, Binomial, Chi-
    Square, F, Gamma, Geometric, Poisson, Student's t, and Uniform. The Python 
    Papers Source Codes 1:4
    """
    def testCDF1(self):
        p = N.BetaDistribution(location=0, scale=1,
                p=1, q=2).CDF(1.0)
        self.assertAlmostEqual(p, 1.0000, places=4)
    def testCDF2(self):
        p = N.BetaDistribution(location=0, scale=1,
                p=6, q=2).CDF(1.0)
        self.assertAlmostEqual(p, 1.0000, places=4)

class testBinomial(unittest.TestCase):
    """
    @see: Ling, MHT. 2009. Compendium of Distributions, I: Beta, Binomial, Chi-
    Square, F, Gamma, Geometric, Poisson, Student's t, and Uniform. The Python 
    Papers Source Codes 1:4
    """
    def testCDF1(self):
        p = N.BinomialDistribution(trial=1000,
                success=0.5).CDF(500)
        self.assertAlmostEqual(p, 0.5126125, places=4)
    def testPDF1(self):
        p = N.BinomialDistribution(trial=20,
                success=0.5).PDF(10)
        self.assertAlmostEqual(p, 0.1762, places=4)
    def testPDF2(self):
        p = N.BinomialDistribution(trial=20, success=0.1).PDF(1)
        self.assertAlmostEqual(p, 0.27017, places=4)
    def testPDF3(self):
        p = N.BinomialDistribution(trial=20, success=0.1).PDF(3)
        self.assertAlmostEqual(p, 0.19012, places=4)
    def testPDF4(self):
        p = N.BinomialDistribution(trial=20, success=0.1).PDF(4)
        self.assertAlmostEqual(p, 0.08978, places=4)
        
        
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
    """
    @see: Ling, MHT. 2009. Compendium of Distributions, I: Beta, Binomial, Chi-
    Square, F, Gamma, Geometric, Poisson, Student's t, and Uniform. The Python 
    Papers Source Codes 1:4
    """
    def testCDF0_1(self):
        p = N.ChiSquareDistribution(df=1).CDF(2.706)
        self.assertAlmostEqual(p, 0.9000, places=4)
    def testCDF0_2(self):
        p = N.ChiSquareDistribution(df=1).CDF(3.841)
        self.assertAlmostEqual(p, 0.9500, places=4)
    def testCDF0_3(self):
        p = N.ChiSquareDistribution(df=1).CDF(10.828)
        self.assertAlmostEqual(p, 0.9990, places=4)
    def testCDF10_1(self):
        p = N.ChiSquareDistribution(df=10).CDF(15.987)
        self.assertAlmostEqual(p, 0.9000, places=4)
    def testCDF10_2(self):
        p = N.ChiSquareDistribution(df=10).CDF(18.307)
        self.assertAlmostEqual(p, 0.9500, places=4)
    def testCDF10_3(self):
        p = N.ChiSquareDistribution(df=10).CDF(29.588)
        self.assertAlmostEqual(p, 0.9990, places=4)
    def testinverseCDF1(self):
        p = N.ChiSquareDistribution(df=10).inverseCDF(0.9)[0]
        self.assertAlmostEqual(p, 15.9870, places=2)
    def testinverseCDF2(self):
        p = N.ChiSquareDistribution(df=10).inverseCDF(0.95)[0]
        self.assertAlmostEqual(p, 18.307, places=1)
    def testinverseCDF3(self):
        p = N.ChiSquareDistribution(df=10).inverseCDF(0.999)[0]
        self.assertAlmostEqual(p, 29.588, places=2)
        
        
class testCosine(unittest.TestCase):
    def testCDF1(self):
        p = N.CosineDistribution(location = 0.0, scale = 1.0).CDF(0.0)
        self.assertAlmostEqual(p, 0.5, places=2)
    def testCDF2(self):
        p = N.CosineDistribution(location = 0.0, scale = 1.0).CDF(1.0)
        self.assertAlmostEqual(p, 0.793079, places=4)
    def testCDF3(self):
        p = N.CosineDistribution(location = 0.0, scale = 1.0).CDF(10.0)
        self.assertAlmostEqual(p, 2.00496578, places=4)
    def testinverseCDF1(self):
        p = N.CosineDistribution(location = 0.0,
                                  scale = 1.0).inverseCDF(2.00496578)[0]
        self.assertAlmostEqual(p, 10.0, places=2)
    def testinverseCDF2(self):
        p =  N.CosineDistribution(location = 0.0,
                                  scale = 1.0).inverseCDF(0.5)[0]
        self.assertAlmostEqual(p, 0.0, places=2)
    def testPDF1(self):
        p = N.CosineDistribution(location = 0.0, scale = 1.0).PDF(0.0)
        self.assertAlmostEqual(p, 0.318309, places=4)
    def testPDF2(self):
        p = N.CosineDistribution(location = 0.0, scale = 1.0).PDF(1.0)
        self.assertAlmostEqual(p, 0.245147, places=4)
    def testPDF3(self):
        p = N.CosineDistribution(location = 0.0, scale = 1.0).PDF(10.0)
        self.assertAlmostEqual(p, 0.02561256, places=4)
    def testVariance(self):
        p = N.CosineDistribution(location = 0.0, scale = 1.0).variance()
        self.assertAlmostEqual(p, 1.289868, places=4)
        
##
class testExponential(unittest.TestCase):
    def testCDF1(self):
        p = N.ExponentialDistribution(location = 0.0, scale = 1.0).CDF(0.0)
        self.assertAlmostEqual(p, 0.0, places = 2)
    def testCDF2(self):
        p = N.ExponentialDistribution(location = 0.0, scale = 1.0).CDF(2.0)
        self.assertAlmostEqual(p, 0.86466, places = 4)
    def testCDF3(self):
        p = N.ExponentialDistribution(location = 1.0, scale = 1.0).CDF(0.0)
        self.assertAlmostEqual(p, - 1.7182818, places = 4)
    def testPDF1(self):
        p = N.ExponentialDistribution(location = 0.0, scale = 1.0).PDF(0.0)
        self.assertAlmostEqual(p, 1.0, places = 4)
    def testPDF2(self):
        p = N.ExponentialDistribution(location = 0.0, scale = 1.0).PDF(1.0)
        self.assertAlmostEqual(p, 0.3679, places = 4)
    def testvariance(self):
        p = N.ExponentialDistribution(location = 0.0, scale = 1.0).variance()
        self.assertAlmostEqual(p, 1.0, places = 4)
    def testmean(self):
        p = N.ExponentialDistribution(location = 0.0, scale = 1.0).mean()
        self.assertAlmostEqual(p, 1.0, places = 4)
    def testmedian(self):
        p = N.ExponentialDistribution(location = 0.0, scale = 1.0).median()
        self.assertAlmostEqual(p, 0.30103, places = 4)
        
##
class testF(unittest.TestCase):
    """
    @see: Ling, MHT. 2009. Compendium of Distributions, I: Beta, Binomial, Chi-
    Square, F, Gamma, Geometric, Poisson, Student's t, and Uniform. The Python 
    Papers Source Codes 1:4
    """
    def testCDF1(self):
        p = N.FDistribution(df1=3, df2=5).CDF(1.0)
        self.assertAlmostEqual(p, 0.535145, places=4)
    def testCDF2(self):
        p = N.FDistribution(df1=3, df2=5).CDF(2.0)
        self.assertAlmostEqual(p, 0.767376, places=4)
    def testCDF3(self):
        p = N.FDistribution(df1=3, df2=5).CDF(3.0)
        self.assertAlmostEqual(p, 0.866145, places=4)
    def testPDF1(self):
        p = N.FDistribution(df1=3, df2=5).PDF(1.0)
        self.assertAlmostEqual(p, 0.361174, places=4)
    def testPDF2(self):
        p = N.FDistribution(df1=3, df2=5).PDF(2.0)
        self.assertAlmostEqual(p, 0.1428963, places=4)
    def testPDF3(self):
        p = N.FDistribution(df1=3, df2=5).PDF(3.0)
        self.assertAlmostEqual(p, 0.066699, places=4)
    def testinverseCDF1(self):
        p = N.FDistribution(df1=3,
                df2=5).inverseCDF(0.535145)[0]
        self.assertAlmostEqual(p, 1.0000, places=2)
    def testinverseCDF2(self):
        p = N.FDistribution(df1=3,
                df2=5).inverseCDF(0.767376)[0]
        self.assertAlmostEqual(p, 2.00, places=2)
    def testinverseCDF3(self):
        p = N.FDistribution(df1=3,
                df2=5).inverseCDF(0.866145)[0]
        self.assertAlmostEqual(p, 3.00, places=2)


class testGamma(unittest.TestCase):
    """
    @see: Ling, MHT. 2009. Compendium of Distributions, I: Beta, Binomial, Chi-
    Square, F, Gamma, Geometric, Poisson, Student's t, and Uniform. The Python 
    Papers Source Codes 1:4
    """
    def testCDF1(self):
        p = N.GammaDistribution(location=0, scale=4,
                shape=4).CDF(7.0)
        self.assertAlmostEqual(p, 0.1008103, places=4)
    def testCDF2(self):
        p = N.GammaDistribution(location=0, scale=4,
                shape=4).CDF(7.5)
        self.assertAlmostEqual(p, 0.1210543, places=4)
    def testCDF3(self):
        p = N.GammaDistribution(location=0, scale=4,
                shape=4).CDF(8.0)
        self.assertAlmostEqual(p, 0.1428765, places=4)
    def testinverseCDF1(self):
        p = N.GammaDistribution(location=0, scale=4,
                                shape=4).inverseCDF(0.1008103)[0]
        self.assertAlmostEqual(p, 7.0000, places=4)
    def testinverseCDF2(self):
        p = N.GammaDistribution(location=0, scale=4,
                                shape=4).inverseCDF(0.1210543)[0]
        self.assertAlmostEqual(p, 7.5000, places=4)
    def testinverseCDF3(self):
        p = N.GammaDistribution(location=0, scale=4,
                                shape=4).inverseCDF(0.1428765)[0]
        self.assertAlmostEqual(p, 8.00, places=2)
    def test_kurtosis(self):
        p = N.GammaDistribution(location=0, scale=4,
                                shape=4).kurtosis()
        self.assertAlmostEqual(p, 1.50, places=2)
        
##
##class testGumbel(unittest.TestCase):
##    def testCDF(self):
##        pass
##    def testPDF(self):
##        pass
##    def testinverseCDF(self):
##        pass
##      
class testLogarithmic(unittest.TestCase):
    def testPDF(self):
        p = N.LogarithmicDistribution(shape=0.45).PDF(1.0)
        self.assertAlmostEqual(p, 1.7332, places=4)
    def testCDF(self):
        p = N.LogarithmicDistribution(shape=0.45).CDF(0.0)
        self.assertAlmostEqual(p, 0.0, places=2)
    def testinverseCDF(self):
        p = N.LogarithmicDistribution(shape=0.45).CDF(0.0)
        self.assertAlmostEqual(p,0.0, places=2)
    def testmode(self):
        p = N.LogarithmicDistribution(shape=0.45).mode()
        self.assertAlmostEqual(p, 1.0, places=2)
    def testmean(self):
        p = N.LogarithmicDistribution(shape=0.45).mean()
        self.assertAlmostEqual(p, 3.15124, places=4)

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
    """
    @see: Ling, MHT. 2009. Compendium of Distributions, I: Beta, Binomial, Chi-
    Square, F, Gamma, Geometric, Poisson, Student's t, and Uniform. The Python 
    Papers Source Codes 1:4
    """
    def testCDF1(self):
        p = N.GeometricDistribution(success=0.4).CDF(1)
        self.assertAlmostEqual(p, 0.4000, places=4)
    def testCDF2(self):
        p = N.GeometricDistribution(success=0.4).CDF(4)
        self.assertAlmostEqual(p, 0.8704, places=4)
    def testCDF3(self):
        p = N.GeometricDistribution(success=0.4).CDF(6)
        self.assertAlmostEqual(p, 0.953344, places=4)
    def testPDF1(self):
        p = N.GeometricDistribution(success=0.4).PDF(1)
        self.assertAlmostEqual(p, 0.4000, places=4)
    def testPDF2(self):
        p = N.GeometricDistribution(success=0.4).PDF(4)
        self.assertAlmostEqual(p, 0.0864, places=4)
    def testPDF3(self):
        p = N.GeometricDistribution(success=0.4).PDF(6)
        self.assertAlmostEqual(p, 0.031104, places=4)
    def testinverseCDF1(self):
        p = N.GeometricDistribution(
                success=0.4).inverseCDF(0.4)[0]
        self.assertAlmostEqual(p, 1.0000, places=4)
    def testinverseCDF2(self):
        p = N.GeometricDistribution(
                success=0.4).inverseCDF(0.8704)[0]
        self.assertAlmostEqual(p, 4.0000, places=4)
    def testinverseCDF3(self):
        p = N.GeometricDistribution(
                success=0.4).inverseCDF(0.953344)[0]
        self.assertAlmostEqual(p, 6.0000, places=4)


class testNormal(unittest.TestCase):
    """
    @see: Ling, MHT. 2009. Ten Z-Test Routines from Gopal Kanji's 100 
    Statistical Tests. The Python Papers Source Codes 1:5
    """
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
    """
    @see: Ling, MHT. 2009. Compendium of Distributions, I: Beta, Binomial, Chi-
    Square, F, Gamma, Geometric, Poisson, Student's t, and Uniform. The Python 
    Papers Source Codes 1:4
    """
    def testCDF5_1(self):
        p = N.PoissonDistribution(expectation=5).CDF(1)
        self.assertAlmostEqual(p, 0.04, places=2)
    def testCDF5_2(self):
        p = N.PoissonDistribution(expectation=5).CDF(10)
        self.assertAlmostEqual(p, 0.986, places=3)
    def testCDF7_1(self):
        p = N.PoissonDistribution(expectation=7).CDF(10)
        self.assertAlmostEqual(p, 0.901, places=3)
    def testCDF7_2(self):
        p = N.PoissonDistribution(expectation=7).CDF(13)
        self.assertAlmostEqual(p, 0.987, places=3)
    def testinverseCDF5_1(self):
        x = N.PoissonDistribution(
                expectation=5).inverseCDF(0.04)[0]
        self.assertAlmostEqual(x, 1.000, places=2)
    def testinverseCDF5_2(self):
        x = N.PoissonDistribution(
                expectation=5).inverseCDF(0.986)[0]
        self.assertAlmostEqual(x, 10.000, places=2)
    def testinverseCDF7_1(self):
        x = N.PoissonDistribution(
                expectation=7).inverseCDF(0.901)[0]
        self.assertAlmostEqual(x, 10.000, places=2)

class testSemicircular(unittest.TestCase):
    def testPDF1(self):
        p = N.SemicircularDistribution(location=0.0, scale=1.0).PDF(0.0)
        self.assertAlmostEqual(p, 0.63662, places=4)
    def testPDF2(self):
        p = N.SemicircularDistribution(location=0.0, scale=1.0).PDF(0.5)
        self.assertAlmostEqual(p, 0.55133, places=4)
    def testCDF1(self):
        p = N.SemicircularDistribution(location=0.0, scale=1.0).CDF(0.0)
        self.assertAlmostEqual(p, 0.5, places=4)
    def testCDF2(self):
        p = N.SemicircularDistribution(location=0.0, scale=1.0).CDF(0.5)
        self.assertAlmostEqual(p, 0.804498, places = 4)
    def testinverseCDF(self):
        p = N.SemicircularDistribution(location=0.0,
                                       scale=1.0).inverseCDF(0.5)[0]
        self.assertAlmostEqual(p, 0.0, places = 2)
    
class testT(unittest.TestCase):
    """
    @see: Ling, MHT. 2009. Compendium of Distributions, I: Beta, Binomial, Chi-
    Square, F, Gamma, Geometric, Poisson, Student's t, and Uniform. The Python 
    Papers Source Codes 1:4
    """
    def testinverseCDF1_1(self):
        x = N.TDistribution(location=0.0, scale=1.0,
                            shape=2).inverseCDF(0.9)[0]
        self.assertAlmostEqual(x, 1.886, places=1)
    def testinverseCDF1_2(self):
        x = N.TDistribution(location=0.0, scale=1.0,
                            shape=2).inverseCDF(0.95)[0]
        self.assertAlmostEqual(x, 2.920, places=3)
    def testinverseCDF1_3(self):
        x = N.TDistribution(location=0.0, scale=1.0,
                            shape=2).inverseCDF(0.99)[0]
        self.assertAlmostEqual(x, 6.965, places=1)
    def testinverseCDF1_4(self):
        x = N.TDistribution(location=0.0, scale=1.0,
                            shape=2).inverseCDF(0.999)[0]
        self.assertAlmostEqual(x, 22.328, places=1)
    def testinverseCDF5_1(self):
        x = N.TDistribution(location=0.0, scale=1.0,
                            shape=5).inverseCDF(0.9)[0]
        self.assertAlmostEqual(x, 1.476, places=3)
    def testinverseCDF5_2(self):
        x = N.TDistribution(location=0.0, scale=1.0,
                            shape=5).inverseCDF(0.95)[0]
        self.assertAlmostEqual(x, 2.020, places=2)
    def testinverseCDF5_3(self):
        x = N.TDistribution(location=0.0, scale=1.0,
                            shape=5).inverseCDF(0.99)[0]
        self.assertAlmostEqual(x, 3.365, places=2)
    def testinverseCDF5_4(self):
        x = N.TDistribution(location=0.0, scale=1.0,
                            shape=5).inverseCDF(0.999)[0]
        self.assertAlmostEqual(x, 5.893, places=2)
        
    
class testTriangular(unittest.TestCase):
    def testCDF1(self):
       p = N.TriangularDistribution(2.0, 1.0).CDF(1.0)
       self.assertAlmostEqual(p, 0.5000, places=4)
    def testCDF2(self):
       p = N.TriangularDistribution(2.0, 1.0).CDF(0.8)
       self.assertAlmostEqual(p, 0.3200, places=4)
    def testCDF3(self):
       p = N.TriangularDistribution(4.0, 2.0, -4).CDF(1.0)
       self.assertAlmostEqual(p, 0.5208, places=4)
    def testPDF1(self):
       p = N.TriangularDistribution(2.0, 1.0).PDF(0.08)
       self.assertAlmostEqual(p, 0.08000, places=4)
    def testPDF2(self):
       p = N.TriangularDistribution(4.0, 2.0, -4).PDF(1.0)
       self.assertAlmostEqual(p, 0.20833, places=4)
    def testkurtosis(self):
       p = N.TriangularDistribution(2.0, 1.0).kurtosis()
       self.assertAlmostEqual(p, -0.6, places=4)

class testUniform(unittest.TestCase):
    """
    @see: Ling, MHT. 2009. Compendium of Distributions, I: Beta, Binomial, Chi-
    Square, F, Gamma, Geometric, Poisson, Student's t, and Uniform. The Python 
    Papers Source Codes 1:4
    """
    def testCDF1(self):
        p = N.UniformDistribution(location=1.0,
                scale=3.0).CDF(1.5)
        self.assertTrue(abs(p / 0.25 - 1) < 0.01)
        self.assertAlmostEqual(p, 0.2500, places=4)
    def testCDF2(self):
        p = N.UniformDistribution(location=1.0,
                scale=3.0).CDF(2.5)
        self.assertTrue(abs(p / 0.75 - 1) < 0.01)
        self.assertAlmostEqual(p, 0.7500, places=4)
    def testCDF3(self):
        p = N.UniformDistribution(location=-1.0,
                                  scale=1.0).CDF(0)
        self.assertAlmostEqual(p, 0.5)
    def testPDF1(self):
        p = N.UniformDistribution(location=1.0,
                scale=3.0).PDF()
        self.assertTrue(p == 0.5)
    def testPDF2(self):
        p = N.UniformDistribution(location=1.0,
                scale=3.0).PDF()
        self.assertTrue(p == 0.5)
    def testinverseCDF1(self):
        p = N.UniformDistribution(location=1.0,
                scale=3.0).inverseCDF(0.25)[0]
        self.assertAlmostEqual(p, 1.50, places=1)
    def testinverseCDF2(self):
        p = N.UniformDistribution(location=1.0,
                scale=3.0).inverseCDF(0.75)[0]
        self.assertAlmostEqual(p, 2.50, places=1)
    def test_mean(self):
        p = N.UniformDistribution(location=1,
                    scale=2).mean()
        self.assertAlmostEqual(p, 1.5)

##class testWeibull(unittest.TestCase):
##    def testCDF(self):
##        pass
##    def testPDF(self):
##        pass
##    def testinverseCDF(self):
##        pass
    
if __name__ == '__main__':
    unittest.main()