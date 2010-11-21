######################################################################
# GA Program #4: Simulates an initial population of 200 organisms to 
# reach the goal of having all 4s for their genome
######################################################################
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'copads'))

import genetic as g
g.population_data['maximum_generation'] = 10000
pop = g.population_constructor(g.population_data)
g.population_simulate(pop)

