import unittest

class testHarness(unittest.TestCase):
    def testEqual(self, func, caseData):
        if len(caseData) < 2 or len(caseData) > 7:
            print "length of caseData must be 2-7"
        if len(caseData) == 2: 
            self.assertEqual(func(caseData[0]), 
                             caseData[1])
        if len(caseData) == 3: 
            self.assertEqual(func(caseData[0], caseData[1]), 
                             caseData[2])
        if len(caseData) == 4: 
            self.assertEqual(func(caseData[0], caseData[1], caseData[2]), 
                             caseData[3])
        if len(caseData) == 5: 
            self.assertEqual(func(caseData[0], caseData[1], caseData[2],
                                  caseData[3]), 
                             caseData[4])
        if len(caseData) == 6: 
            self.assertEqual(func(caseData[0], caseData[1], caseData[2],
                                  caseData[3], caseData[4]), 
                             caseData[5])
        if len(caseData) == 7: 
            self.assertEqual(func(caseData[0], caseData[1], caseData[2],
                                  caseData[3], caseData[4], caseData[5]), 
                             caseData[6])