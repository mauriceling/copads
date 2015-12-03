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
        'Jaccard for set'
        distance = D.Jaccard(o1, t1)
        actual = 0.7143
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testSokal_Michener(self):
        'Sokal and Michener for set'
        distance = D.Sokal_Michener(o1, t1)
        actual = 0.7143
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testMatching(self):
        'Matching for set'
        distance = D.Matching(o1, t1)
        actual = 0.4167
        self.assertAlmostEqual(distance, actual, places=4)
       
    def testDice(self):
        'Dice for set'
        distance = D.Dice(o1, t1)
        actual = 0.8333
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testOchiai(self):
        'Ochiai for set'
        distance = D.Ochiai(o1, t1)
        actual = 0.8333
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testOchiai2(self):
        'Ochiai 2 for set'
        distance = D.Ochiai2(o1, t1)
        actual = 0.0000
        self.assertAlmostEqual(distance, actual, places=4)
    
    def testAnderberg(self):
        'Anderberg for set'
        distance = D.Anderberg(o1, t1)
        actual = 0.55555
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testKulczynski2(self):
        'Kulczynski 2 for set'
        distance = D.Kulczynski2(o1, t1)
        actual = 0.8333
        self.assertAlmostEqual(distance, actual, places=4)    

    def testKulczynski(self):
        'Kulczynski for set'
        distance = D.Kulczynski(o1, t1)
        actual = 2.5000
        self.assertAlmostEqual(distance, actual, places=4) 
        
    def testForbes(self):
        'Forbes for set'
        distance = D.Forbes(o1, t1)
        actual = 0.9722
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testHamann(self):
        'Hamann for set'
        distance = D.Hamann(o1, t1)
        actual = 0.4286
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testSimpson(self):
        'Simpson for set'
        distance = D.Simpson(o1, t1)
        actual = 0.8333
        self.assertAlmostEqual(distance, actual, places=4)  
        
    def testRussel_Rao(self):
        'Russel and Rao for set'
        distance = D.Russel_Rao(o1, t1)
        actual = 0.7143
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testRoger_Tanimoto(self):
        'Roger and Tanimoto for set'
        distance = D.Roger_Tanimoto(o1, t1)
        actual = 0.55555
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testSokal_Sneath(self):
        'Sokal and Sneath for set'
        distance = D.Sokal_Sneath(o1, t1)
        actual = 0.55555
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testSokal_Sneath2(self):
        'Sokal and Snealth 2 for set'
        distance = D.Sokal_Sneath2(o1, t1)
        actual = 0.8333
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testSokal_Sneath3(self):
        'Sokal and Snealth 3 for set'
        distance = D.Sokal_Sneath3(o1, t1)
        actual = 2.5000
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testBuser(self):
        'Buser for set'
        distance = D.Buser(o1, t1)
        actual = 0.7835
        self.assertAlmostEqual(distance, actual, places=4)  
        
    def testFossum(self):
        'Fossum for set'
        distance = D.Fossum(o1, t1)
        actual = 3.9375
        self.assertAlmostEqual(distance, actual, places=4) 
        
    def testYuleQ(self):
        'Yule Q for set'
        distance = D.YuleQ(o1, t1)
        actual = -1.0000
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testYuleY(self):
        'Yule Y for set'
        distance = D.YuleY(o1, t1)
        actual = -1.0000
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testMcconnaughey(self):
        'McConnaughey for set'
        distance = D.Mcconnaughey(o1, t1)
        actual = 0.6667
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testStiles(self):
        'Stiles for set'
        distance = D.Stiles(o1, t1)
        actual = 0.0847
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testPearson(self):
        'Pearson for set'
        distance = D.Pearson(o1, t1)
        actual = -0.1667
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testDennis(self):
        'Dennis for set'
        distance = D.Dennis(o1, t1)
        actual = -0.0630
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testGower_Legendre(self):
        'Gower and Legendre for set'
        distance = D.Gower_Legendre(o1, t1)
        actual = 0.8333
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testTulloss(self):
        'Tulloss for set'
        distance = D.Tulloss(o1, t1)
        actual = 0.8509
        self.assertAlmostEqual(distance, actual, places=4)
        
        
