"""
COPADS (Collection of Python Algorithms and Data Structures).

The main aim of COPADS is to develop a compilation of of Python data 
structures and its algorithms, making it almost a purely developmental 
project. Personally, I look at this as a re-usable collection of tools 
that I can use in other projects. Therefore, this project is essentially 
"needs-driven", except a core subset of data structures and algorithms. 

This project originated from 3 threads of thought. Firstly, while browsing 
through Mehta and Sahni's Handbook of Data Structures and Applications, I 
thought there might be utility to have a number of the listed data 
structures implemented in Python. Given my interest in biological data 
management, having a good set of data structures is always handy. The 2nd 
thread of thought came from Numerical Recipes. Again, I thought these 
algorithms will be handy to have and had started to translate some of 
them into Python during some overly energetic days. Finally, Python 
Cookbook had undergone 2 editions by 2008 and ActiveState had provided an 
online platform for Python Recipes which I found to be useful and can see 
how some of these recipes can be merged. Thus, COPADS is borned.

Project website: U{https://github.com/copads/copads}

License: Unless specified otherwise, all parts of this package, except 
those adapted, are covered under Python Software Foundation License 
version 2.
"""

__version__ = '0.5.0'

__author__ = 'Maurice H.T. Ling <mauriceling@acm.org>'

__copyright__ = '(c) 2007-2016, Maurice H.T. Ling.'

# Data Structures
from .bag import Bag
from .dataframe import Dataframe
from .dataframe import MultiDataframe
from .dataframe import Series
from .graph import Graph
from .matrix import Matrix
from .matrix import Vector
from .parallelarray import ParallelArray
from .prioritydictionary import PriorityDictionary
from .ring import RingList

# Operational classes
from .randomize import MersenneTwister
from .randomize import LCG
from .randomize import CLCG
from .statisticsdistribution import BetaDistribution
from .statisticsdistribution import BinomialDistribution
from .statisticsdistribution import CauchyDistribution
from .statisticsdistribution import ChiSquareDistribution
from .statisticsdistribution import CosineDistribution
from .statisticsdistribution import ErlangDistribution
from .statisticsdistribution import ExponentialDistribution
from .statisticsdistribution import FDistribution
from .statisticsdistribution import FrechetDistribution
from .statisticsdistribution import FurryDistribution
from .statisticsdistribution import GammaDistribution
from .statisticsdistribution import GeometricDistribution
from .statisticsdistribution import HypergeometricDistribution
from .statisticsdistribution import LogarithmicDistribution
from .statisticsdistribution import NormalDistribution
from .statisticsdistribution import PoissonDistribution
from .statisticsdistribution import SemicircularDistribution
from .statisticsdistribution import TDistribution
from .statisticsdistribution import TriangularDistribution
from .statisticsdistribution import UniformDistribution
from .statisticsdistribution import WeiBullDistribution

# Operational functions
from . import entropy
from . import hash
from . import hypothesis
from . import nrpy
from . import objectdistance

# Type-casting functions
from .typecast import tc_Dataframe_Series
from .typecast import tc_Dataframe_MultiDataframe
from .typecast import tc_List_Dictionary
from .typecast import tc_MultiDataframe_Dataframe
from .typecast import tc_Series_Dataframe
from .typecast import tc_Series_Dictionary
from .typecast import tc_Series_List
from .typecast import tc_Series_Vector
from .typecast import tc_Vector_List
from .typecast import tc_Vector_Dictionary
