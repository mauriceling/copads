import sys
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'copads'))
import objectdistance as D

# for set comparison
# 5 elements in both
# 1 element in test
# 1 element in original
o1 = ['C', 'D', 'E', 'F', 'G', 'H']
t1 = ['B', 'E', 'D', 'F', 'G', 'H']

# for list comparison
# 4 elements in both
# 1 element in test
# 1 element in original
o2 = [1, 1, 1, 0, 1, 1]
t2 = [1, 1, 0, 1, 1, 1]

# for list comparison in interval/ratio measures
o3 = [1.0, 2.0, 3.0, 6.0, 8.0, 9.0]
t3 = [1.0, 2.0, 4.0, 4.0, 8.0, 9.0]


class testSet(unittest.TestCase):
    def testJaccard(self):
        distance = D.Jaccard(o1, t1)
        actual = 0.7143
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testSokal_Michener(self):
        distance = D.Sokal_Michener(o1, t1)
        actual = 0.7143
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testMatching(self):
        distance = D.Matching(o1, t1)
        actual = 0.4167
        self.assertAlmostEqual(distance, actual, places=4)
       
    def testDice(self):
        distance = D.Dice(o1, t1)
        actual = 0.8333
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testOchiai(self):
        distance = D.Ochiai(o1, t1)
        actual = 0.8333
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testOchiai2(self):
        distance = D.Ochiai2(o1, t1)
        actual = 0.0000
        self.assertAlmostEqual(distance, actual, places=4)
    
    def testAnderberg(self):
        distance = D.Anderberg(o1, t1)
        actual = 0.55555
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testKulczynski2(self):
        distance = D.Kulczynski2(o1, t1)
        actual = 0.8333
        self.assertAlmostEqual(distance, actual, places=4)    

    def testKulczynski(self):
        distance = D.Kulczynski(o1, t1)
        actual = 2.5000
        self.assertAlmostEqual(distance, actual, places=4) 
        
    def testForbes(self):
        distance = D.Forbes(o1, t1)
        actual = 0.9722
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testHamann(self):
        distance = D.Hamann(o1, t1)
        actual = 0.4286
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testSimpson(self):
        distance = D.Simpson(o1, t1)
        actual = 0.8333
        self.assertAlmostEqual(distance, actual, places=4)  
        
    def testRussel_Rao(self):
        distance = D.Russel_Rao(o1, t1)
        actual = 0.7143
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testRoger_Tanimoto(self):
        distance = D.Roger_Tanimoto(o1, t1)
        actual = 0.55555
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testSokal_Sneath(self):
        distance = D.Sokal_Sneath(o1, t1)
        actual = 0.55555
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testSokal_Sneath2(self):
        distance = D.Sokal_Sneath2(o1, t1)
        actual = 0.8333
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testSokal_Sneath3(self):
        distance = D.Sokal_Sneath3(o1, t1)
        actual = 2.5000
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testBuser(self):
        distance = D.Buser(o1, t1)
        actual = 0.7835
        self.assertAlmostEqual(distance, actual, places=4)  
        
    def testFossum(self):
        distance = D.Fossum(o1, t1)
        actual = 3.9375
        self.assertAlmostEqual(distance, actual, places=4) 
        
    def testYuleQ(self):
        distance = D.YuleQ(o1, t1)
        actual = -1.0000
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testYuleY(self):
        distance = D.YuleY(o1, t1)
        actual = -1.0000
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testMcconnaughey(self):
        distance = D.Mcconnaughey(o1, t1)
        actual = 0.6667
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testStiles(self):
        distance = D.Stiles(o1, t1)
        actual = 0.0847
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testPearson(self):
        distance = D.Pearson(o1, t1)
        actual = -0.1667
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testDennis(self):
        distance = D.Dennis(o1, t1)
        actual = -0.0630
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testGower_Legendre(self):
        distance = D.Gower_Legendre(o1, t1)
        actual = 0.8333
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testTulloss(self):
        distance = D.Tulloss(o1, t1)
        actual = 0.8509
        self.assertAlmostEqual(distance, actual, places=4)
        
        
