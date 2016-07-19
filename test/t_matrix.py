import unittest
import sys
import os
import math

sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'copads'))
import matrix as m
from matrix import *

class testVector(unittest.TestCase):
    def testInit0(self):
        vectorA = m.Vector()
        vectorA.zeros(4)
        self.assertEqual(vectorA.values, [0, 0, 0, 0])
    def testInit1(self):
        vectorA = m.Vector()
        vectorA.ones(4)
        self.assertEqual(vectorA.values, [1, 1, 1, 1])
    def testLog10(self):
        vectorA = m.Vector([1, 2, 3, 4])
        result = [math.log10(x) for x in vectorA.values]
        self.assertEqual(vectorA.log10(), result)
    def testLog_e(self):
        vectorA = m.Vector([1, 2, 3, 4])
        result = [math.log(x, math.e) for x in vectorA.values]
        self.assertEqual(vectorA.log(), result)
    def testLog_2(self):
        vectorA = m.Vector([1, 2, 3, 4])
        result = [math.log(x, 2) for x in vectorA.values]
        self.assertEqual(vectorA.log(2), result)
    def testExp(self):
        vectorA = m.Vector([1, 2, 3, 4])
        result = [math.exp(x) for x in vectorA.values]
        self.assertEqual(vectorA.exp(), result)
    def testPow(self):
        vectorA = m.Vector([1, 2, 3, 4])
        result = [float(x)**4 for x in vectorA.values]
        self.assertEqual(vectorA.pow(4), result)
    def testSin(self):
        vectorA = m.Vector([1, 2, 3, 4])
        result = [math.sin(x) for x in vectorA.values]
        self.assertEqual(vectorA.sin(), result)
    def testCos(self):
        vectorA = m.Vector([1, 2, 3, 4])
        result = [math.cos(x) for x in vectorA.values]
        self.assertEqual(vectorA.cos(), result)
    def testTan(self):
        vectorA = m.Vector([1, 2, 3, 4])
        result = [math.tan(x) for x in vectorA.values]
        self.assertEqual(vectorA.tan(), result)
    def testASin(self):
        vectorA = m.Vector([0.1, 0.2, 0.3, 0.4])
        result = [math.asin(x) for x in vectorA.values]
        self.assertEqual(vectorA.asin(), result)
    def testACos(self):
        vectorA = m.Vector([0.1, 0.2, 0.3, 0.4])
        result = [math.acos(x) for x in vectorA.values]
        self.assertEqual(vectorA.acos(), result)
    def testATan(self):
        vectorA = m.Vector([0.1, 0.2, 0.3, 0.4])
        result = [math.atan(x) for x in vectorA.values]
        self.assertEqual(vectorA.atan(), result)
    def testSinh(self):
        vectorA = m.Vector([0.1, 0.2, 0.3, 0.4])
        result = [math.sinh(x) for x in vectorA.values]
        self.assertEqual(vectorA.sinh(), result)
    def testCosh(self):
        vectorA = m.Vector([0.1, 0.2, 0.3, 0.4])
        result = [math.cosh(x) for x in vectorA.values]
        self.assertEqual(vectorA.cosh(), result)
    def testTanh(self):
        vectorA = m.Vector([0.1, 0.2, 0.3, 0.4])
        result = [math.tanh(x) for x in vectorA.values]
        self.assertEqual(vectorA.tanh(), result)
    def testASinh(self):
        vectorA = m.Vector([0.1, 0.2, 0.3, 0.4])
        result = [math.asinh(x) for x in vectorA.values]
        self.assertEqual(vectorA.asinh(), result)
    def testACosh(self):
        vectorA = m.Vector([1, 2, 3, 4])
        result = [math.acosh(x) for x in vectorA.values]
        self.assertEqual(vectorA.acosh(), result)
    def testATanh(self):
        vectorA = m.Vector([0.1, 0.2, 0.3, 0.4])
        result = [math.atanh(x) for x in vectorA.values]
        self.assertEqual(vectorA.atanh(), result)
    def testSqrt(self):
        vectorA = m.Vector([1, 2, 3, 4])
        result = [math.sqrt(x) for x in vectorA.values]
        self.assertEqual(vectorA.sqrt(), result)
    def testRoot2(self):
        vectorA = m.Vector([1, 2, 3, 4])
        result = [math.sqrt(x) for x in vectorA.values]
        self.assertEqual(vectorA.root(2), result)
    def testRoot3(self):
        vectorA = m.Vector([1, 2, 3, 4])
        result = [float(x)**(1.0/3) for x in vectorA.values]
        self.assertEqual(vectorA.root(3), result)
    def testAbs(self):
        vectorA = m.Vector([1, -2, 3, 4])
        result = [math.fabs(x) for x in vectorA.values]
        self.assertEqual(vectorA.abs(), result)
    def testFactorial(self):
        vectorA = m.Vector([1, 2, 3, 4])
        result = [math.factorial(x) for x in vectorA.values]
        self.assertEqual(vectorA.factorial(), result)
    def testDegrees(self):
        vectorA = m.Vector([1, 2, 3, 4])
        result = [math.degrees(x) for x in vectorA.values]
        self.assertEqual(vectorA.degrees(), result)
    def testRadians(self):
        vectorA = m.Vector([10, 20, 30, 40])
        result = [math.radians(x) for x in vectorA.values]
        self.assertEqual(vectorA.radians(), result)
    def testSum(self):
        vectorA = m.Vector([1, 2, 3, 4])
        self.assertEqual(vectorA.factorial(), math.fsum(vectorA.values))
    def testAdd(self):
        vectorA = m.Vector([1, 2, 3, 4])
        vectorB = m.Vector([1, 2, 3, 4])
        result = [2, 4, 6, 8]
        vectorC = vectorA + vectorB
        self.assertEqual(vectorC.values, result)

