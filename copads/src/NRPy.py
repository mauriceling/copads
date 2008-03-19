"""
This file contains Python implementations of the numerical functions in 

Press, William H., Flannery, Brian P., Teukolsky, Saul A., and Vetterling, 
William T. 1989. Numerical Recipes in Pascal. Cambridge University Press,
Cambridge (ISBN 978-0521375160);
Press, William H., Flannery, Brian P., Teukolsky, Saul A., and Vetterling, 
William T. 1992. Numerical Recipes in C, 2nd edition. Cambridge University 
Press, Cambridge (ISBN 978-0521431088)

Numerical Recipes in C, 2nd edition is freely browsable online at 
http://www.nrbook.com/a/bookcpdf.php but is not intended as a substitution
for purchasing the book.

Unless otherwise stated as "No reference implementation", the functions 
implemented in this file (module) has a reference implementation in a 
programming language used in the reference book. In mathematics, it is 
likely that a function is built (depends) on other simpler functions,
such dependencies (if any) are listed in each function.

Functions will be named as in the references and will be referred to section 
number. For example, the reference "NRP 5.2" refers to Numerical Recipes 
in Pascal chapter 5 section 2.

The authors of Numerical Recipes in Pascal (NRP) and Numerical Recipes in
C, 2nd edition (NRC2) explicitly allows the reader to analyze the mathematical 
ideas in the codes within the book and owns the re-implemented functions as 
stated in NRP and NRC2 that "If you analyze the ideas contained in a program, 
and then express those ideas in your own distinct implemtnation, then that new 
program implementation belongs to you" (page xv of NRP; page xviii of NRC2).
Not mentioned in NRP, NRC2 allows the reader a "free licence" (page xviii of 
NRC2) which allows the reader to make one machine-readable copy of the C codes
in the book for his/her own use (not distribution) in his/her work, provided 
that the source codes are not distributed. As such, the codes in this file
will be called by other functions in COPADS but not for direct use by users
of COPADS - if you intend to call these functions directly, the simplest way
is to own a copy of both NRP and NRC2.
"""

import math
import Constants
from JMathsExceptions import FunctionParameterTypeError
from JMathsExceptions import FunctionParameterValueError


def adi(): 
    pass
def amoeba(): pass
def anneal(): pass
def avevar(): pass
def badluk(): pass
def balanc(): pass
def bcucof(): pass
def bcuint(): pass
def bessi(n, x):
    """Modified Bessel function I-sub-n(x). Ref: NRP 6.5
    
    @param n: integer, more than 1 - modified n-th Bessel function 
    @param x: positive integer
    @return: modified n-th Bessel function of x
    """
    iacc = 40
    bigno = 1.0e10
    bigni = 1.0e-10
    if n < 2: 
        raise FunctionParameterValueError('n must be more than 1 - use bessi0 or bessi1 \
            for n = 0 or 1 respectively')
    else:
        if x == 0.0: ans = 0.0
        else:
            ans = 0.0
            tox = 2.0/abs(x)
            bip = 0.0
            bi = 1.0
            m = 2 * (n + math.floor(math.sqrt(iacc * n)))
            for j in range(m, 1, -1):
                bim = bip+j*tox*bi
                bip = bi
                bi = bim
                if abs(bi) > bigno:
                    ans = ans*bigni
                    bi = bi*bigni
                    bip = bip*bigni
                if j == n: ans = bip
            if x < 0.0 and (n % 2) == 1: ans = -ans
            return ans*bessi0(x)/bi
    
def bessi0(x):
    """Modified Bessel function I-sub-0(x). Ref: NRP 6.5
    
    @param x: float number
    @return: modified Bessel function base 0 of x"""
    if abs(x) < 3.75:
        y = (x/3.75)*(x/3.75)
        return 1.0 + y * (3.5156229 + y * (3.0899424 + y * (1.2067492 + y * \
                (0.2659732 + y * (0.360768e-1 + y  * 0.45813e-2)))))
    else:
        ax = abs(x)
        y = 3.75/ax
        return (math.exp(ax)/math.sqrt(ax)) * (0.39894228 + y * (0.1328592e-1 + \
             y * (0.225319e-2 + y * (-0.157565e-2 + y * (0.916281e-2 + y * \
             (-0.2057706e-1 + y * (0.2635537e-1 + y * (-0.1647633e-1 + y * \
               0.392377e-2))))))))
    
