"""
Package for Genetic Algorithm and Programming.

Copyright (c) Maurice H.T. Ling <mauriceling@acm.org>

Date created: 23rd February 2010
"""
from random import random, randint, randrange

class Chromosome(object):
    """Representation of a linear chromosome."""
    def __init__(self, sequence=[0]*1000, base=[1, 0], 
                 background_mutation=0.0001):
        """
        Sets up a chromosome.
        
        @param sequence: a subscriptable object (list or string) representing
            the sequence of the chromosome. Default = list of 1000 integers.
        @param base: a subscriptable object (list or string) representing
            allowable entities in the sequence. Default = [1, 0].
        @param background_mutation: background mutation rate represented as the 
            probability of number of mutations per base. Default = 0.0001 
            (0.01%).
        """
        self.sequence = sequence
        self.base = base
        self.background_mutation = background_mutation
    
    def rmutate(self, type='point', rate=0.01, start=0, end=-1):
        """
        Random Mutation operator - to simulate random point, insertion, 
        deletion, inversion, gene translocation and gene duplication events.
        
        The start and end parameters are useful for simulating mutational 
        hotspots in the genome.
        
        @param type: type of mutation. Accepts 'point' (point mutation), 
            'insert' (insert a base), 'delete' (delete a base), 'invert'
            (invert a stretch of the chromosome), 'duplicate' (duplicate a
            stretch of the chromosome), 'translocate' (translocate a stretch of
            chromosome to another random position). Default = point.
        @param rate: probability of mutation per base above background
            mutation rate. Default = 0.01 (1%). No mutation event will ever 
            happen if (rate + background_mutation) is less than zero.
        @param start: starting base on the sequence for mutation.
            Default = 0, start of the genome.
        @param end: last base on the sequence for mutation. Default = -1, end of
            the genome.
        """
        if end > len(self.sequence) - 1: end = len(self.sequence) - 1
        if end == -1: end = len(self.sequence) - 1
        if start == end: start = 0
        length = int(end - start)
        mutation = int((self.background_mutation + mrate) * length)
        while mutation > 0:
            position = int(start) + randrange(length)
            new_base = self.base[randrange(len(self.base))]
            if type == 'point': 
                self.sequence[position] = new_base
            if type == 'delete': 
                self.sequence.pop(position)
            if type == 'insert': 
                self.sequence.insert(position, new_base)
            if type == 'duplicate':
                end_pos = randrange(position + 1, end)
                fragment = self.sequence[position:end_pos]
                for i in range(len(fragment)):
                    self.sequence.insert(end_pos + i, fragment[i])
            if type == 'invert':
                end_pos = randrange(position + 1, end)
                fragment = self.sequence[position:end_pos]
                for base in fragment:
                    self.sequence.insert(position, base)
            if type == 'translocate':
                end_pos = randrange(position + 1, end)
                fragment = [self.sequence.pop(position) 
                            for i in range(end_pos - position)]
                insertion_point = randint(len(self.sequence))
                for i in range(len(fragment)):
                    self.sequence.insert(insertion_point + i, fragment[i])
            mutation = mutation - 1
    
    def kmutate(self, type='point', start=0, end=0, sequence=None, tpos=0):
        """
        Known Mutation operator - to simulate a known point, insertion, 
        deletion, inversion, gene translocation or gene duplication event.
        
        The required parameters will be determined by the type of mutation:
            - point requires 
                - start (the position of the base to mutate)
                - sequence (the new base)
            - delete requires
                - start (the position of the base to delete)
            - insert requires
                - start (the position of the base to begin insertion)
                - sequence (list of sequence or a base to insert)
            - invert requires
                - start (the position of the base to start inversion)
                - end (the position of the base to end inversion)
            - duplicate requires
                - start (the position of the starting base to duplicate)
                - end (the position of the last base to duplicate)
            - translocate requires
                - start (the position of the base to start translocation)
                - end (the position of the base to end translocation)
                - tpos (the position of the base insert the translocated 
                    sequence)
                
        @param type: type of mutation. Accepts 'point' (point mutation), 
            'insert' (insert a base), 'delete' (delete a base), 'invert'
            (invert a stretch of the chromosome), 'duplicate' (duplicate a
            stretch of the chromosome), 'translocate' (translocate a stretch of
            chromosome to another random position). Default = point.
        @param start: starting base on the chromosome for mutation.
            Default = 0, start of the genome.
        @param end: last base on the chromosome for mutation. Default = 0.
        @param sequence: list of bases to change to (point mutation) or to 
            insert (insertion mutation)
        @param tpos: position of the chromosome to insert the translocated
            sequence.
        """
        if type == 'point':
            self.sequence[start] = sequence
        if type == 'delete': 
            self.sequence.pop(start)
        if type == 'insert':
            for base in list(sequence):
                self.sequence.insert(start, base)
        if type == 'duplicate':
            fragment = self.sequence[start:end + 1]
            for i in range(len(fragment)):
                self.sequence.insert(end + i, fragment[i])
        if type == 'invert':
            for base in self.sequence[start:end]:
                self.sequence.insert(start, base)
        if type == 'translocate':
            fragment = [self.sequence.pop(start) 
                        for i in range(end - start)]
            for i in range(len(fragment)):
                self.sequence.insert(tpos + i, fragment[i])

    def replicate(self):
        """
        Replicates (deep copy) the chromosome.
        
        @return: a copy of current chromosome.
        """
        return Chromosome(self.sequence, self.base, self.background_mutation)

        
