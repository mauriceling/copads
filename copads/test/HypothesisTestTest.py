import sys
import os
import unittest


class testHypothesisTest(unittest.TestCase):
    
    def testZ1Mean1Variance(self): 
        """Test 1: Z-test for a population mean (variance known)"""
        self.assertAlmostEqual(N.Z1Mean1Variance(pmean = 4.0, smean = 4.6, 
            pvar = 1.0, ssize = 9, confidence = 0.975)[1], 1.8)
        self.assertFalse(N.Z1Mean1Variance(pmean = 4.0, smean = 4.6, 
            pvar = 1.0, ssize = 9, confidence = 0.975)[0])
            
    def testZ2Mean1Variance(self): 
        """Test 2: Z-test for two population means (variances known and equal)
        """
        self.assertAlmostEqual(N.Z2Mean1Variance(smean1 = 1.2, smean2 = 1.7,
            pvar = 1.4405, ssize1 = 9, ssize2 = 16, confidence = 0.975)[1], 
            -0.83304408)
        self.assertFalse(N.Z2Mean1Variance(smean1 = 1.2, smean2 = 1.7,
            pvar = 1.4405, ssize1 = 9, ssize2 = 16, confidence = 0.975)[0])
            
    def testZ2Mean2Variance(self): 
        """Test 3: Z-test for two population means (variances known and 
        unequal)"""
        self.assertAlmostEqual(N.Z2Mean2Variance(smean1 = 80.02, 
            smean2 = 79.98, pvar1 = 0.000576, pvar2 = 0.001089,
            ssize1 = 13, ssize2 = 8, confidence = 0.975)[1], 
            2.977847)
        self.assertTrue(N.Z2Mean2Variance(smean1 = 80.02, 
            smean2 = 79.98, pvar1 = 0.000576, pvar2 = 0.001089,
            ssize1 = 13, ssize2 = 8, confidence = 0.975)[0])
            
    def testZ1Proportion(self): 
        """Test 4: Z-test for a proportion (binomial distribution)"""
        self.assertAlmostEqual(N.Z1Proportion(spro = 0.5, ppro = 0.4, 
            ssize = 100, confidence = 0.975)[1], 2.23606798)
        self.assertTrue(N.Z1Proportion(spro = 0.5, ppro = 0.4, 
            ssize = 100, confidence = 0.975)[0])
            
    def testZ2Proportion(self): 
        """
        Test 5: Z-test for the equality of two proportions (binomial 
        distribution)"""
        self.assertAlmostEqual(N.Z2Proportion(spro1 = 0.00325, spro2 = 0.0573, 
            ssize1 = 952, ssize2 = 1168, confidence = 0.025)[1], -6.9265418)
        self.assertFalse(N.Z2Proportion(spro1 = 0.00325, spro2 = 0.0573, 
            ssize1 = 952, ssize2 = 1168, confidence = 0.025)[0])
            
if __name__ == '__main__':
    sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'src'))
    import HypothesisTest as N
    unittest.main()