import unittest
import sys
import os
import math

sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'copads'))
import parallelarray as a

class testParallelArray(unittest.TestCase):
    def testInit0(self):
        arrayA = a.ParallelArray()
        self.assertEqual(arrayA.data, {})
        self.assertEqual(arrayA.fieldnames(), [])
    def testInit1(self):
        fnames = ['F1', 'F2', 'F3']
        arrayA = a.ParallelArray(fnames)
        self.assertEqual(arrayA.data, {'F1': [], 'F2': [], 'F3': []})
        self.assertEqual(arrayA.fieldnames(), fnames)
    def testAddFields1(self):
        fnames = ['F1', 'F2', 'F3']
        arrayA = a.ParallelArray()
        arrayA.addFields(fnames)
        self.assertEqual(arrayA.data, {'F1': [], 'F2': [], 'F3': []})
        self.assertEqual(arrayA.fieldnames(), fnames)
    def testAddFields2(self):
        fnames = ['F1', 'F2', 'F3']
        arrayA = a.ParallelArray()
        arrayA.addFields('F1')
        self.assertEqual(arrayA.data, {'F1': []})
        self.assertEqual(arrayA.fieldnames(), ['F1'])
        arrayA.addFields('F2')
        self.assertEqual(arrayA.data, {'F1': [], 'F2': []})
        self.assertEqual(arrayA.fieldnames(), ['F1', 'F2'])
    def testAddDataList1(self):
        fnames = ['F1', 'F2', 'F3']
        arrayA = a.ParallelArray(fnames)
        self.assertEqual(arrayA.data, {'F1': [], 'F2': [], 'F3': []})
        arrayA.addDataList(['F1', 'F3'], [1, 3])
        self.assertEqual(arrayA.data, {'F1': [1], 
                                       'F2': [None], 
                                       'F3': [3]})
        arrayA.addDataList(['F2'], [2])
        self.assertEqual(arrayA.data, {'F1': [1, None], 
                                       'F2': [None, 2], 
                                       'F3': [3, None]})
        arrayA.addFields('F4')
        self.assertEqual(arrayA.data, {'F1': [1, None], 
                                       'F2': [None, 2], 
                                       'F3': [3, None],
                                       'F4': [None, None]})
    def testAddDataList2(self):
        fnames = ['F1', 'F2', 'F3']
        arrayA = a.ParallelArray(fnames)
        self.assertEqual(arrayA.data, {'F1': [], 'F2': [], 'F3': []})
        arrayA.addDataList(['F1', 'F3'], [1, 3])
        self.assertEqual(arrayA.data, {'F1': [1], 
                                       'F2': [None], 
                                       'F3': [3]})
        arrayA.addDataList(['F4'], [4])
        self.assertEqual(arrayA.data, {'F1': [1, None], 
                                       'F2': [None, None], 
                                       'F3': [3, None],
                                       'F4': [None, 4]})
    def testRemoveFields(self):
        arrayA = a.ParallelArray()
        arrayA.addDataList(['F1', 'F3'], [1, 3])
        arrayA.addDataList(['F2', 'F4'], [2, 4])
        self.assertEqual(arrayA.data, {'F1': [1, None], 
                                       'F2': [None, 2], 
                                       'F3': [3, None],
                                       'F4': [None, 4]})
        self.assertEqual(arrayA.removeField('F1'), [1, None])
        self.assertEqual(arrayA.data, {'F2': [None, 2], 
                                       'F3': [3, None],
                                       'F4': [None, 4]})
        self.assertEqual(arrayA.removeField('F5'), [])
        self.assertEqual(arrayA.data, {'F2': [None, 2], 
                                       'F3': [3, None],
                                       'F4': [None, 4]})
    def testChangeFieldname(self):
        arrayA = a.ParallelArray()
        arrayA.addDataList(['F1', 'F2', 'F3', 'F4'], [1, 2, 3, 4])
        self.assertEqual(arrayA.data, {'F1': [1], 'F2': [2], 
                                       'F3': [3], 'F4': [4]})
        arrayA.changeFieldname('F4', 'FOUR')
        self.assertEqual(arrayA.data, {'F1': [1], 'F2': [2], 
                                       'F3': [3], 'FOUR': [4]})
                                       
        
if __name__ == '__main__':
    unittest.main()
