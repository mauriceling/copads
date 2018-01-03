'''
Optimizer using Genetic Algorithm
Date created: 27th December 2017
Licence: Python Software Foundation License version 2
'''

from copy import deepcopy

class OptimizationTarget(object):
    '''
    Abstract class to create the object to be optimized. This class 
    is used to created an inherited class, which is the optimization 
    target. In the context of genetic algorithms, the inherited class 
    represents an organism where its chromosome(s) is/are being 
    optimized - so that the reduced execution results (comparatorData) 
    approaches targetResults.
    
    The way the organism executes is as follows: Firstly, The 
    runnerFunction in the inherited class represents the method to 
    execute the chromosomes to generate the executionResults. Secondly, 
    the dataFunction in the inherited class represents the method to 
    select required data variables (reduce the number of data variables) 
    from executionResults into comparatorData. Finally, the 
    comparatorFunction in the inherited class compares between the 
    targetResults and comparatorData to generate a fitnessScore.
    
    There can be one or more chromosomes in each organism; hence, 
    chromosomes are defined as dictionary in this template class.
    
    The chromosomes_lower_bounds and chromosomes_upper_bounds 
    represents the lower and upper bound values of the chromosomes, 
    which can be used during mutation.
    '''
    def __init__(self):
        '''
        Constructor method.
        '''
        self.chromosomes = {}
        self.chromosomes_lower_bounds = {}
        self.chromosomes_upper_bounds = {}
        self.targetResults = []
        self.executionResults = []
        self.comparatorData = []
        self.fitnessScore = 0
        self.fitted = False

    def dataFunction(self):
        '''
        Method to be inherited and represents the selection of 
        self.executionResults into self.comparatorData. For example, 
        self.executionResults may be a list of 100 elements but 
        obnly 10 of the elements are experimentally known (self.
        targetResults) and matched. Hence, the format of self.
        comparatorData should be the same as self.targetResults.
        '''
        self.comparatorData = []
    
    def comparatorFunction(self):
        '''
        Method to be inherited and represent the fitness function, 
        which compares self.comparatorData to self.targetResults 
        and generate a fitness score (self.fitnessScore). This method 
        must set self.fitted to True when the required organism 
        achieves the required fitness score.
        '''
        self.fitnessScore = 0
    
    def runnerFunction(self):
        '''
        Method to be inherited and represents the execution of the 
        organism. This method must use self.chromosomes and the 
        results to be fed into self.executionResults.
        '''
        pass
        
class OptimizerGA(object):
    def __init__(self, optTarget, population_size=10, max_generations=100):
        self.optTarget = optTarget
        self.generations = 0
        self.max_generations = int(max_generations)
        self.population_size = int(population_size)
        self.population = {}
        for i in range(self.population_size):
            self.population[i] = deepcopy(self.optTarget)
        self.mutateFunction = 'random'
        self.matingFunction = 'top50'
    
    def setMutate(self, name='random'):
        availableMutates = ['random']
        if str(name) in availableMutates:
            self.mutateFunction = str(name)
        elif callable(name):
            self.mutateFunction = name
        else:
            self.mutateFunction = 'random'
            
    def _mutate(self):
        if self.mutateFunction == 'random':
            self.population = self._mutateRandom(self.population)
        elif callable(self.mutateFunction):
            self.population = self.mutateFunction(self.population)
    
    def setMate(self, name='top50'):
        availableMates = ['top50']
        if str(name) in availableMates:
            self.mateFunction = str(name)
        elif callable(name):
            self.mateFunction = name
        else:
            self.mateFunction = 'top50'
            
    def _mate(self):
        if self.mutateFunction == 'top50':
            self.population = self._mateTop50(self.population)
        elif callable(self.mutateFunction):
            self.population = self.mateFunction(self.population)
        
    def run(self, tolerance=0.1):
        while (self.generation < self.max_generation):
            for i in range(len(self.population)):
                self.population.runnerFunction()
                self.population.dataFunction()
                self.population.comparatorFunction()
            if True in [self.population[i].fitted 
                        for i in range(len(self.population))]:
                return (self.generation, self.population)
            self._mutate()
            self._mate()
            self.generation = self.generation + 1
        
    def _mutateRandom(self, population):
        pass
    
    def _mateTop50(self, population):
        pass
    