def bessi1(x):
    """Bessel function I-sub-1(x). Ref: NRP 6.5
    
    @param x: float number
    @return: float number 
    """
    if abs(x) < 3.75:
        y = (x/3.75)*(x/3.75)
        return x * (0.5 + y * (0.87890594 + y * (0.51498869 + y * (0.15084934 + \
               y * (0.2658733e-1 + y * (0.301532e-2 + y * 0.32411e-3))))))
    else:
        ax = abs(x)
        y = 3.75/ax
        ans = 0.2282967e-1 + y * (-0.2895312e-1 + y * (0.1787654e-1 - y * \
               0.420059e-2))
        ans = 0.39894228 + y * (-0.3988024e-1 + y * (-0.362018e-2 + y * \
                 (0.163801e-1 + y * (-0.1031555e-1 + y * ans))))
        ans = (math.exp(ax)/math.sqrt(ax))*ans
        if x < 0.0: return -ans
        else: return ans
        
def bessj(): 
    """Bessel function J-sub-n(x). Ref: NRP 6.5
    
    @param x: float number
    @return: float number 
    """
    iacc = 40
    bigno = 1.0e10
    bigni = 1.0e-10
    if n < 2: 
        raise FunctionParameterValueError('n must be more than 1 - use bessj0 or bessj1 \
            for n = 0 or 1 respectively')
    if x == 0.0: ans = 0.0
    else:
        if abs(x) > 1.0 * n:
            tox = 2.0/abs(x)
            bjm = bessj0(abs(x))
            bj = bessj1(abs(x))
            for j in range(1, n):
                bjp = j*tox*bj-bjm
                bjm = bj
                bj = bjp
            ans = bj
        else:
            tox=2.0/abs(x)
            m = 2*((n+math.floor(math.sqrt(1.0*(iacc*n)))) % 2)
            ans = 0.0
            jsum = 0
            sum = 0
            bjp = 0.0
            bj = 1.0
            for j in range(m, 1, -1):
                bjm = j*tox*bj-bjp
                bjp = bj
                bj = bjm
                if abs(bj) > bigno:
                    bj = bj*bigni
                    bjp = bjp*bigni
                    ans = ans*bigni
                    sum = sum*bigni
                if jsum <> 0: sum = sum + bj
                jsum = 1-jsum
                if j == n: ans = bjp
            sum = 2.0*sum-bj
            ans = ans/sum
        if x < 0.0 and (n % 2) == 1: ans = -ans
        return ans

def bessj0(x):
    """Bessel function J-sub-0(x). Ref: NRP 6.4
    
    @param x: float number
    @return: float number 
    """
    if abs(x) < 8.0:
        y = x*x
        return (57568490574.0 + y * (-13362590354.0 + y * (651619640.7 + \
               y * (-11214424.18 + y * (77392.33017 + y * (-184.9052456))))))/ \
               (57568490411.0 + y * (1029532985.0 + y * (9494680.718 + y * \
               (59272.64853 + y * (267.8532712 + y * 1.0)))))
    else: 
        ax = abs(x)
        z = 8.0/ax
        y = z*z
        xx = ax - 0.785398164
        ans1 = 1.0 + y * (-0.1098628627e-2 + y * (0.2734510407e-4 + y * \
              (-0.2073370639e-5 + y * 0.2093887211e-6)))
        ans2 = -0.156249995e-1 + y * (0.1430488765e-3 + y * (-0.6911147651e-5 + \
             y * (0.7621095161e-6 - y * 0.934945152e-7)))
        return math.sqrt(0.636619772 / ax ) * (math.cos(xx) * ans1 - z * \
               math.sin(xx) * ans2)
        