class testList(unittest.TestCase):

    def testJaccard(self):
        distance = D.Jaccard(o2, t2, 0, 'List')
        actual = 0.6667
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testSokal_Michener(self):
        distance = D.Sokal_Michener(o2, t2, 0, 'List')
        actual = 0.6667
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testMatching(self):
        distance = D.Matching(o2, t2, 0, 'List')
        actual = 0.4000
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testDice(self):
        distance = D.Dice(o2, t2, 0, 'List')
        actual = 0.6667
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testOchiai(self):
        distance = D.Ochiai(o2, t2, 0, 'List')
        actual = 0.8000
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testOchiai2(self):
        distance = D.Ochiai2(o2, t2, 0, 'List')
        actual = 0.0000
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testAnderberg(self):
        distance = D.Anderberg(o2, t2, 0, 'List')
        actual = 0.5000
        self.assertAlmostEqual(distance, actual, places=4)
     
    def testKulczynski2(self):
        distance = D.Kulczynski2(o2, t2, 0, 'List')
        actual = 0.8000
        self.assertAlmostEqual(distance, actual, places=4)
    
    def testKulczynski(self):
        distance = D.Kulczynski(o2, t2, 0, 'List')
        actual = 2.0000
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testForbes(self):
        distance = D.Forbes(o2, t2, 0, 'List')
        actual = 0.9600
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testHamann(self):
        distance = D.Hamann(o2, t2, 0, 'List')
        actual = 0.3333
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testSimpson(self):
        distance = D.Simpson(o2, t2, 0, 'List')
        actual = 0.8000
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testRussel_Rao(self):
        distance = D.Russel_Rao(o2, t2, 0, 'List')
        actual = 0.6667
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testRoger_Tanimoto(self):
        distance = D.Roger_Tanimoto(o2, t2, 0, 'List')
        actual = 0.5000
        self.assertAlmostEqual(distance, actual, places=4)
    
    def testSokal_Sneath(self):
        distance = D.Sokal_Sneath(o2, t2, 0, 'List')
        actual = 0.5000
        self.assertAlmostEqual(distance, actual, places=4)
    
    def testSokal_Sneath2(self):
        distance = D.Sokal_Sneath2(o2, t2, 0, 'List')
        actual = 0.8000
        self.assertAlmostEqual(distance, actual, places=4)  

    def testSokal_Sneath3(self):
        distance = D.Sokal_Sneath3(o2, t2, 0, 'List')
        actual = 2.0000
        self.assertAlmostEqual(distance, actual, places=4)  
        
    def testBuser(self):
        distance = D.Buser(o2, t2, 0, 'List')
        actual = 0.7500
        self.assertAlmostEqual(distance, actual, places=4)  
        
    def testFossum(self):
        distance = D.Fossum(o2, t2, 0, 'List')
        actual = 2.9400
        self.assertAlmostEqual(distance, actual, places=4)
    
    def testYuleQ(self):
        distance = D.YuleQ(o2, t2, 0, 'List')
        actual = -1.000
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testYuleY(self):
        distance = D.YuleY(o2, t2, 0, 'List')
        actual = -1.000
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testMcconnaughey(self):
        distance = D.Mcconnaughey(o2, t2, 0, 'List')
        actual = 0.6000
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testStiles(self):
        distance = D.Stiles(o2, t2, 0, 'List')
        actual = -0.0177
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testPearson(self):
        distance = D.Pearson(o2, t2, 0, 'List')
        actual = -0.2000
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testDennis(self):
        distance = D.Dennis(o2, t2, 0, 'List')
        actual = -0.0816
        self.assertAlmostEqual(distance, actual, places=4)
    
    def testGower_Legendre(self):
        distance = D.Gower_Legendre(o2, t2, 0, 'List')
        actual = 0.8000
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testTulloss(self):
        distance = D.Tulloss(o2, t2, 0, 'List')
        actual = 0.8211
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testHamming2(self):
        distance = D.Hamming(o2, t2)
        actual = 2
        self.assertEqual(distance, actual)
        
    def testHamming3(self):
        distance = D.Hamming(o3, t3)
        actual = 2
        self.assertEqual(distance, actual)
    
    def testEuclidean2(self):
        distance = D.Euclidean(o2, t2)
        actual = 1.4142
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testEuclidean3(self):
        distance = D.Euclidean(o3, t3)
        actual = 2.2361
        self.assertAlmostEqual(distance, actual, places=4)
     
    def testMinkowski2(self):
        distance = D.Minkowski(o2, t2)
        actual = 1.2599
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testMinkowski3(self):
        distance = D.Minkowski(o3, t3)
        actual = 2.0801
        self.assertAlmostEqual(distance, actual, places=4)    
     
    def testManhattan2(self):
        distance = D.Manhattan(o2, t2)
        actual = 2.0
        self.assertAlmostEqual(distance, actual, places=4)   

    def testManhattan3(self):
        distance = D.Manhattan(o3, t3)
        actual = 3.0
        self.assertAlmostEqual(distance, actual, places=4) 
        
    def testCanberra2(self):
        distance = D.Canberra(o2, t2)
        actual = 2.0
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testCanberra3(self):
        distance = D.Canberra(o3, t3)
        actual = 0.3429
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testBray_Curtis2(self):
        distance = D.Bray_Curtis(o2, t2)
        actual = 0.8000
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testBray_Curtis3(self):
        distance = D.Bray_Curtis(o3, t3)
        actual = 0.9474
        self.assertAlmostEqual(distance, actual, places=4)   
        
    def testCosine2(self):
        distance = D.Cosine(o2, t2)
        actual = 0.8000
        self.assertAlmostEqual(distance, actual, places=4)
    
    def testCosine3(self):
        distance = D.Cosine(o3, t3)
        actual = 0.9873
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testTanimoto2(self):
        distance = D.Tanimoto(o2, t2)
        actual = 0.6667
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testTanimoto(self):
        distance = D.Tanimoto(o3, t3)
        actual = 0.9738
        self.assertAlmostEqual(distance, actual, places=4) 


if __name__ == '__main__':
    unittest.main()