class Genome(object):
    """
    Represents the genome (collection of chromosomes) for use by an organism.
    """
    
    def __init__(self, type=None):
        """
        Sets up a genome for an organism. 
        
        @param type: initialization type of the genome. Accepts 'dummy' 
        chromosome which is basically a chromosome with only one base or a 
        'default' chromosome. Default = None, an empty genome.
        """
        if type == 'dummy':
            self.data = {1: Chromosome([0])}
        elif type == 'default':
            self.data = {1: Chromosome()}
        else: self.data = {}
        
        
class Organism(object):
    """
    An organism represented by a list of chromosomes and a status table.
    
    Pre-defined status are
        1. alive - is the organism alive? True or False.
        2. vitality - percentage of maximum vitality.
        3. age - the current age of the organism
        4. lifespan - pre-defined maximum lifespan. Set to 100.
        5. fitness - how fit the organism is? Set to maximum fitness, 100
        6. death - reason of death (as death code)
    
    List of defined death codes
        1. death01 - zero vitality
        2. death02 - maximum age reached
        3. death03 - unknown death cause
    """
    status = {'alive': True,                # is the organism alive?
              'vitality': 100.0,            # % of vitality
              'age': 0.0,                   # age of the organism
              'lifespan': 100.0,            # maximum lifespan
              'fitness': 100.0,             # % of fitness
              'death': None}
             
    def __init__(self, genome='default', gender=None):
        """
        Sets up a new organism with default status (age = 0, vitality = 100,
        lifespan = 100, fitness = 100, alive = True)
        
        @param genome: Genome object to inherit. Default = 'default', which will
            set up the genome as one default chromosome. It also allows a 
            'dummy' chromosome which is basically a chromosome with only one 
            base - this is for applications which does not utilize the 
            chromosome.
        @param gender: establishes the gender of the organism which may be used
            for mating routines.
        """
        if genome == 'default': 
            self.genome = Genome('default')
        elif genome == 'dummy':
            self.genome = Genome('dummy')
        else: 
            self.genome = genome
        self.gender = gender
    
    def setStatus(self, variable, value):
        """
        Sets new status or change status of the organism. However, the following
        status change will result in death of the organism
            1. 'alive' to False
            2. 'vitality' to or below zero
            3. 'age' to or above lifespan
        
        @param variable: name of status to change
        @param value: new value of the status
        """
        if variable == 'alive' and value == True: 
            self.status['alive'] = value
        if variable == 'alive' and value == False: 
            self.status['alive'] = value
            self.status['death'] = 'death03'
        if variable == 'vitality':
            if float(value) > 100.1:
                self.status['vitality'] = 100.0
            if float(value) > 0.0 and float(value) < 100.1:
                self.status['vitality'] = float(value)
            if float(value) == 0 or float(value) < 0:
                self.status['vitality'] = 0
                self.status['alive'] = False
                self.status['death'] = 'death01'
        elif variable == 'age':
            if float(value) < self.status['lifespan']:
                self.status['age'] = float(value)
            else:
                self.status['age'] = self.status['lifespan']
                self.status['alive'] = False
                self.status['death'] = 'death02'
        else:
            self.status[variable] = value
        
    def getStatus(self, variable):
        try:
            return self.status[variable]
        except:
            raise KeyError('%s not found in organism status' % str(variable))
            
    def clone(self):
        """
        Cloness (deep copy) the organism.
        
        @return: a copy of current organism.
        """
        return Organism(self.genome, self.gender)
        
        
class Population(object):
    """Representation of a population."""
    def __init__(self, size=0):
        self.agents = [0] * size
        self.generation = 0
        
    def add_organism(self, organism):
        self.agents.append(organism)
        