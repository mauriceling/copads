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
    
    def testtPearsonCorrelation(self):
        """Test 12: t-test of a correlation coefficient"""
        self.assertAlmostEqual(N.tPearsonCorrelation(r = 0.32, ssize = 18,
            confidence = 0.95)[2], 1.35, places=2)
        self.assertFalse(N.tPearsonCorrelation(r = 0.32, ssize = 18,
            confidence = 0.95)[4])
    
    def testZPearsonCorrelation(self):
        """Test 13: Z-test of a correlation coefficient"""
        self.assertAlmostEqual(N.ZPearsonCorrelation(sr = 0.75, pr = 0.50, 
            ssize = 24, confidence = 0.90)[2], 1.94, places = 2)
        self.assertTrue(N.ZPearsonCorrelation(sr = 0.75, pr = 0.50,
            ssize = 24, confidence = 0.90)[4])
            
    def testZ2PearsonCorrelation(self):
        """Test 14: Z-test for two correlation coefficients"""
        self.assertAlmostEqual(N.Z2PearsonCorrelation(r1 = 0.50, r2 = 0.30,
        ssize1 = 28, ssize2 = 35, confidence =0.95)[2], 0.8985, places = 3)
        self.assertFalse(N.Z2PearsonCorrelation(r1 = 0.50, r2 = 0.30,
        ssize1 = 28, ssize2 = 35, confidence =0.95)[4])
        
    def testChiSquarePopVar(self):
        """Test 15: Chi-square test for a population variance"""
        self.assertAlmostEqual(N.ChiSquarePopVar(values = (70, 71, 71, 69, 69, 
            72, 72, 68, 68, 67, 67, 73, 73, 74, 74, 66, 66, 65, 65,
            75, 75, 76, 76, 64, 64), ssize = 25, pv = 9, 
            confidence = 0.95)[2], 40.4, places = 1)
        self.assertTrue(N.ChiSquarePopVar(values = (70, 71, 71, 69, 69, 
            72, 72, 68, 68, 67, 67, 73, 73, 74, 74, 66, 66, 65, 65, 75, 75, 76,
            76, 64, 64), ssize = 25, pv = 9, confidence = 0.95)[4])
    
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
            
    # def testFishercumulant(self):
        # """Test 20: Fisher's cumulant test for normality of a population"""
        # self.assertAlmostEqual(N.Fishercumulant(m1 = 151, m2 = 805, m3 = 1837, 
            # m4 = 10753, ssize = 190, confidence = 0.95)[2], 0.449, places = 2)
        # self.assertFalse(N.Fishercumulant(m1 = 151, m2 = 805, m3 = 1837, 
            # m4 = 10753, ssize = 190, confidence = 0.95)[4])
            
    # def testDixonTest(self):
        # """Test 21: Dixon's test for outliers"""
        # self.assertAlmostEqual(N.DixonTest(values = (326, 177, 176, 157), 
            # n = 4, confidence = 0.95)[2], 0.882, places = 2)
        # self.assertFalse(N.DixonTest(values = (326, 177, 176, 157), 
            # n = 4, confidence = 0.95)[4])
            
    # def testFTestAnalysisofVar(self):
        # """Test 22: F-test for K population means (analysis of variance)"""
        # self.assertAlmostEqual(N.FTestAnalysisofVar(s = ((5, 4, 3),
            # (5, 5, 4, 4, 3, 3), (4, 6, 8, 10)), k = 3,
            # confidence = 0.95)[2], 0.002433, places = 4)
        # self.assertTrue(N.FTestAnalysisofVar(s = ((5, 4, 3),
            # (5, 5, 4, 4, 3, 3), (4, 6, 8, 10)), k = 3, confidence = 0.95)[4])
            
    def testZCorrProportion(self):
        """Test 23: Z-test for correlated proportions"""
        self.assertAlmostEqual(N.ZCorrProportion(ssize = 105, ny = 15,
        yn = 9, confidence = 0.95)[2], 1.23, places = 1)
        self.assertFalse(N.ZCorrProportion(ssize = 105, ny = 15,
        yn = 9, confidence = 0.95)[4])
        
    def testChisq2Variance(self):
        """Test 24: Chi-square test for an assumed population variance"""
        self.assertAlmostEqual(N.Chisq2Variance(ssize = 25, svar = 12, 
        pvar = 9, confidence = 0.95)[2], 32)
        self.assertFalse(N.Chisq2Variance(ssize = 25, svar = 12, 
        pvar = 9, confidence = 0.95)[4])
        
    def testF2Count(self):
        """Test 25: F-test for two counts (Poisson distribution)"""
        self.assertAlmostEqual(N.F2Count(count1 = 13, count2 = 3,
            confidence = 0.95)[2], 3.25)
        self.assertTrue(N.F2Count(count1= 13, count2 = 3, 
            confidence = 0.95)[4])
            
    def testChisqFit(self):
        """Test 37: Chi-square test for goodness of fit"""
        self.assertAlmostEqual(N.ChisqFit(observed = (25, 17, 15, 23, 24, 16), 
        expected = (20, 20, 20, 20, 20, 20), confidence = 0.95)[2], 5.0)
        self.assertFalse(N.ChisqFit(observed = (25, 17, 15, 23, 24, 16), 
        expected = (20, 20, 20, 20, 20, 20), confidence = 0.95)[4])
            
    def testtx2testofKcounts(self):
        """Test 38: The x2-test for compatibility of K counts"""
        self.assertAlmostEqual(N.tx2testofKcounts(T = (1, 1, 1, 1),
            V = (5, 12, 18, 19), confidence = 0.95)[2], 9.259, places = 2)
        self.assertTrue(N.tx2testofKcounts(T = (1, 1, 1, 1),
            V = (5, 12, 18, 19), confidence = 0.95)[4])
    
    def testChisq2x2(self):
        """Test 40: Chi-square test for consistency in 2x2 table"""
        self.assertAlmostEqual(N.Chisq2x2(s1 = (15, 85), s2 = (4, 77),
            ssize = 180, confidence = 0.95)[2], 4.79, places = 1)
        self.assertTrue(N.Chisq2x2(s1 = (15, 85), s2 = (4, 77), ssize = 180, 
            confidence = 0.95),[4])
            
    def testChisquareKx2table(self):
        """Test 41: The x2-test for consistency in a K x 2 table"""
        self.assertAlmostEqual(N.ChisquareKx2table(c1 = (3, 4, 5),
            c2 = (7, 2, 4), k = 3, confidence = 0.95)[2], 2.344, places = 2)
        self.assertFalse(N.ChisquareKx2table(c1 = (3, 4, 5),
            c2 = (7, 2, 4), k = 3, confidence = 0.95)[4])
            
    def testChisquare2xKtable(self):
        """Test 43: The x2-test for consistency in a 2 x K table"""
        self.assertAlmostEqual(N.Chisquare2xKtable(s1 = (50, 47, 56),
            s2 = (5, 14, 8), k = 3, confidence = 0.95)[2], 4.84, places = 2)
        self.assertFalse(N.Chisquare2xKtable(s1 = (50, 47, 56),
            s2 = (5, 14, 8), k = 3, confidence = 0.95)[4])
            
    # def testChisquarePxQ(self):
        # """Test 44: The x2-test for independence in a p x q table"""
        # self.assertAlmostEqual(N.ChisquarePxQ(d = ((32, 13), (14, 22), (6, 9)),
            # confidence = 0.95)[2], 10.67, places = 2)
        # self.assertTrue(N.ChisquarePxQ(d = ((32, 13), (14, 22), (6, 9)),
            # confidence = 0.95)[4])
    
    # def testt2MediansPairedObs(self):
        # """Test 46: The sign test for two medians (paired observations)"""
        # self.assertAlmostEqual(N.t2MediansPairedObs(x = (0.19, 0.22, 0.18, 0.17, 
            # 1.20, 0.14, 0.09, 0.13, 0.26, 0.66), y = (0.21, 0.27, 0.15, 
            # 0.18, 0.40, 0.08, 0.14, 0.28, 0.30, 0.68), confidence = 0.90)[2], 3)
        # self.assertFalse(N.t2MediansPairedObs(x = (0.19, 0.22, 0.18, 0.17, 
            # 1.20, 0.14, 0.09, 0.13, 0.26, 0.66), y = (0.21, 0.27, 0.15, 
            # 0.18, 0.40, 0.08, 0.14, 0.28, 0.30, 0.68), confidence = 0.90)[4])
    
    def testMedianTestfor2Pop(self):
        """Test 50: The median test of two populations"""
        self.assertAlmostEqual(N.MedianTestfor2Pop(s1 = (9, 6), 
            s2 = (6, 9), confidence = 0.95)[2], 0.53, places = 1)
        self.assertFalse(N.MedianTestfor2Pop(s1 = (9, 6), s2 = (6, 9),
            confidence = 0.95)[4])
    
    def testZtestLogOddsRatio(self):
        """Test 84: Z-test for comparing sequential contingencies acoss two 
        groups using the 'log odds ratio' """
        self.assertAlmostEqual(N.ZtestLogOddsRatio(group1 = (76, 79, 100, 200), 
            group2 = (80, 43, 63, 39), confidence = 0.95)[2], 1.493, places=3)
        self.assertFalse(N.ZtestLogOddsRatio(group1 = (76, 79, 100, 200), 
            group2 = (80, 43, 63, 39), confidence = 0.95)[4])
            
if __name__ == '__main__':
    unittest.main()