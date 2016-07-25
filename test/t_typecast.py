import unittest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'copads'))
from typecast import *


class testTypecast(unittest.TestCase):
    def setUp(self):
        self.df = Dataframe('frame1')
        self.df.data = {'A':[10, 20, 30, 40], 
                        'B':[11, 21, 31, 41], 
                        'C':[12, 22, 32, 42], 
                        'D':[13, 23, 33, 43], 
                        'E':[14, 24, 34, 44]}
        self.df.series_names = ['seriesA', 'seriesB', 'seriesC', 'seriesD']
        self.df.label = ['A', 'B', 'C', 'D', 'E']
    def testDataframe_Series(self):
        series = tc_Dataframe_Series(self.df, 'seriesB')
        self.assertEqual(series.data, [20, 21, 22, 23, 24])
        self.assertEqual(series.label, ['A', 'B', 'C', 'D', 'E'])
        return series
    def testSeries_Dataframe(self):
        series = self.testDataframe_Series()
        df = tc_Series_Dataframe(series)
        self.assertEqual(df.series_names, ['seriesB'])
        self.assertEqual(df.data, {'A': [20], 'B': [21], 'C': [22], 
                                   'D': [23], 'E': [24]})
    def testSeries_List(self):
        series = self.testDataframe_Series()
        data = tc_Series_List(series, 'data')
        self.assertEqual(data, [20, 21, 22, 23, 24])
        label = tc_Series_List(series, 'label')
        self.assertEqual(label, ['A', 'B', 'C', 'D', 'E'])
    def testSeries_Dictionary(self):
        series = self.testDataframe_Series()
        dict = tc_Series_Dictionary(series)
        self.assertEqual(dict, {'A': 20, 'B': 21, 'C': 22, 
                                'D': 23, 'E': 24})
    
    
if __name__ == '__main__':
    unittest.main()
    