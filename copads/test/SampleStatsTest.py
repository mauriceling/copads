import sys
import os
import unittest

import SampleStatistics as S

class testSingleSample(unittest.TestCase):
    def testJaccard(self):
        self.assertEqual(D.Jaccard(o1, t1), 1.0-(5.0/7.0


class testTwoSample(unittest.TestCase):
    def testJaccard(self):
        self.assertEqual(D.Jaccard(o1, t1), 1.0-(5.0/7.0))    


class testMultiSample(unittest.TestCase):
    def testJaccard(self):
        self.assertEqual(D.Jaccard(o1, t1), 1.0-(5.0/7.0))


if __name__ == '__main__':
    sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'copads'))
    unittest.main()
