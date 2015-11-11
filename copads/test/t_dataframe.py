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
    def testGetDatum(self):
        s = d.Series('new_series')
        data = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        label = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        s.addData(data, label)
        self.assertEqual(s.getDatum('B'), 11)
        self.assertEqual(s.getDatum('D'), 13)
        self.assertEqual(s.getDatum('J'), 19)
    def testGetLabels(self):
        s = d.Series('new_series')
        data = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 18]
        label = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
        s.addData(data, label)
        self.assertEqual(s.getLabels(11), ['B'])
        self.assertEqual(s.getLabels(50), [None])
        self.assertEqual(s.getLabels(18), ['I', 'K'])
        
        
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
    def testAddData(self):
        df = d.Dataframe('frame1')
        dataset = {'seriesA': [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                   'seriesB': [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
                   'seriesC': [30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
                   'seriesD': [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]}
        label = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        df.label.sort()
        df.addData(dataset, label)
        self.assertEqual(df.series_names, ['seriesA', 'seriesB', 
                                           'seriesC', 'seriesD'])
        self.assertEqual(df.label, ['A', 'B', 'C', 'D', 'E', 'F', 'G', 
                                    'H', 'I', 'J'])
        self.assertEqual(df.data, {'A':[10, 20, 30, 40], 
                                   'B':[11, 21, 31, 41], 
                                   'C':[12, 22, 32, 42], 
                                   'D':[13, 23, 33, 43], 
                                   'E':[14, 24, 34, 44], 
                                   'F':[15, 25, 35, 45], 
                                   'G':[16, 26, 36, 46], 
                                   'H':[17, 27, 37, 47], 
                                   'I':[18, 28, 38, 48], 
                                   'J':[19, 29, 39, 49]})
        

if __name__ == "__main__":
    unittest.main()