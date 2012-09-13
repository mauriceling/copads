'''
World structure for DOSE (digital organism simulation environment)
Date created: 13th September 2012
Licence: Python Software Foundation License version 2 
'''
import copy

class World(object):
    '''
    Representation of a 3-dimensional world.
    '''
    ecosystem = {}
    
    def __init__(self, world_x, world_y, world_z):
        eco_cell = {'local_input': [], 'local_output': [],
                    'temporary_input': [], 'temporary_output': [],
                    'organisms': 0}
        self.world_x = int(world_x)
        self.world_y = int(world_y)
        self.world_z = int(world_z)
        for x in range(self.world_x):
            eco_x = {}
            for y in range(self.world_y):
                eco_y = {}
                for z in range(self.world_z): eco_y[z] = copy.deepcopy(eco_cell)
                eco_x[y] = copy.deepcopy(eco_y)
            self.ecosystem[x] = copy.deepcopy(eco_x)
    
    def ecoregulate(self): 
        pass
        
    def organism_movement(self, x, y, z): 
        pass
    def organism_location(self, x, y, z): 
        pass
    
    def update_ecology(self, x, y, z): 
        pass
        
    def update_local(self, x, y, z): 
        pass