def bessj1(x):
    """Bessel function J-sub-1(x). Ref: NRP 6.4
    
    @param x: float number
    @return: float number 
    """
    if abs(x) < 8.0:
        y = x*x
        ans1 = x * (72362614232.0 + y * (-7895059235.0 + y * (242396853.1 + y * \
              (-2972611.439 + y * (15704.4826 + y * (-30.16036606))))))
        ans2 = 144725228442.0 + y * (2300535178.0 + y * (18583304.74 + y * \
             (99447.43394 + y * (376.9991397 + y))))
        return ans1 / ans2
    else:
        ax = abs(x)
        x = 8.0 / ax
        y = z*z
        xx = ax - 2.356194491
        ans1 = 1.0 + y * (0.183105e-2 + y * (-0.3516396496e-4 + y * \
             (0.2457520174e-5 + y * (-0.240337019e-6))))
        ans2 = 0.04687499995 + y * (-0.2002690873e-3 + y * (0.8449199096e-5 + y * \
            (-0.88228987e-6 + y * 0.105787412e-6)))
        if x < 0.0: return math.sqrt(0.636619772 / ax ) * (math.cos(xx) * ans1 - z * \
                           math.sin(xx) * ans2)
        else: return -1 * math.sqrt(0.636619772 / ax ) * (math.cos(xx) * ans1 - \
                  z * math.sin(xx) * ans2)
        
def bessk(n, x):
    """Bessel function K-sub-n(x). Ref: NRP 6.5
    
    @param n: integer, more than 1 - modified n-th Bessel function 
    @param x: positive integer
    @return: modified n-th Bessel function of x
    """
    if n < 2: 
        raise FunctionParameterValueError('n must be more than 1 - use bessk0 or bessk1 \
            for n = 0 or 1 respectively')
    else:
        tox = 2.0/x
        bkm = bessk0(x)
        bk = bessk1(x)
        for j in range(1, n):
            bkp = bkm * j * tox * bk
            bkm = bk
            bk = bkp
        return bk
        
def bessk0(x):
    """Bessel function K-sub-0(x). Ref: NRP 6.5
    
    @param n: integer, more than 1 - n-th Bessel function 
    @param x: positive integer
    @return: n-th Bessel function of x"""
    if x <= 2.0:
        y = x * x/4.0
        return (-math.log(x/2.0) * bessi0(x)) + (-0.57721566 + y * (0.4227842 + y * \
                (0.23069756 + y * (0.348859e-1 + y * (0.262698e-2 + y * (0.1075e-3 + \
                 y * 0.74e-5))))))
    else:
        y = 2.0/x
        return (math.exp(-x)/math.sqrt(x)) * (1.25331414 + y * (-0.7832358e-1 + y * \
                (0.2189568e-1 + y * (-0.1062446e-1 + y * (0.587872e-2 + y * \
                  (-0.25154e-2 + y * 0.53208e-3))))))
    
def bessk1():
    """Bessel function K-sub-1(x). Ref: NRP 6.5
    
    @param n: integer, more than 1 - n-th Bessel function 
    @param x: positive integer
    @return: n-th Bessel function of x"""
    if x <= 2.0:
        y = x*x/4.0
        return (math.log(x/2.0) * bessi1(x)) + (1.0/x) * (1.0 + y * (0.15443144 + y * \
                 (-0.67278579 + y * (-0.18156897 + y * (-0.1919402e-2 + y * \
                (-0.110404e-2 + y * (-0.4686e-4)))))))
    else:
        y = 2.0/x
        return (math.exp(-x)/math.sqrt(x)) * (1.25331414 + y * (0.23498619 + y * \
                (-0.365562e-1 + y * (0.1504268e-1 + y * (-0.780353e-2 + y * \
                 (0.325614e-2 + y * (-0.68245e-3)))))))
        
def bessy(n, x):
    """Bessel function Y-sub-n(x). Ref: NRP 6.4
    
    @param n: integer, more than 1 - n-th Bessel function 
    @param x: positive integer
    @return: n-th Bessel function of x
    """
    if n < 2: 
        raise FunctionParameterValueError('n must be more than 1 - use bessy0 or bessy1 \
            for n = 0 or 1 respectively')
    else:
        tox = 2.0/x
        by = bessy1(x)
        bym = bessy0(x)
        for j in range(1, n):
            byp = j * tox * by - bym
            bym = by
            by = byp
        return by
    
