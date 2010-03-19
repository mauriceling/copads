import sys
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'copads'))
import hypothesis as N
    
class testNormalDistribution(unittest.TestCase):
    
    def testZ1Mean1Variance(self): 
        """Test 1: Z-test for a population mean (variance known)"""
        self.assertAlmostEqual(N.Z1Mean1Variance(pmean = 4.0, smean = 4.6, 
            pvar = 1.0, ssize = 9, confidence = 0.975)[2], 1.8)
        self.assertFalse(N.Z1Mean1Variance(pmean = 4.0, smean = 4.6, 
            pvar = 1.0, ssize = 9, confidence = 0.975)[4])
            
    def testZ2Mean1Variance(self): 
        """Test 2: Z-test for two population means (variances known and equal)
        """
        self.assertAlmostEqual(N.Z2Mean1Variance(smean1 = 1.2, smean2 = 1.7,
            pvar = 1.4405, ssize1 = 9, ssize2 = 16, confidence = 0.975)[2], 
            -0.83304408)
        self.assertFalse(N.Z2Mean1Variance(smean1 = 1.2, smean2 = 1.7,
            pvar = 1.4405, ssize1 = 9, ssize2 = 16, confidence = 0.975)[4])
            
    def testZ2Mean2Variance(self): 
        """Test 3: Z-test for two population means (variances known and 
        unequal)"""
        self.assertAlmostEqual(N.Z2Mean2Variance(smean1 = 80.02, 
            smean2 = 79.98, pvar1 = 0.000576, pvar2 = 0.001089,
            ssize1 = 13, ssize2 = 8, confidence = 0.975)[2], 
            2.977847)
        self.assertTrue(N.Z2Mean2Variance(smean1 = 80.02, 
            smean2 = 79.98, pvar1 = 0.000576, pvar2 = 0.001089,
            ssize1 = 13, ssize2 = 8, confidence = 0.975)[4])
            
    def testZ1Proportion(self): 
        """Test 4: Z-test for a proportion (binomial distribution)"""
        self.assertAlmostEqual(N.Z1Proportion(spro = 0.5, ppro = 0.4, 
            ssize = 100, confidence = 0.975)[2], 2.23606798)
        self.assertTrue(N.Z1Proportion(spro = 0.5, ppro = 0.4, 
            ssize = 100, confidence = 0.975)[4])
            
    def testZ2Proportion(self): 
        """Test 5: Z-test for the equality of two proportions (binomial 
        distribution)"""
        self.assertAlmostEqual(N.Z2Proportion(spro1 = 0.00325, spro2 = 0.0573, 
            ssize1 = 952, ssize2 = 1168, confidence = 0.025)[2], -6.9265418)
        self.assertFalse(N.Z2Proportion(spro1 = 0.00325, spro2 = 0.0573, 
            ssize1 = 952, ssize2 = 1168, confidence = 0.025)[4])
            
    def testZ2Count(self): 
        """Test 6: Z-test for comparing two counts (Poisson distribution)"""
        self.assertAlmostEqual(N.Z2Count(time1 = 22, time2 = 30, count1 = 952,
            count2 = 1168, confidence = 0.975)[2], 2.401630072)
        self.assertTrue(N.Z2Count(time1 = 22, time2 = 30, count1 = 952,
            count2 = 1168, confidence = 0.975)[4])
            
    def testZPearsonCorrelation(self): 
        """Test 13: Z-test of a correlation coefficient"""
        self.assertAlmostEqual(N.ZPearsonCorrelation(sr = 0.75, pr = 0.5, 
            ssize = 24, confidence = 0.95)[2], 1.94140329)
        self.assertTrue(N.ZPearsonCorrelation(sr = 0.75, pr = 0.5, 
            ssize = 24, confidence = 0.95)[4])
            
    def testZ2PearsonCorrelation(self): 
        """Test 14: Z-test for two correlation coefficients"""
        self.assertAlmostEqual(N.Z2PearsonCorrelation(r1 = 0.5, r2 = 0.3, 
            ssize1 = 28, ssize2 = 35, confidence = 0.975)[2], 0.89832268)
        self.assertFalse(N.Z2PearsonCorrelation(r1 = 0.5, r2 = 0.3, 
            ssize1 = 28, ssize2 = 35, confidence = 0.975)[4])
            
    def testZCorrProportion(self): 
        """Test 23: Z-test for correlated proportions"""
        self.assertAlmostEqual(N.ZCorrProportion(ny = 15, yn = 9, 
            ssize = 105, confidence = 0.975)[2], 1.22769962)
        self.assertFalse(N.ZCorrProportion(ny = 15, yn = 9, 
            ssize = 105, confidence = 0.975)[4])
            
    def testSpearmanCorrelation(self): 
        """Test 58: Spearman rank correlation test (paired observations)"""
        self.assertAlmostEqual(N.SpearmanCorrelation(R = 24, ssize = 11, 
            confidence = 0.975)[2], -2.8173019)
        self.assertFalse(N.SpearmanCorrelation(R = 24, ssize = 11, 
            confidence = 0.975)[4])
            

