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
        data = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        df.addData(data)
        self.assertTrue(df.data, data)
        self.assertTrue(df.label, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    def testAddData2(self):
        df = d.Series('new_series')
        data = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        label = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        df.addData(data)
        self.assertTrue(df.data, data)
        self.assertTrue(df.label, label)
        
        
class testDataframe(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()