def bessy0(x):
    """Bessel function Y-sub-0(x). Ref: NRP 6.4
    Depend: bessj0
    
    @param x: float number
    @return: float number 
    """
    if x < 8.0:
        y = x*x
        ans1 = -2957821389.0 + y * (7062834065.0 + y * (-512359803.6 + y * \
                (10879881.29 + y * (-86327.92757 + y * 228.4622733))))
        ans2 = 40076544269.0 + y * (745249964.8 + y * (7189466.438 + y * \
               (47447.2647 + y * (226.1030244 + y * 1.0))))
        return (ans1 / ans2) + 0.636619772 * bessj0(x) * math.log(x)
    else:
        z = 8.0 / x
        y = z*z
        xx = x - 0.785398164
        ans1 = 1.0 + y * (-0.1098628627e-2 + y * (0.2734510407e-4 + y * \
              (-0.2073370639e-5 + y * 0.2093887211e-6)))
        ans2 = -0.1562499995e-1 + y * (0.1430488765e-3 + y * (-0.6911147651e-5 + \
              y * (0.7621095161e-6 + y * (-0.934945152e-7))))
        ans = math.sin(xx) * ans1 + z * math.cos(xx) * ans2
        return math.sqrt(0.636619772 / x) * ans
    
def bessy1(x):
    """Bessel function Y-sub-1(x). Ref: NRP 6.4
    Depend: bessj1
    
    @param x: float number
    @return: float number 
    """
    if abs(x) < 8.0:
        y = x*x
        ans1 = x * (-0.4900604943e13 + y * (0.127527439e13 + y * (-0.5153438139e11 + \
              y * (0.7349264551e9 + y * (-0.4237922726e7 + y * 0.8511937935e4)))))
        ans2 = 0.249958057e14 + y * (0.4244419664e12 + y * (0.3733650367e10 + y * \
                (0.2245904002e8 + y * (0.102042605e6 + y * (0.3549632885e3 + y)))))
        return (ans1/ans2) + 0.626619772 * (bessj1(x) * math.log(x) - (1.0/x))
    else:
        ax = abs(x)
        x = 8.0 / ax
        y = z*z
        xx = ax - 2.356194491
        ans1 = 1.0 + y * (0.183105e-2 + y * (-0.3516396496e-4 + y * \
             (0.2457520174e-5 + y * (-0.240337019e-6))))
        ans2 = 0.04687499995 + y * (-0.2002690873e-3 + y * (0.8449199096e-5 + y * \
            (-0.88228987e-6 + y * 0.105787412e-6)))
        if x < 0.0: return math.sqrt(0.636619772 / ax ) * (math.cos(xx) * ans1 - z * \
                           math.sin(xx) * ans2)
        else: return -1 * math.sqrt(0.636619772 / ax ) * (math.cos(xx) * ans1 - \
                  z * math.sin(xx) * ans2)

def beta(z, w): 
    """Beta function. 
    Depend: gammln
    Ref: NRP 6.1
    
    @param z: float number
    @param w: float number
    @return: float number""" 
    return math.exp(gammln(z) + gammln(w) - gammln(z+w))

def betacf(a, b, x):
    """
    Continued fraction for incomplete beta function. 
    Adapted from salstat_stats.py of SalStat (www.sf.net/projects/salstat)
    Ref; NRP 6.3
    """
    ITMAX = 200
    EPS = 3.0e-7

    bm = az = am = 1.0
    qab = a+b
    qap = a+1.0
    qam = a-1.0
    bz = 1.0-qab*x/qap
    for i in range(ITMAX+1):
        em = float(i+1)
        tem = em + em
        d = em*(b-em)*x/((qam+tem)*(a+tem))
        ap = az + d*am
        bp = bz+d*bm
        d = -(a+em)*(qab+em)*x/((qap+tem)*(a+tem))
        app = ap+d*az
        bpp = bp+d*bz
        aold = az
        am = ap/bpp
        bm = bp/bpp
        az = app/bpp
        bz = 1.0
        if (abs(az-aold)<(EPS*abs(az))):
            return az

def betai(a,b,x):
    """
    Incomplete beta function

    I-sub-x(a,b) = 1/B(a,b)*(Integral(0,x) of t^(a-1)(1-t)^(b-1) dt)

    where a,b>0 and B(a,b) = G(a)*G(b)/(G(a+b)) where G(a) is the gamma
    function of a. 
    
    Adapted from salstat_stats.py of SalStat (www.sf.net/projects/salstat)
    Depend: betacf, gammln
    Ref: NRP 6.3
    """
    if (x<0.0 or x>1.0):
        raise FunctionParameterValueError('Bad x in lbetai')
    if (x==0.0 or x==1.0):
        bt = 0.0
    else:
        bt = math.exp(gammln(a+b)-gammln(a)-gammln(b)+a*math.log(x)+b*
                        math.log(1.0-x))
    if (x<(a+1.0)/(a+b+2.0)):
        return bt*betacf(a,b,x)/float(a)
    else:
        return 1.0-bt*betacf(b,a,1.0-x)/float(b)

