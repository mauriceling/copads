"""
Loredo, Tom. 2000. Where are the math functions? 
http://mail.python.org/pipermail/python-list/2000-June/671838.html
"""
from math import *

# Exceptions:

max_iters = 'Too many iterations: '

#============= Globals ===============

rt2 = sqrt(2.)
gammln_cof = [76.18009173, -86.50532033, 24.01409822,
    -1.231739516e0, 0.120858003e-2, -0.536382e-5]
gammln_stp = 2.50662827465

#============= Gamma, Incomplete Gamma ===========
    
def gser(a, x, itmax=700, eps=3.e-7):
    """Series approx'n to the incomplete gamma function."""
    gln = gammln(a)
    if (x < 0.):
        raise bad_arg, x
    if (x == 0.):
        return(0.)
    ap = a
    sum = 1. / a
    delta = sum
    n = 1
    while n <= itmax:
        ap = ap + 1.
        delta = delta * x / ap
        sum = sum + delta
        if (abs(delta) < abs(sum)*eps):
            return (sum * exp(-x + a*log(x) - gln), gln)
        n = n + 1
    raise max_iters, str((abs(delta), abs(sum)*eps))


def gcf(a, x, itmax=200, eps=3.e-7):
    """Continued fraction approx'n of the incomplete gamma function."""
    gln = gammln(a)
    gold = 0.
    a0 = 1.
    a1 = x
    b0 = 0.
    b1 = 1.
    fac = 1.
    n = 1
    while n <= itmax:
        an = n
        ana = an - a
        a0 = (a1 + a0*ana)*fac
        b0 = (b1 + b0*ana)*fac
        anf = an*fac
        a1 = x*a0 + anf*a1
        b1 = x*b0 + anf*b1
        if (a1 != 0.):
            fac = 1. / a1
            g = b1*fac
            if (abs((g-gold)/g) < eps):
                return (g*exp(-x+a*log(x)-gln), gln)
            gold = g
        n = n + 1
    raise max_iters, str(abs((g-gold)/g))


def gammp(a, x):
    """Incomplete gamma function."""
    if (x < 0. or a <= 0.):
        raise ValueError, (a, x)
    if (x < a+1.):
        return gser(a,x)[0]
    else:
        return 1.-gcf(a,x)[0]

def gammq(a, x):
    """Incomplete gamma function."""
    if (x < 0. or a <= 0.):
        raise ValueError, repr((a, x))
    if (x < a+1.):
        return 1.-gser(a,x)[0]
    else:
        return gcf(a,x)[0]

#======== Error function, normal CDF and inverse ================

def ncdf_inv(p):
    """Inverse of the normal CDF."""
    c0 = 2.515517
    c1 = 0.802853
    c2 = 0.010328
    d1 = 1.432788
    d2 = 0.189269
    d3 = 0.001308
    
    sign = -1.
    if (p > 0.5):
        sign = 1.
        p = 1. - p
    arg = -2.*log(p)
    t = sqrt(arg)
    g = t - (c0 + t*(c1 + t*c2)) / (1. + t*(d1 + t*(d2 + t*d3)))
    return sign*g


def erfcc(x):
    """Complementary error function."""
    z = abs(x)
    t = 1. / (1. + 0.5*z)
    r = t * exp(-z*z-1.26551223+t*(1.00002368+t*(.37409196+
        t*(.09678418+t*(-.18628806+t*(.27886807+
        t*(-1.13520398+t*(1.48851587+t*(-.82215223+
        t*.17087277)))))))))
    if (x >= 0.):
        return r
    else:
        return 2. - r


def ncdf(x):
    """Cumulative normal dist'n."""
    global rt2
    return 1. - 0.5*erfcc(x/rt2)


def ncdf_sig (nsig):
    """Cummulative normal dist'n inside nsig sigmas.
    ncdf_sig = 1 - 2 * (upper tail) = 1 - erfc(sigfac/rt(2))"""
    global rt2
    return 1. - erfcc(nsig/rt2)

#=============== Chi squared dist'n ==============

def pchisq(chisq, nu):
    """Lower tail area of the chi**2 dist'n with nu dof.
    Note that chisq is *not* the reduced chis**2!"""
    hnu = 0.5 * nu
    hchi = 0.5 * chisq
    return gammp(hnu, hchi)

def qchisq(chisq, nu):
    """Upper tail area of the chi**2 dist'n with nu dof.
    Note that chisq is *not* the reduced chis**2!"""
    hnu = 0.5 * nu
    hchi = 0.5 * chisq
    return gammq(hnu, hchi)


def chisq_crit(nu, p, tol=1.e-5):
    """Critical chi**2 with lower tail area of p for nu dof."""

    #  For the first guess, use the assyptotic normal limit of the
    # chi**2 distribution:  chi**2 ~ N(nu,sqrt(2*nu)).
    chi = nu + ncdf_inv(p)*sqrt(2.*nu)
    pcur = pchisq(chi,nu)
    
    # Now do a Newton-Raphson loop...
    while 1:
        dfdc = (pchisq(1.001*chi,nu) - pcur) / (0.001*chi)
        chi = chi - (pcur - p)/dfdc
        pcur = pchisq(chi,nu)
        if (abs(pcur-p) <= tol):
            return chi

# Allow it to run as a script    
if __name__ == "__main__":
    print 'gammln: ', gammln(0.5)
    print 'gser: ', gser(5., 5.)
    print 'gcf:  ', gcf(5., 7.)
    print 'gammp, gammq: ', gammp(5.,5.), gammq(5.,5.)
    print 'erfcc: ', erfcc(.5)
    print 'ncdf_inv: ', ncdf_inv(0.977), ncdf_inv(0.5)
    print 'ncdf: ', ncdf(1.)
    print 'ncdf_sig: ', ncdf_sig(2.)
    print 'q & p chisq: ', qchisq(4.,1), pchisq(4.,1)
    print 'chisq_crit: ', chisq_crit(1.,0.954)
#gammln:  0.572364942913
#gser:  (0.55950669681645049, 3.1780538301903123)
#gcf:   (0.1729916079093404, 3.1780538301903123)
#gammp, gammq:  0.559506696816 0.440493303184
#erfcc:  0.479500092277
#ncdf_inv:  1.99582818333 1.01006675468e-07
#ncdf:  0.841344738604
#ncdf_sig:  0.95449974022
#q & p chisq:  0.0455002704962 0.954499729504
#chisq_crit:  3.98159563657
