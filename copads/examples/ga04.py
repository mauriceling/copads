######################################################################
# GA Program #4: Simulates an initial population of 20 organisms to 
# reach the goal of having all 4s for their genome
######################################################################
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'copads'))

import genetic as g
c = g.Chromosome([0]*200, [1,2,3,4])
o = g.Organism([c])
oset = [o.clone() for x in range(20)]
p = g.Population(4.0, 'infinite', oset)
print '\t\t'.join(['Generation', 'Number of', 'Average', 'Percentage'])
print '\t\t'.join(['Count', 'Organism', 'Fitness', 'to Goal'])
print '=' * 70
report = p.generation_step()
while report['% to goal'] < -27:
    print '\t\t'.join([str(report['generation']),
                       str(len(p.agents)),
                       str(report['average fitness']),
                       str(report['% to goal'])])
    if report['generation'] % 500 == 0: p.freeze()
    report = p.generation_step()