def bico(n, k):
    """Binomial coefficient. Returns n!/(k!(n-k)!)
    Depend: factln, gammln
    Ref: NRP 6.1
    
    @param n: total number of items
    @param k: required number of items
    @return: floating point number  
    """ 
    return math.floor(math.exp(factln(n) - factln(k) - factln(n-k)))

def bnldev(): pass
def brent(): pass
def bsstep(): pass
def caldat(): pass
def cel(): pass
def chder(): pass

def chebev(a, b, c, m , x):
    """Chebyshev evaluation.
    Ref: NRP 5.6
    
    @param a: float number
    @param b: float number
    @param c: list of Chebyshev coefficients produced by chebft with the 
    same 'a' and 'b'
    @param m:
    @param x: 
    @return: float number - function value   
    """
    if (x-a)*(x-b) > 0.0:
        raise FunctionParameterValueError('x must be between a and b')
    else:
        d, dd = 0.0, 0.0
        y = (2.0 * x - a - b) / (b - a)
        y2 = 2.0 * y
        for i in range(m, 0, -1):
            sv = d
            d = y2 * d - dd + c[i]
            dd = sv
        return y * d - dd + 0.5 * c[0]
    
def chebtf(): pass
def chebpc(): pass
def chint(): pass
def chsone(): pass
def chstwo(): pass
def cntab1(): pass
def cntab2(): pass
def convlv(): pass
def correl(): pass
def cosft(): pass
def covsrt(): pass
def dbrent(): pass
def ddpoly(): pass
def des(): pass
def df1dim(): pass
def dfpmin(): pass
def eclass(): pass
def eclazz(): pass
def eigsrt(): pass
def el2(): pass
def elmhes(): pass

def erf(x): 
    """
    Error function (a special incomplete gamma function) equivalent to gammp(0.5, x^2) 
    for x => 0. 
    Depend: gammp, gser. gcf, gammln
    Ref: NRP 6.2
    
    @param x: float number
    @return: float number
    """
    if x < 0.0: return -1*gammp(0.5, x*x)
    else: return gammp(0.5, x*x)
    
def erfc(x):
    """
    Complementary error function (a special incomplete gamma function) equivalent to 
    gammq(0.5, x^2) which is equivalent to 1 - gammp(0.5, x^2) for x => 0. 
    Depend: gammp, gammq, gser, gcf, gammln
    Ref: NRP 6.2
    
    @param x: float number
    @return: float number
    """
    if x < 0.0: return 1.0 + gammp(0.5, x*x)
    else: return gammq(0.5, x*x)
    
def erfcc(x):
    """
    Complementart error function similar to erfc(x) but with fractional error lesser than
    1.2e-7. 
    Ref: NRP 6.2
    
    @param x: float number
    @return: float number
    """
    z = abs(x)
    t = 1.0 / (1.0 + 0.5 * z)
    ans = t * math.exp(-z * z - 1.26551223 + t * (1.00002368 + t * (0.37409196 + t * \
        (0.09678418 + t * (-0.18628806 + t * (-1.13520398 + t * 1.48851587 + t * \
        (-0.82215223 + t * 0.17087277)))))))
    if x >= 0.0: return ans
    else: return 2.0 - ans
    
def eulsum(): pass
def evlmem(): pass
def expdev(): pass
def f1dim(): pass
def factln(n):
    """Natural logarithm of factorial: ln(n!)
    Ref: NRP 6.1
    
    @param n: positive integer
    @return: natural logarithm of factorial of n """
    return gammln(n + 1.0)

def factrl(n):
    """Factorial: n!
    Ref: NRP 6.1
    
    @param n: positive integer
    @return: factorial of n """
    return math.exp(gammln(n + 1.0))

def fgauss(): pass
def fit(): pass
def fixrts(): pass
def fleg(): pass
def flmoon(): pass
def four1(): pass
def fourn(): pass
def fpoly(): pass
def frprmn(): pass
def ftest(): pass
def gamdev(): pass

