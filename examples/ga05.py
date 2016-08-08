######################################################################
# GA Program #5: Simulates an initial population of 200 organisms to 
# reach the goal of having all 4s for their genome, from genome size
# of 200 to 1500 in 100 base increments
######################################################################
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'copads'))

import genetic as g

pdata = \
{
    'nucleotide_list' : [1, 2, 3, 4],
    'chromosome_length' : 200,
    'chromosome_type' : 'defined',
    'chromosome' : [1] * 200,
    'background_mutation' : 0.0001,
    'genome_size' : 1,
    'population_size' : 200,
    'fitness_function' : 'default',
    'mutation_scheme' : 'default',
    'additional_mutation_rate' : 0.01,
    'mutation_type' : 'point',
    'goal' : 4,
    'maximum_generation' : 5000,
    'prepopulation_control' : 'default',
    'mating' : 'default',
    'postpopulation_control' : 'default',
    'generation_events' : 'default',
    'report' : 'default'
}

for chromosome_length in range(200, 1600, 100):
    pdata['chromosome'] = [0] * chromosome_length
    pop = g.population_constructor(pdata)
    g.population_simulate(pop, 100, 'never', 'pop', 0.1, 
                          str(chromosome_length)+'result.txt')
