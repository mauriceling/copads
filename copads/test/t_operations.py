import unittest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'copads'))
import operations

class testModulus2(unittest.TestCase):
    """Unit test cases for operations.Modulus2 class"""
    def testInitNothing(self):
        mod2 = operations.Modulus2()
        self.assertEqual(mod2.datum, 0)
        
    def testInitOne(self):
        mod2 = operations.Modulus2(1)
        self.assertEqual(mod2.datum, 1)
        
    def testAddSelfZero(self):
        mod2 = operations.Modulus2(0)
        self.assertEqual(mod2 + 0, 0)
        self.assertEqual(mod2 + 1, 1)
        
    def testAddSelfOne(self):
        mod2 = operations.Modulus2(1)
        self.assertEqual(mod2 + 0, 1)
        self.assertEqual(mod2 + 1, 0)
        
    def testMulSelfZero(self):
        mod2 = operations.Modulus2(0)
        self.assertEqual(mod2 * 0, 0)
        self.assertEqual(mod2 * 1, 0)
        
    def testMulSelfOne(self):
        mod2 = operations.Modulus2(1)
        self.assertEqual(mod2 * 0, 0)
        self.assertEqual(mod2 * 1, 1)
        
        
class testBoolean(unittest.TestCase):
    """Unit test cases for operations.Boolean class"""
    def testInitNothing(self):
        bool = operations.Boolean()
        self.assertEqual(bool.datum, 0)
        
    def testInitOne(self):
        bool = operations.Boolean(1)
        self.assertEqual(bool.datum, 1)
        
    def testAddSelfZero(self):
        bool = operations.Boolean(0)
        self.assertEqual(bool + 0, 0)
        self.assertEqual(bool + 1, 1)
        
    def testAddSelfOne(self):
        bool = operations.Boolean(1)
        self.assertEqual(bool + 0, 1)
        self.assertEqual(bool + 1, 1)
        
    def testMulSelfZero(self):
        bool = operations.Boolean(0)
        self.assertEqual(bool * 0, 0)
        self.assertEqual(bool * 1, 0)
        
    def testMulSelfOne(self):
        bool = operations.Boolean(1)
        self.assertEqual(bool * 0, 0)
        self.assertEqual(bool * 1, 1)
        

if __name__ == "__main__":
    unittest.main()