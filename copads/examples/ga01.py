######################################################################
# GA Program #1: Simulates random point, deletion, insertion, 
# invertion and translocation mutations.
######################################################################
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'copads'))

from genetic import Chromosome
c = Chromosome([0]*150)
c.rmutate('point', 0.1)
print c.sequence
print
c.rmutate('delete', 0.1)
print c.sequence
print
c.rmutate('insert', 0.1)
print c.sequence
print
c.rmutate('invert', 0.1)
print c.sequence
print
c.rmutate('translocate', 0.1)
print c.sequence
