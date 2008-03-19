import unittest
import os
import sys

class testModulus2(unittest.TestCase):
    """Unit test cases for Operations.Modulus2 class"""
    def testInitNothing(self):
        mod2 = Operations.Modulus2()
        self.assertEqual(mod2.datum, 0)
        
    def testInitOne(self):
        mod2 = Operations.Modulus2(1)
        self.assertEqual(mod2.datum, 1)
        
    def testAddSelfZero(self):
        mod2 = Operations.Modulus2(0)
        self.assertEqual(mod2 + 0, 0)
        self.assertEqual(mod2 + 1, 1)
        
    def testAddSelfOne(self):
        mod2 = Operations.Modulus2(1)
        self.assertEqual(mod2 + 0, 1)
        self.assertEqual(mod2 + 1, 0)
        
    def testMulSelfZero(self):
        mod2 = Operations.Modulus2(0)
        self.assertEqual(mod2 * 0, 0)
        self.assertEqual(mod2 * 1, 0)
        
    def testMulSelfOne(self):
        mod2 = Operations.Modulus2(1)
        self.assertEqual(mod2 * 0, 0)
        self.assertEqual(mod2 * 1, 1)
        
        
class testBoolean(unittest.TestCase):
    """Unit test cases for Operations.Boolean class"""
    def testInitNothing(self):
        bool = Operations.Boolean()
        self.assertEqual(bool.datum, 0)
        
    def testInitOne(self):
        bool = Operations.Boolean(1)
        self.assertEqual(bool.datum, 1)
        
    def testAddSelfZero(self):
        bool = Operations.Boolean(0)
        self.assertEqual(bool + 0, 0)
        self.assertEqual(bool + 1, 1)
        
    def testAddSelfOne(self):
        bool = Operations.Boolean(1)
        self.assertEqual(bool + 0, 1)
        self.assertEqual(bool + 1, 1)
        
    def testMulSelfZero(self):
        bool = Operations.Boolean(0)
        self.assertEqual(bool * 0, 0)
        self.assertEqual(bool * 1, 0)
        
    def testMulSelfOne(self):
        bool = Operations.Boolean(1)
        self.assertEqual(bool * 0, 0)
        self.assertEqual(bool * 1, 1)
        

if __name__ == "__main__":
    #    print os.path.join(os.path.dirname(os.getcwd()), 'adalp')
    sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'copads'))
    import Operations
    unittest.main()