class testTDistribution(unittest.TestCase):
    
    def testt1Mean(self): 
        """Test 7: t-test for a population mean (population variance unknown)"""
        self.assertAlmostEqual(N.t1Mean(smean = 3.1, pmean = 4.0, svar = 1.0,
            ssize = 9, confidence = 0.975)[2], -2.69999999)
        self.assertFalse(N.t1Mean(smean = 3.1, pmean = 4.0, svar = 1.0,
            ssize = 9, confidence = 0.975)[4])
            
    def testt2Mean2EqualVariance(self):
        """Test 8: t-test for two population means (population variance unknown 
        but equal)"""
        self.assertAlmostEqual(N.t2Mean2EqualVariance(smean1 = 31.75, 
            smean2 = 28.67, svar1 = 112.25, svar2 = 66.64, ssize1 = 12, 
            ssize2 = 12, confidence = 0.975)[2], 0.798, places=3)
        self.assertFalse(N.t2Mean2EqualVariance(smean1 = 31.75, 
            smean2 = 28.67, svar1 = 112.25, svar2 = 66.64, ssize1 = 12,
            ssize2 = 12, confidence = 0.975)[4])
    
    def testt2Mean2UnequalVariance(self):
        """Test 9: t-test for two population means (population variance unknown 
        and unequal)"""
        self.assertAlmostEqual(N.t2Mean2UnequalVariance(smean1 = 3166.0, 
            smean2 = 2240.4, svar1 = 6328.67, svar2 = 221661.3, ssize1 = 4, 
            ssize2 = 9, confidence = 0.975)[2], 5.717, places=2)
        self.assertTrue(N.t2Mean2UnequalVariance(smean1 = 3166.0, 
            smean2 = 2240.4, svar1 = 6328.67, svar2 = 221661.3, ssize1 = 4,
            ssize2 = 9, confidence = 0.975)[4])
            
    def testtPaired(self):
        """Test 10: t-test for two population means (method of paired 
        comparisons)"""
        self.assertAlmostEqual(N.tPaired(smean1 = 0.9, smean2 = 1.0, svar = 2.9,
            ssize = 10, confidence=0.975)[2], -0.11, places=2)
        self.assertFalse(N.tPaired(smean1 = 0.9, smean2 = 1.0, svar = 2.9,
            ssize = 10, confidence = 0.975)[4])
            
    def testtRegressionCoefficient(self):
        """Test 11: t-test of a regression coefficient"""
        self.assertAlmostEqual(N.tRegressionCoefficient(variancex = 15.61,
            varianceyx = 92.4, b = 5.029, ssize = 12, confidence = 0.975)[2], 
            0.6232, places=3)
        self.assertFalse(N.tRegressionCoefficient(variancex = 15.61,
            varianceyx = 92.4, b = 5.029, ssize = 12, confidence = 0.975)[4])
            
    def testFVarianceRatio(self):
        """Test 16: F-test for two population variances (variance ratio test)"""
        self.assertAlmostEqual(N.FVarianceRatio(var1 = 0.36, var2 = 0.087, 
            ssize1 = 6, ssize2 = 4, confidence = 0.95)[2], 4.14, places=2)
        self.assertFalse(N.FVarianceRatio(var1 = 0.36, var2 = 0.087,
            ssize1 = 6, ssize2 = 4, confidence = 0.95)[4])

    def testF2CorrelatedObs(self):
        """Test 17: F-test for two population variances 
        with correlated observations)"""
        self.assertAlmostEqual(N.F2CorrelatedObs(var1 = 0.36,
            var2 = 0.087, ssize1 = 6, ssize2 = 6, r = 0.811, 
            confidence = 0.95)[2], 0.796, places = 2)
        self.assertFalse(N.F2CorrelatedObs(var1 = 0.36, var2 = 0.087,
            ssize1 = 6, ssize2 = 6, r = 0.811, confidence = 0.95)[4])
            


    
if __name__ == '__main__':
    unittest.main()
