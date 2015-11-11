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
        df.addData(dataset, label)
        df.label.sort()
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
    def testAddDataAndSeries(self):
        df = d.Dataframe('frame1')
        dataset = {'seriesA': [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                   'seriesB': [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
                   'seriesC': [30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
                   'seriesD': [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]}
        label = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        df.addData(dataset, label)
        s1 = d.Series('seriesE')
        s1.addData([51, 52, 53, 54, 55],
                   ['A', 'B', 'K', 'L', 'M'])
        df.addSeries(s1, 'NA')
        self.assertEqual(df.series_names, ['seriesA', 'seriesB', 
                                           'seriesC', 'seriesD',
                                           'seriesE'])
        df.label.sort()
        self.assertEqual(df.label, ['A', 'B', 'C', 'D', 'E', 'F', 'G', 
                                    'H', 'I', 'J', 'K', 'L', 'M'])
        self.assertEqual(df.data, {'A':[10, 20, 30, 40, 51], 
                                   'B':[11, 21, 31, 41, 52], 
                                   'C':[12, 22, 32, 42, 'NA'], 
                                   'D':[13, 23, 33, 43, 'NA'], 
                                   'E':[14, 24, 34, 44, 'NA'], 
                                   'F':[15, 25, 35, 45, 'NA'], 
                                   'G':[16, 26, 36, 46, 'NA'], 
                                   'H':[17, 27, 37, 47, 'NA'], 
                                   'I':[18, 28, 38, 48, 'NA'], 
                                   'J':[19, 29, 39, 49, 'NA'],
                                   'K':['NA', 'NA', 'NA', 'NA', 53], 
                                   'L':['NA', 'NA', 'NA', 'NA', 54], 
                                   'M':['NA', 'NA', 'NA', 'NA', 55]})
    def testChangeDatum(self):
        df = d.Dataframe('frame1')
        dataset = {'seriesA': [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                   'seriesB': [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
                   'seriesC': [30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
                   'seriesD': [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]}
        label = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        df.addData(dataset, label)
        df.label.sort()
        self.assertEqual(df.series_names, ['seriesA', 'seriesB', 
                                           'seriesC', 'seriesD'])
        self.assertEqual(df.label, ['A', 'B', 'C', 'D', 'E', 'F', 'G', 
                                    'H', 'I', 'J'])
        df.changeDatum(1.3, 'seriesA', 'D')
        self.assertEqual(df.data, {'A':[10, 20, 30, 40], 
                                   'B':[11, 21, 31, 41], 
                                   'C':[12, 22, 32, 42], 
                                   'D':[1.3, 23, 33, 43], 
                                   'E':[14, 24, 34, 44], 
                                   'F':[15, 25, 35, 45], 
                                   'G':[16, 26, 36, 46], 
                                   'H':[17, 27, 37, 47], 
                                   'I':[18, 28, 38, 48], 
                                   'J':[19, 29, 39, 49]})
        df.changeDatum(2.4, 'seriesB', 'E')
        self.assertEqual(df.data, {'A':[10, 20, 30, 40], 
                                   'B':[11, 21, 31, 41], 
                                   'C':[12, 22, 32, 42], 
                                   'D':[1.3, 23, 33, 43], 
                                   'E':[14, 2.4, 34, 44], 
                                   'F':[15, 25, 35, 45], 
                                   'G':[16, 26, 36, 46], 
                                   'H':[17, 27, 37, 47], 
                                   'I':[18, 28, 38, 48], 
                                   'J':[19, 29, 39, 49]})
    def testChangeSeriesName(self):
        df = d.Dataframe('frame1')
        dataset = {'seriesA': [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                   'seriesB': [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
                   'seriesC': [30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
                   'seriesD': [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]}
        label = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        df.addData(dataset, label)
        df.label.sort()
        self.assertEqual(df.series_names, ['seriesA', 'seriesB', 
                                           'seriesC', 'seriesD'])
        df.changeSeriesName('seriesK', 'seriesB')
        self.assertEqual(df.series_names, ['seriesA', 'seriesK', 
                                           'seriesC', 'seriesD'])
    def testChangeLabel(self):
        df = d.Dataframe('frame1')
        dataset = {'seriesA': [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                   'seriesB': [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
                   'seriesC': [30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
                   'seriesD': [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]}
        label = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        df.addData(dataset, label)
        df.label.sort()
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
        df.changeLabel('X', 'C')
        self.assertEqual(df.label, ['A', 'B', 'X', 'D', 'E', 'F', 'G', 
                                    'H', 'I', 'J'])
        self.assertEqual(df.data, {'A':[10, 20, 30, 40], 
                                   'B':[11, 21, 31, 41], 
                                   'X':[12, 22, 32, 42], 
                                   'D':[13, 23, 33, 43], 
                                   'E':[14, 24, 34, 44], 
                                   'F':[15, 25, 35, 45], 
                                   'G':[16, 26, 36, 46], 
                                   'H':[17, 27, 37, 47], 
                                   'I':[18, 28, 38, 48], 
                                   'J':[19, 29, 39, 49]})
        df.changeLabel('Y', 'D')
        self.assertEqual(df.label, ['A', 'B', 'X', 'Y', 'E', 'F', 'G', 
                                    'H', 'I', 'J'])
        self.assertEqual(df.data, {'A':[10, 20, 30, 40], 
                                   'B':[11, 21, 31, 41], 
                                   'X':[12, 22, 32, 42], 
                                   'Y':[13, 23, 33, 43], 
                                   'E':[14, 24, 34, 44], 
                                   'F':[15, 25, 35, 45], 
                                   'G':[16, 26, 36, 46], 
                                   'H':[17, 27, 37, 47], 
                                   'I':[18, 28, 38, 48], 
                                   'J':[19, 29, 39, 49]})
    def testGetDatum(self):
        df = d.Dataframe('frame1')
        dataset = {'seriesA': [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                   'seriesB': [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
                   'seriesC': [30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
                   'seriesD': [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]}
        label = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        df.addData(dataset, label)
        self.assertEqual(df.getDatum('seriesA', 'B'), 11)
        self.assertEqual(df.getDatum('seriesB', 'J'), 29)
        self.assertEqual(df.getDatum('seriesP', 'B'), None)
        self.assertEqual(df.getDatum('seriesA', 'P'), None)
        self.assertEqual(df.getDatum('seriesP', 'P'), None)
    def testGetLabels(self):
        df = d.Dataframe('frame1')
        dataset = {'seriesA': [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                   'seriesB': [20, 21, 22, 23, 24, 14, 26, 27, 28, 29],
                   'seriesC': [30, 31, 32, 33, 34, 35, 14, 37, 38, 39],
                   'seriesD': [40, 41, 41, 41, 44, 45, 46, 47, 48, 49]}
        label = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        df.addData(dataset, label)
        self.assertEqual(df.getLabels(21), ['B'])
        self.assertEqual(df.getLabels(49), ['J'])
        self.assertEqual(df.getLabels(88), [None])
        rlabels = df.getLabels(14)
        rlabels.sort()
        self.assertEqual(rlabels, ['E', 'F', 'G'])
        rlabels = df.getLabels(41)
        rlabels.sort()
        self.assertEqual(rlabels, ['B', 'C', 'D'])
    def testGetSeries(self):
        df = d.Dataframe('frame1')
        dataset = {'seriesA': [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                   'seriesB': [20, 21, 22, 23, 24, 25, 26, 17, 28, 29],
                   'seriesC': [30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
                   'seriesD': [40, 41, 42, 43, 14, 45, 46, 17, 48, 49]}
        label = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        df.addData(dataset, label)
        self.assertEqual(df.getSeries(21), ['seriesB'])
        self.assertEqual(df.getSeries(49), ['seriesD'])
        self.assertEqual(df.getSeries(88), [None])
        rseries = df.getSeries(14)
        rseries.sort()
        self.assertEqual(rseries, ['seriesA', 'seriesD'])
        rseries = df.getSeries(17)
        rseries.sort()
        self.assertEqual(rseries, ['seriesA', 'seriesB', 'seriesD'])
        
    def testGetSeriesLabels(self):
        df = d.Dataframe('frame1')
        dataset = {'seriesA': [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                   'seriesB': [20, 21, 22, 23, 24, 25, 26, 17, 28, 29],
                   'seriesC': [30, 31, 10, 33, 34, 35, 36, 37, 38, 39],
                   'seriesD': [40, 41, 42, 10, 14, 45, 46, 17, 48, 49]}
        label = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        df.addData(dataset, label)
        self.assertEqual(df.getSeriesLabels(21), [('seriesB', 'B')])
        self.assertEqual(df.getSeriesLabels(49), [('seriesD', 'J')])
        self.assertEqual(df.getSeriesLabels(88), [(None, None)])
        coordinates = df.getSeriesLabels(14)
        coordinates.sort()
        self.assertEqual(coordinates, [('seriesA', 'E'), 
                                       ('seriesD', 'E')])
        coordinates = df.getSeriesLabels(17)
        coordinates.sort()
        self.assertEqual(coordinates, [('seriesA', 'H'), 
                                       ('seriesB', 'H'), 
                                       ('seriesD', 'H')])
        coordinates = df.getSeriesLabels(10)
        coordinates.sort()
        self.assertEqual(coordinates, [('seriesA', 'A'), 
                                       ('seriesC', 'C'), 
                                       ('seriesD', 'D')])
        

if __name__ == "__main__":
    unittest.main()