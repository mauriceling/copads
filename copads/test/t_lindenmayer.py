import sys
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'src'))
import lindenmayer as N

class testReplacement(unittest.TestCase):
    def setUp(self):
        s = N.lindenmayer(1)
        r = [['A', 'BAC']]
        s.add_rules(r)
        axiom = 'A'
        self.result = []
        for i in range(10):
            axiom = s.apply_rules(axiom)
            self.result.append(axiom)
        self.answer = ['BAC',
                       'BBACC',
                       'BBBACCC',
                       'BBBBACCCC',
                       'BBBBBACCCCC',
                       'BBBBBBACCCCCC',
                       'BBBBBBBACCCCCCC',
                       'BBBBBBBBACCCCCCCC',
                       'BBBBBBBBBACCCCCCCCC',
                       'BBBBBBBBBBACCCCCCCCCC']
    def testGeneration(self):
        self.assertEqual(self.result, self.answer)

class testReplacementPriority(unittest.TestCase):
    def setUp(self):
        s = N.lindenmayer(1)
        r = [['A', 'BAC', 1],
             ['B', 'BC', 2]]
        s.add_rules(r)
        axiom = 'A'
        self.result = []
        for i in range(8):
            axiom = s.apply_rules(axiom)
            self.result.append(axiom)
        self.answer = ['BCAC',
                       'BCCBCACC',
                       'BCCCBCCBCACCC',
                       'BCCCCBCCCBCCBCACCCC',
                       'BCCCCCBCCCCBCCCBCCBCACCCCC',
                       'BCCCCCCBCCCCCBCCCCBCCCBCCBCACCCCCC',
                       'BCCCCCCCBCCCCCCBCCCCCBCCCCBCCCBCCBCACCCCCCC',
                       'BCCCCCCCCBCCCCCCCBCCCCCCBCCCCCBCCCCBCCCBCCBCACCCCCCCC']
    def testGeneration(self):
        self.assertEqual(self.result, self.answer)

class testReplacementNoPriority(unittest.TestCase):
    def setUp(self):
        s = N.lindenmayer(1)
        r = [['A', 'BAC'],
             ['B', 'BC']]
        s.add_rules(r)
        axiom = 'A'
        self.result = []
        for i in range(8):
            axiom = s.apply_rules(axiom)
            self.result.append(axiom)
        self.answer = ['BAC',
                       'BCBACC',
                       'BCCBCBACCC',
                       'BCCCBCCBCBACCCC',
                       'BCCCCBCCCBCCBCBACCCCC',
                       'BCCCCCBCCCCBCCCBCCBCBACCCCCC',
                       'BCCCCCCBCCCCCBCCCCBCCCBCCBCBACCCCCCC',
                       'BCCCCCCCBCCCCCCBCCCCCBCCCCBCCCBCCBCBACCCCCCCC']
    def testGeneration(self):
        self.assertEqual(self.result, self.answer)

class testReplacement2(unittest.TestCase):
    def setUp(self):
        s = N.lindenmayer(2)
        r = [['AA', 'BBAAC'],
             ['AB', 'ABC'],
             ['AC', 'BCC']]
        s.add_rules(r)
        axiom = 'AA'
        self.result = []
        for i in range(8):
            axiom = s.apply_rules(axiom)
            self.result.append(axiom)
        self.answer = ['BBAAC',
                       'BBBBAACC',
                       'BBBBBBAACCC',
                       'BBBBBBBBAACCCC',
                       'BBBBBBBBBBAACCCCC',
                       'BBBBBBBBBBBBAACCCCCC',
                       'BBBBBBBBBBBBBBAACCCCCCC',
                       'BBBBBBBBBBBBBBBBAACCCCCCCC']
    def testGeneration(self):
        self.assertEqual(self.result, self.answer)

if __name__ == '__main__':
    unittest.main()