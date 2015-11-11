import unittest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'src'))
import dataframe as d

class testSeries(unittest.TestCase):
    def testInitNothing(self):
        df = d.Series('new_series')
        self.assertTrue(df.name, 'new_series')
        self.assertEqual(df.data, [])
        self.assertEqual(df.label, [])
        self.assertEqual(df.analyses, {})
    def testAddData1(self):
        df = d.Series('new_series')
        data = range(10, 20, 1)
        df.addData(data)
        self.assertTrue(df.data, [10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
        self.assertTrue(df.label, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        
        
class testDataframe(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()