def gammln(n):
    """Gamma function. Ref: NRP 6.1
    
    @param n: float number
    @return: float number"""
    x = n - 1
    tmp = x + 5.5
    tmp = (x + 0.5) * math.log(tmp) - tmp
    ser = 1.0 + (76.18009173/(x + 1.0)) - (86.50532033/(x+2.0)) + (24.01409822/(x+3.0)) \
        (-1.231739516/(x+4.0)) + (0.120858003e-2/(x+5.0)) - (0.536382e-5/(x+6.0))
    return tmp + math.log(Constants.SQRT2PI * ser)

def gammp(a, x): 
    """Gamma incomplete function, P(a,x). 
    P(a,x) = (1/gammln(a)) * integral(0, x, (e^-t)*(t^(a-1)), dt)
    Depend: gser, gcf, gammln
    Ref: NRP 6.2
    
    @param a: float number
    @param x: float number
    @return: float number
    """
    if x < 0.0 and a <= 0.0: raise TypeError
    if x < a + 1.0:
        gser(a, x, gamser, gln)
        return gamser
    else:
        gcf(a, x, gammcf, gln)
        return 1.0 - gammcf
    
def gammq(): pass
def gasdev(): pass
def gauleg(): pass
def gaussj(): pass
def gcf(): pass
def golden(): pass
def gser(): pass
def hqr(): pass
def hunt(): pass
def indexx(): pass
def irbit1(): pass
def irbit2(): pass
def jacobi(): pass
def julday(): pass
def kendl1(): pass
def kendl2(): pass
def ksone(): pass
def kstwo(): pass
def laguer(): pass
def lfit(): pass
def linmin(): pass
def locate(): pass
def lubksb(): pass
def ludcmp(): pass
def mdian1(data):
    """Calculates the median of a list of numerical values using sorting. Ref: NRP 13.2
    
    @param data: a 1-dimensional list of numerical data
    @return: value of median
    """
    data.sort()
    n2 = len(data) % 2
    if n2 % 2 == 1: return data[n2+1]
    else: return 0.5*(x[n2] + x[n2+1])
    
def mdian2(): pass
def medfit(): pass
def memcof(): pass
def midexp(): pass
def midinf(): pass
def midpnt(): pass
def midsql(): pass
def midsqu(): pass
def mmid(): pass
def mnbrak(): pass
def mnewt(): pass

def moment(data):
    """Calculates moment from a list of numerical data. Ref: NRP 13.1
    
    @param data: a 1-dimensional list of numerical values
    @return: (ave, adev, sdev, var, skew, kurt) where 
            ave = mean
            adev = average deviation
            sdev = standard deviation
            var = variance
            skew = skew
            kurt = kurtosis
    """
    s = 0.0
    for d in data: s = s + d
    ave = s/len(data)
    adev = 0.0
    svar = 0.0
    skew = 0.0
    kurt = 0.0
    for d in data:
        s = d - ave
        adev = adev + abs(s)
        p = s*s
        svar = svar + p
        p = p*s
        skew = skew + p
        p = p*s
        kurt = kurt + p
    adev = adev/len(data)
    svar = svar/(len(data) - 1)
    sdev = math.sqrt(svar)
    if svar <> 0.0:
        skew = skew/(len(data)*sdev*sdev*sdev)
        kurt = (kurt/(len(data)*svar*svar)) - 3.0
    return (ave, adev, sdev, var, skew, kurt)

def mprove(): pass
def mrqmin(): pass
def odeint(): pass
def pcshft(): pass
def pearsn(): pass
def piksr2(): pass
def piksrt(): pass
def plgndr(): pass
def poidev(): pass
def poicoe(): pass
def polcof(): pass
def poldiv(): pass
def polin2(): pass
def polint(): pass
def powell(): pass
def predic(): pass
def probks(): pass
def pzextr(): pass
def qcksrt(): pass
def qgaus(): pass
def qromb(): pass
def qromo(): pass
def qroot(): pass
def qsimp(): pass
def qtrap(): pass
def quad3d(): pass
def ran0(): pass
def ran1(): pass
def ran2(): pass
def ran3(): pass
def ran4(): pass
def rank(): pass
def ratint(): pass
def realft(): pass
def rk4(): pass
def rkdumb(): pass
def rkqc(): pass
def rtbis(): pass
def rtflsp(): pass
def rtnewt(): pass
def rtsafe(): pass
def rtsec(): pass
def rzextr(): pass
def scrsho(): pass
def sfroid(): pass
def shell(): pass
def shoot(): pass
def shootf(): pass
def simplx(): pass
def sinft(): pass
def smooft(): pass
def sncndn(): pass
def solvde(): pass
def sor(): pass
def sort(): pass
def sort2(): pass
def sort3(): pass
def sparse(): pass
def spctrm(): pass
def spear(): pass
def splie2(): pass
def splin2(): pass
def spline(): pass
def splint(): pass
def svbksb(): pass
def svdcmp(): pass
def svdfit(): pass
def svdvar(): pass
def toeplz(): pass
def tptest(): pass
def tqli(): pass
def trapzd(): pass
def tred2(): pass
def tridag(): pass
def ttest(): pass
def tutest(): pass
def twofft(): pass
def vander(): pass
def zbrac(): pass
def zbrak(): pass
def zbrent(): pass
def zroots(): pass

