import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'copads'))
from matrix import *

def Vector_test():
    print 'a = zeros(4)'
    a = vZeros(4)

    print 'a.__doc__=',a.__doc__

    print 'a[0] = 1.0'
    a[0] = 1.0

    print 'a[3] = 3.0'
    a[3] = 3.0

    print 'a[0]=', a[0]
    print 'a[1]=', a[1]

    print 'len(a)=',len(a)
    print 'a.size()=', a.size()
            
    b = Vector([1, 2, 3, 4])
    print 'a=', a
    print 'b=', b

    print 'a+b'
    c = a + b
    c.out()

    print '-a'
    c = -a
    c.out()
    a.out()

    print 'a-b'
    c = a - b
    c.out()

    print 'a*1.2'
    c = a*1.2
    c.out()


    print '1.2*a'
    c = 1.2*a
    c.out()
    print 'a=', a

    print 'dot(a,b) = ', vDot(a,b)
    print 'dot(b,a) = ', vDot(b,a)

    print 'a*b'
    c = a*b
    c.out()
    
    print 'a/1.2'
    c = a/1.2
    c.out()

    print 'a[0:2]'
    c = a[0:2]
    c.out()

    print 'a[2:5] = [9.0, 4.0, 5.0]'
    a[2:5] = [9.0, 4.0, 5.0]
    a.out()

    print 'sqrt(a)=', vSqrt(a)
    print 'pow(a, 2*ones(len(a)))=', vPow(a, 2*vOnes(len(a)))
    print 'pow(a, 2)=',vPow(a, 2 * vOnes(len(a)))

    print 'ones(10)'
    c = vOnes(10)
    c.out()

    print 'zeros(10)'
    c = vZeros(10)
    c.out()    

    print 'del a'
    del a

    try:
        a = vRandom(11, 0., 2.)
        a.out()

    except: pass
    
def SparseMatrix_test():
    print 'a = sparse()'
    a = SparseMatrix()

    print 'a.__doc__=',a.__doc__

    print 'a[(0,0)] = 1.0'
    a[(0,0)] = 1.0
    a.out()

    print 'a[(2,3)] = 3.0'
    a[(2,3)] = 3.0
    a.out()

    print 'len(a)=',len(a)
    print 'a.size()=', a.size()
            
    b = SparseMatrix({(0,0):2.0, (0,1):1.0, (1,0):1.0, (1,1):2.0, (1,2):1.0, (2,1):1.0, (2,2):2.0})
    print 'a=', a
    print 'b=', b
    b.out()

    print 'a+b'
    c = a + b
    c.out()

    print '-a'
    c = -a
    c.out()
    a.out()

    print 'a-b'
    c = a - b
    c.out()

    print 'a*1.2'
    c = a*1.2
    c.out()


    print '1.2*a'
    c = 1.2*a
    c.out()
    print 'a=', a

    print 'dot(a, b)'
    print 'a.size()[1]=',a.size()[1],' b.size()[0]=', b.size()[0]
    c = smDot(a, b)
    c.out()

    print 'dot(b, a)'
    print 'b.size()[1]=',b.size()[1],' a.size()[0]=', a.size()[0]
    c = smDot(b, a)
    c.out()

    try:
        print 'dot(b, vector.vector([1,2,3]))'
        c = smDot(b, Vector([1,2,3]))
        c.out()
    
        print 'dot(vector.vector([1,2,3]), b)'
        c = smDot(Vector([1,2,3]), b)
        c.out()

        print 'b.size()=', b.size()
    except: pass
    
    print 'a*b -> element by element product'
    c = a*b
    c.out()

    print 'b*a -> element by element product'
    c = b*a
    c.out()
    
    print 'a/1.2'
    c = a/1.2
    c.out()

    print 'c = identity(4)'
    c = smIdentity(4)
    c.out()

    print 'c = transpose(a)'
    c = smTranspose(a)
    c.out()


    b[(2,2)]=-10.0
    b[(2,0)]=+10.0

    try:
        print 'Check conjugate gradient solver'
        s = Vector([1, 0, 0])
        print 's'
        s.out()
        x0 = s 
        print 'x = b.biCGsolve(x0, s, 1.0e-10, len(b)+1)'
        x = b.biCGsolve(x0, s, 1.0e-10,  len(b)+1)
        x.out()

        print 'check validity of CG'
        c = smDot(b, x) - s
        c.out()
    except: pass

    print 'plot b matrix'
    b.out()
    b.plot()

    print 'del b[(2,2)]'
    del b[(2,2)]

    print 'del a'
    del a
    #a.out()
    


if __name__ == "__main__":
    Vector_test()
    SparseMatrix_test()