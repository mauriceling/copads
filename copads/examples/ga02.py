######################################################################
# GA Program #2: Simulates different rates of mutation (5 to 25% above
# background mutation rate. Fitness is the average of the chromosome
# where 1-4 is allowed; hence, all 4 organisms should converge to the
# average of 2.5 but at different rates.
######################################################################
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'copads'))
    
import genetic as g
c = g.Chromosome([0]*200, [1,2,3,4])
o = g.Organism([c])
oset = [o.clone() for x in range(5)]
print 'Generation \tMutation rate above background rate'
print 'Count \t\t', '\t'.join(['5%', '10%', '15%', '20%', '25%'])
print '=' * 60
for x in xrange(100):
    print x,'\t\t', '\t'.join([str(oset[x].fitness()) for x in range(5)])
    for mut in range(1, 6):
        oset[mut-1].mutation_scheme('point', float(mut)/20)