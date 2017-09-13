import sys
import os
import unittest
import re

sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'copads'))
import lindenmayer as N

class testReplacement(unittest.TestCase):
    '''
    Test for single replacement rule without priority.
    Command length = 1
    '''
    def setUp(self):
        s = N.lindenmayer(1)
        r = [['A', 'BAC']]
        s.add_rules(r)
        axiom = 'A'
        self.result = []
        for i in range(10):
            axiom = s._apply_rules(axiom)
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
    '''
    Test for replacement rules with priority.
    Command length = 1
    '''
    def setUp(self):
        s = N.lindenmayer(1)
        r = [['A', 'BAC', 1],
             ['B', 'BC', 2]]
        s.add_rules(r)
        axiom = 'A'
        self.result = []
        for i in range(8):
            axiom = s._apply_rules(axiom)
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
    '''
    Test for replacement rules without priority.
    Command length = 1
    '''
    def setUp(self):
        s = N.lindenmayer(1)
        r = [['A', 'BAC'],
             ['B', 'BC']]
        s.add_rules(r)
        axiom = 'A'
        self.result = []
        for i in range(8):
            axiom = s._apply_rules(axiom)
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
    '''
    Test for replacement rules without priority.
    Command length = 2
    '''
    def setUp(self):
        s = N.lindenmayer(2)
        r = [['AA', 'BBAAC'],
             ['AB', 'ABC'],
             ['AC', 'BCC']]
        s.add_rules(r)
        axiom = 'AA'
        self.result = []
        for i in range(8):
            axiom = s._apply_rules(axiom)
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
    
class testFunction(unittest.TestCase):
    '''
    Test for function rules.
    Command length = 1
    '''
    def replaceFunction(self, dstring, position):
        if dstring[position+3] == 'O': return 'BAAB'
        elif dstring[position-1] == 'O': return 'AABB'
        else: return 'OOAB'
    def setUp(self):
        s = N.lindenmayer(2)
        r = [['AB', self.replaceFunction, 1, 'function']]
        s.add_rules(r)
        axiom = 'ACCCABABDD'
        self.result = []
        for i in range(5):
            axiom = s._apply_rules(axiom)
            self.result.append(axiom)
        self.answer = ['ACCCOOABOOABDD',
                       'ACCCOOBAABOOAABBDD',
                       'ACCCOOBABAABOOAABBDD',
                       'ACCCOOBABABAABOOAABBDD',
                       'ACCCOOBABABABAABOOAABBDD']
    def testGeneration(self):
        self.assertEqual(self.result, self.answer)


if __name__ == '__main__':
    unittest.main()