class testList(unittest.TestCase):

    def testJaccard(self):
        'Jaccard for list'
        distance = D.Jaccard(o2, t2, 0, 'List')
        actual = 0.6667
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testSokal_Michener(self):
        'Sokal and Michener for list'
        distance = D.Sokal_Michener(o2, t2, 0, 'List')
        actual = 0.6667
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testMatching(self):
        'Matching for list'
        distance = D.Matching(o2, t2, 0, 'List')
        actual = 0.4000
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testDice(self):
        'Dice for list'
        distance = D.Dice(o2, t2, 0, 'List')
        actual = 0.6667
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testOchiai(self):
        'Ochiai for list'
        distance = D.Ochiai(o2, t2, 0, 'List')
        actual = 0.8000
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testOchiai2(self):
        'Ochiai 2 for list'
        distance = D.Ochiai2(o2, t2, 0, 'List')
        actual = 0.0000
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testAnderberg(self):
        'Anderberg for list'
        distance = D.Anderberg(o2, t2, 0, 'List')
        actual = 0.5000
        self.assertAlmostEqual(distance, actual, places=4)
     
    def testKulczynski2(self):
        'Kulczynski 2 for list'
        distance = D.Kulczynski2(o2, t2, 0, 'List')
        actual = 0.8000
        self.assertAlmostEqual(distance, actual, places=4)
    
    def testKulczynski(self):
        'Kulczynski for list'
        distance = D.Kulczynski(o2, t2, 0, 'List')
        actual = 2.0000
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testForbes(self):
        'Forbes for list'
        distance = D.Forbes(o2, t2, 0, 'List')
        actual = 0.9600
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testHamann(self):
        'Hamann for list'
        distance = D.Hamann(o2, t2, 0, 'List')
        actual = 0.3333
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testSimpson(self):
        'Simpson for list'
        distance = D.Simpson(o2, t2, 0, 'List')
        actual = 0.8000
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testRussel_Rao(self):
        'Russel and Rao for list'
        distance = D.Russel_Rao(o2, t2, 0, 'List')
        actual = 0.6667
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testRoger_Tanimoto(self):
        'Roger and Tanimoto for list'
        distance = D.Roger_Tanimoto(o2, t2, 0, 'List')
        actual = 0.5000
        self.assertAlmostEqual(distance, actual, places=4)
    
    def testSokal_Sneath(self):
        'Sokal and Sneath for list'
        distance = D.Sokal_Sneath(o2, t2, 0, 'List')
        actual = 0.5000
        self.assertAlmostEqual(distance, actual, places=4)
    
    def testSokal_Sneath2(self):
        'Sokal and Sneath 2 for list'
        distance = D.Sokal_Sneath2(o2, t2, 0, 'List')
        actual = 0.8000
        self.assertAlmostEqual(distance, actual, places=4)  

    def testSokal_Sneath3(self):
        'Sokal and Sneath 3 for list'
        distance = D.Sokal_Sneath3(o2, t2, 0, 'List')
        actual = 2.0000
        self.assertAlmostEqual(distance, actual, places=4)  
        
    def testBuser(self):
        'Buser for list'
        distance = D.Buser(o2, t2, 0, 'List')
        actual = 0.7500
        self.assertAlmostEqual(distance, actual, places=4)  
        
    def testFossum(self):
        'Fossum for list'
        distance = D.Fossum(o2, t2, 0, 'List')
        actual = 2.9400
        self.assertAlmostEqual(distance, actual, places=4)
    
    def testYuleQ(self):
        'Yule Q for list'
        distance = D.YuleQ(o2, t2, 0, 'List')
        actual = -1.000
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testYuleY(self):
        'Yule Y for list'
        distance = D.YuleY(o2, t2, 0, 'List')
        actual = -1.000
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testMcconnaughey(self):
        'McConnaughey for list'
        distance = D.Mcconnaughey(o2, t2, 0, 'List')
        actual = 0.6000
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testStiles(self):
        'Stiles for list'
        distance = D.Stiles(o2, t2, 0, 'List')
        actual = -0.0177
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testPearson(self):
        'Pearson for list'
        distance = D.Pearson(o2, t2, 0, 'List')
        actual = -0.2000
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testDennis(self):
        'Dennis for list'
        distance = D.Dennis(o2, t2, 0, 'List')
        actual = -0.0816
        self.assertAlmostEqual(distance, actual, places=4)
    
    def testGower_Legendre(self):
        'Gower and Legendre for list'
        distance = D.Gower_Legendre(o2, t2, 0, 'List')
        actual = 0.8000
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testTulloss(self):
        'Tulloss for list'
        distance = D.Tulloss(o2, t2, 0, 'List')
        actual = 0.8211
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testHamming2(self):
        'Hamming for list (Test 1)'
        distance = D.Hamming(o2, t2)
        actual = 2
        self.assertEqual(distance, actual)
        
    def testHamming3(self):
        'Hamming for list (Test 2)'
        distance = D.Hamming(o3, t3)
        actual = 2
        self.assertEqual(distance, actual)
    
    def testEuclidean2(self):
        'Euclidean for list (Test 1)'
        distance = D.Euclidean(o2, t2)
        actual = 1.4142
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testEuclidean3(self):
        'Euclidean for list (Test 2)'
        distance = D.Euclidean(o3, t3)
        actual = 2.2361
        self.assertAlmostEqual(distance, actual, places=4)
     
    def testMinkowski2(self):
        'Minkowski for list (Test 1)'
        distance = D.Minkowski(o2, t2)
        actual = 1.2599
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testMinkowski3(self):
        'Minkowski for list (Test 2)'
        distance = D.Minkowski(o3, t3)
        actual = 2.0801
        self.assertAlmostEqual(distance, actual, places=4)    
     
    def testManhattan2(self):
        'Manhattan for list (Test 1)'
        distance = D.Manhattan(o2, t2)
        actual = 2.0
        self.assertAlmostEqual(distance, actual, places=4)   

    def testManhattan3(self):
        'Manhattan for list (Test 2)'
        distance = D.Manhattan(o3, t3)
        actual = 3.0
        self.assertAlmostEqual(distance, actual, places=4) 
        
    def testCanberra2(self):
        'Canberra for list (Test 1)'
        distance = D.Canberra(o2, t2)
        actual = 2.0
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testCanberra3(self):
        'Canberra for list (Test 2)'
        distance = D.Canberra(o3, t3)
        actual = 0.3429
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testBray_Curtis2(self):
        'Bray Curtis for list (Test 1)'
        distance = D.Bray_Curtis(o2, t2)
        actual = 0.8000
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testBray_Curtis3(self):
        'Bray Curtis for list (Test 2)'
        distance = D.Bray_Curtis(o3, t3)
        actual = 0.9474
        self.assertAlmostEqual(distance, actual, places=4)   
        
    def testCosine2(self):
        'Cosine for list (Test 1)'
        distance = D.Cosine(o2, t2)
        actual = 0.8000
        self.assertAlmostEqual(distance, actual, places=4)
    
    def testCosine3(self):
        'Cosine for list (Test 2)'
        distance = D.Cosine(o3, t3)
        actual = 0.9873
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testTanimoto2(self):
        'Tanimoto for list (Test 1)'
        distance = D.Tanimoto(o2, t2)
        actual = 0.6667
        self.assertAlmostEqual(distance, actual, places=4)
        
    def testTanimoto(self):
        'Tanimoto for list (Test 2)'
        distance = D.Tanimoto(o3, t3)
        actual = 0.9738
        self.assertAlmostEqual(distance, actual, places=4)  


if __name__ == '__main__':
    unittest.main()