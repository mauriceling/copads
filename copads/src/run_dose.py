from datetime import datetime
import genetic as g
import dose_world as w
from dose_entities import Chromosome, Organism
from dose_entities import Population, World
from dose_parameters import *

populations = {}
world = World()

for i in range(len(population_names)): 
    populations[population_names[i]] = Population()
    L = population_locations[i]
    world.ecosystem[L[0]][L[1]][L[2]]['organisms'] = \
        len(populations[population_names[i]].agents)

generation_count = 0
while generation_count < maximum_generations:
    generation_count = generation_count + 1
    # Run World.ecoregulate function
    world.ecoregulate()
    
    # For each ecological cell, run World.update_ecology and 
    # World.update_local functions
    for x in range(world.world_x):
        for y in range(world.world_y):
            for z in range(world.world_z):
                world.update_ecology(x, y, z)
                world.update_local(x, y, z)  
                
    # For each organism
    #    Execute genome by Ragaraja interpreter using 
    #       existing cytoplasm, local conditions as input
    #    Update cytoplasm (Organism.status['cytoplasm'])
    #    Add input/output from organism intermediate_condition of local cell
    population_names = populations.keys()
    
    # For each population
    #    Run Population.prepopulation_control function
    #    Run Population.mating function and add new organisms to cell
    #    For each organism, run Organism.mutation_scheme function
    #    Run Population.generation_events function
    #    Add 1 to generation count
    #    Run Population.report function
    #    Fossilize population if needed
    for name in population_names:
        report = populations[name].generation_step()
        if generation_count % int(fossilized_frequency) == 0:
            ffile = fossil_files[name] + '_'
            populations[name].freeze(ffile, fossilized_ratio)
            
    # For each ecological cell
    #    Run World.organism_movement function
    #    Run World.organism_location function
    for x in range(world.world_x):
        for y in range(world.world_y):
            for z in range(world.world_z):
                world.organism_movement(x, y, z)
                world.organism_location(x, y, z)
    
    # Administrative tasks
    if generation_count % int(print_frequency) == 0:
        print str(generation_count), str(report)
        for name in population_names:
            f = open(result_files[name] + '.result', 'a')
            dtstamp = str(datetime.utcnow())
            f.write('\t'.join([dtstamp, str(generation_count),
                               str(report)]))
            f.write('\n')
            f.close()