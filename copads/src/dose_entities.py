'''
Boiler-plate codes for DOSE (digital organism simulation environment) entities
Date created: 13th September 2012
Licence: Python Software Foundation License version 2 
'''
import copy, random, string

import genetic as g
import dose_world as w
from dose_parameters import *

Chromosome = g.Chromosome([0]*chromosome_size, 
                          ['0','1','2','3','4','5','6','7','8','9'], 
                          background_mutation_rate)
                          
class Organism(g.Organism):
    
    def __init__(self): self.genome = Chromosome.replicate()
    def fitness(self): pass
    def mutation_scheme(self): pass
        
class Population(g.Population):
    
    def __init__(self, pop_size=population_size, 
                 max_gen=maximum_generations):
        self.agents = [Organism() for x in xrange(pop_size)]
        self.generation = 0
        self.maximum_generations = max_gen
    def prepopulation_control(self): pass
    def mating(self): pass
    def postpopulation_control(self): pass
    def generation_events(self): pass
    def report(self): pass
    
class World(w.World):
    def __init__(self, world_x=world_x, world_y=world_y, world_z=world_z):
        super(World, self).__init__(world_x, world_y, world_z)
    def organism_movement(self, x, y, z): pass
    def organism_location(self, x, y, z): pass
    def ecoregulate(self): pass
    def update_ecology(self, x, y, z): pass
    def update_local(self, x, y, z): pass