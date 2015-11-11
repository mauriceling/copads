import unittest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'src'))
import dataframe as d

class testSeries(unittest.TestCase):
    def testInitNothing(self):
        s = d.Series('new_series')
        self.assertTrue(s.name, 'new_series')
        self.assertEqual(s.data, [])
        self.assertEqual(s.label, [])
        self.assertEqual(s.analyses, {})
    def testAddData1(self):
        s = d.Series('new_series')
        data = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        s.addData(data)
        self.assertEqual(s.data, data)
        self.assertEqual(s.label, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    def testAddData2(self):
        s = d.Series('new_series')
        data = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        label = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        s.addData(data, label)
        self.assertEqual(s.data, data)
        self.assertEqual(s.label, label)
    def testAddData3(self):
        s = d.Series('new_series')
        data = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        label = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        s.addData(data, label)
        s.addData([30, 31])
        self.assertEqual(s.data, data + [30, 31])
        self.assertEqual(s.label, label + [0, 1])
    def testAddData4(self):
        s = d.Series('new_series')
        data = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        label = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        s.addData(data, label)
        s.addData([30, 31], ['K', 'L'])
        self.assertEqual(s.data, data + [30, 31])
        self.assertEqual(s.label, label + ['K', 'L'])
    def testChangeDatum(self):
        s = d.Series('new_series')
        data = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        label = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        s.addData(data, label)
        s.changeDatum(50, 'C')
        self.assertEqual(s.data, [10, 11, 50, 13, 14, 15, 16, 17, 18, 19])
    def testChangeLabel(self):
        s = d.Series('new_series')
        data = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        label = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        s.addData(data, label)
        s.changeLabel('Z', 'C')
        self.assertEqual(s.label, ['A', 'B', 'Z', 'D', 'E', 'F', 
                                   'G', 'H', 'I', 'J'])
        
        
class testDataframe(unittest.TestCase):
    def testAddSeries1(self):
        s = d.Series('new_series')
        data = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        label = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        s.addData(data, label)
        df = d.Dataframe('frame1')
        df.addSeries(s)
        self.assertEqual(df.series_names, ['new_series'])
        df.label.sort()
        self.assertEqual(df.label, label)
        self.assertEqual(df.data, {'A':[10], 
                                   'B':[11], 
                                   'C':[12], 
                                   'D':[13], 
                                   'E':[14], 
                                   'F':[15], 
                                   'G':[16], 
                                   'H':[17], 
                                   'I':[18], 
                                   'J':[19]})
    def testAddSeries2(self):
        s1 = d.Series('seriesA')
        s1.addData([10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                   ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
        s2 = d.Series('seriesB')
        s2.addData([51, 52, 53, 54, 55],
                   ['A', 'B', 'K', 'L', 'M'])
        df = d.Dataframe('frame1')
        df.addSeries(s1, None)
        df.addSeries(s2, None)
        self.assertEqual(df.series_names, ['seriesA', 'seriesB'])
        df.label.sort()
        self.assertEqual(df.label, ['A', 'B', 'C', 'D', 'E', 'F', 'G', 
                                    'H', 'I', 'J', 'K', 'L', 'M'])
        self.assertEqual(df.data, {'A':[10, 51], 
                                   'B':[11, 52], 
                                   'C':[12, None], 
                                   'D':[13, None], 
                                   'E':[14, None], 
                                   'F':[15, None], 
                                   'G':[16, None], 
                                   'H':[17, None], 
                                   'I':[18, None], 
                                   'J':[19, None],
                                   'K':[None, 53],
                                   'L':[None, 54],
                                   'M':[None, 55]})


if __name__ == "__main__":
    unittest.main()