def airy(): pass
def amebsa(): pass
def anorm2(): pass
def arcmak(): pass
def arcode(): pass
def arcsum(): pass
def banbks(): pass
def bandec(): pass
def banmul(): pass
def beschb(): pass
def bessik(): pass
def bessjy(): pass
def broydn(): pass
def choldc(): pass
def cholsl(): pass
def cisi(): pass
def cosft1(): pass
def cosft2(): pass
def crank(): pass
def cyclic(): pass
def daub4(): pass
def dawson(): pass
def decchk(): pass
def dfridr(): pass
def dftint(): pass
def ei(): pass
def elle(): pass
def ellf(): pass
def ellpi(): pass
def expint(): pass
def fasper(): pass
def fitexy(): pass
def fourfs(): pass
def fred2(): pass
def fredex(): pass
def fredin(): pass
def frenel(): pass
def gaucof(): pass
def gauher(): pass
def gaujac(): pass
def gaulag(): pass
def hpsel(): pass
def hpsort(): pass
def hufapp(): pass
def hufdec(): pass
def hufenc(): pass
def hufmak(): pass
def hypdrv(): pass
def hypgeo(): pass
def hypser(): pass
def icrc(): pass
def icrc1(): pass
def igray(): pass
def ks2d1s(): pass
def ks2d2s(): pass
def linbcg(): pass
def lnsrch(): pass
def lop(): pass
def machar(): pass
def mgfas(): pass
def mglin(): pass
def miser(): pass
def mp2dfr(): pass
def mpdiv(): pass
def mpinv(): pass
def mppi(): pass
def mrqcof(): pass
def newt(): pass
def orthog(): pass
def pade(): pass
def pccheb(): pass
def period(): pass
def psdes(): pass
def pwt(): pass
def pwtest(): pass
def qrdcmp(): pass
def qrsolv(): pass
def qrupdt(): pass
def quadvl(): pass
def ratlsq(): pass
def ratval(): pass
def rc(): pass
def rd(): pass
def rf(): pass
def rj(): pass
def rkqs(): pass
def rlft3(): pass
def rofunc(): pass
def savgol(): pass
def select(): pass
def selip(): pass
def simpr(): pass
def sobseq(): pass
def sphbes(): pass
def sphfpt(): pass
def sphoot(): pass
def spread(): pass
def sprsax(): pass
def sprsin(): pass
def sprspm(): pass
def sprstm(): pass
def sprstp(): pass
def sprstx(): pass
def stifbs(): pass
def stiff(): pass
def stoerm(): pass
def vegas(): pass
def voltra(): pass
def wt1(): pass
def wtn(): pass
def wwghts(): pass
def zrhqr(): pass
def zriddr(): pass
def cdf_poisson(k, x):
    """
    Cummulative density function of Poisson distribution from 0 to k - 1 
    inclusive. No reference implementation. 
    Depend: gammq, gser, gcf, gammln
    Ref: NRP 6.2
    
    @param k: number of times of event occurrence
    @param x: mean of Poisson distribution
    @return: float number - Poisson probability of k - 1 times of occurrence
    with the mean of x
    """
    return gammq(k, x)

def cdf_binomial(k, n, p):
    """
    Cummulative density function of Binomial distribution. No reference
    implementation. 
    Depend: betai, betacf, gammln
    Ref: NRP 6.3
    
    @param k: number of times of event occurrence in n trials
    @param n: total number of trials
    @param p: probability of event occurrence per trial
    @return: float number - Binomial probability  
    """
    return betai(k, n-k+1, p)