######################################################################
# GA Program #3: Simulates crossover events between 2 chromosomes
######################################################################
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'copads'))

import genetic as g
c1 = g.Chromosome([0]*50, [1,2,3,4])          # integer chromosome
c2 = g.Chromosome(['A']*50, ['A','B','C','D'])  # alphabet chromosome
print 'INITIAL CHROMOSOMES =================================='
print 'Integer chromosome sequence: ' + str(c1.sequence)
print 'Alphabet chromosome sequence: ' + str(c2.sequence)
for x in range(10, 50, 10):
    print
    (g1, g2) = g.crossover(c1, c2, x)
    print 'Crossover at base ' + str(x)
    print 'Integer chromosome sequence: ' + str(g1.sequence)
    print 'Alphabet chromosome sequence: ' + str(g2.sequence)