# def Vector_test():

    # print('a[0] = 1.0')
    # a[0] = 1.0

    # print('a[3] = 3.0')
    # a[3] = 3.0

    # print('a[0]=', a[0])
    # print('a[1]=', a[1])

    # print('len(a)=',len(a))
    # print('a.size()=', a.size())
            
    # b = Vector([1, 2, 3, 4])
    # print('a=', a)
    # print('b=', b)

    # print('a+b')
    # c = a + b
    # c.out()

    # print('-a')
    # c = -a
    # c.out()
    # a.out()

    # print('a-b')
    # c = a - b
    # c.out()

    # print('a*1.2')
    # c = a*1.2
    # c.out()

    # print('1.2*a')
    # c = 1.2*a
    # c.out()
    # print('a=', a)

    # print('dot(a,b) = ', vDot(a,b))
    # print('dot(b,a) = ', vDot(b,a))

    # print('a*b')
    # c = a*b
    # c.out()
    
    # print('a/1.2')
    # c = a/1.2
    # c.out()

    # print('a[0:2]')
    # c = a[0:2]
    # c.out()

    # print('a[2:5] = [9.0, 4.0, 5.0]')
    # a[2:5] = [9.0, 4.0, 5.0]
    # a.out()

    # print('sqrt(a)=', vSqrt(a))
    # print('pow(a, 2*ones(len(a)))=', vPow(a, 2*vOnes(len(a))))
    # print('pow(a, 2)=',vPow(a, 2 * vOnes(len(a))))
  

    # print('del a')
    # del a

    # try:
        # a = vRandom(11, 0., 2.)
        # a.out()

    # except: pass
    
# def SparseMatrix_test():
    # print('a = sparse()')
    # a = SparseMatrix()

    # print('a.__doc__=',a.__doc__)

    # print('a[(0,0)] = 1.0')
    # a[(0,0)] = 1.0
    # a.out()

    # print('a[(2,3)] = 3.0')
    # a[(2,3)] = 3.0
    # a.out()

    # print('len(a)=',len(a))
    # print('a.size()=', a.size())
            
    # b = SparseMatrix({(0,0):2.0, (0,1):1.0, (1,0):1.0, (1,1):2.0, (1,2):1.0, (2,1):1.0, (2,2):2.0})
    # print('a=', a)
    # print('b=', b)
    # b.out()

    # print('a+b')
    # c = a + b
    # c.out()

    # print('-a')
    # c = -a
    # c.out()
    # a.out()

    # print('a-b')
    # c = a - b
    # c.out()

    # print('a*1.2')
    # c = a*1.2
    # c.out()


    # print('1.2*a')
    # c = 1.2*a
    # c.out()
    # print('a=', a)

    # print('dot(a, b)')
    # print('a.size()[1]=',a.size()[1],' b.size()[0]=', b.size()[0])
    # c = smDot(a, b)
    # c.out()

    # print('dot(b, a)')
    # print('b.size()[1]=',b.size()[1],' a.size()[0]=', a.size()[0])
    # c = smDot(b, a)
    # c.out()

    # try:
        # print('dot(b, vector.vector([1,2,3]))')
        # c = smDot(b, Vector([1,2,3]))
        # c.out()
    
        # print('dot(vector.vector([1,2,3]), b)')
        # c = smDot(Vector([1,2,3]), b)
        # c.out()

        # print('b.size()=', b.size())
    # except: pass
    
    # print('a*b -> element by element product')
    # c = a*b
    # c.out()

    # print('b*a -> element by element product')
    # c = b*a
    # c.out()
    
    # print('a/1.2')
    # c = a/1.2
    # c.out()

    # print('c = identity(4)')
    # c = smIdentity(4)
    # c.out()

    # print('c = transpose(a)')
    # c = smTranspose(a)
    # c.out()


    # b[(2,2)]=-10.0
    # b[(2,0)]=+10.0

    # try:
        # print('Check conjugate gradient solver')
        # s = Vector([1, 0, 0])
        # print('s')
        # s.out()
        # x0 = s 
        # print('x = b.biCGsolve(x0, s, 1.0e-10, len(b)+1)')
        # x = b.biCGsolve(x0, s, 1.0e-10,  len(b)+1)
        # x.out()

        # print('check validity of CG')
        # c = smDot(b, x) - s
        # c.out()
    # except: pass

    # print('plot b matrix')
    # b.out()
    # b.plot()

    # print('del b[(2,2)]')
    # del b[(2,2)]

    # print('del a')
    # del a
    # #a.out()
    


if __name__ == "__main__":
    # Vector_test()
    # SparseMatrix_test()
    unittest.main()