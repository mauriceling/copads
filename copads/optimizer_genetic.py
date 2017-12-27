'''
Optimizer using Genetic Algorithm
Date created: 27th December 2017
Licence: Python Software Foundation License version 2
'''

from copy import deepcopy

class OptimizationTarget(object):
    def __init__(self):
        self.chromosomes = {}
        self.chromosomes_lower_bounds = {}
        self.chromosomes_upper_bounds = {}
        self.targets = []
        self.results = []
        self.comparatorData = []
        self.comparatorResult = 0

    def dataFunction(self):
        self.comparatorData = []
    
    def comparatorFunction(self):
        self.comparatorResult = 0
    
    def runnerFunction(self):
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
        self.error = 100000
        
    def _processPopulation(self):
        for i in range(len(self.population)):
            self.population.runnerFunction()
            self.population.dataFunction()
            self.population.comparatorFunction()
    
    def _testTolerance(self, tolerance):
        result = [False for i in range(len(self.population))]
        for i in range(len(self.population)):
            if self.population[i].comparatorResults =< tolerance:
                result[i] = True
        return result
        
    def _mutate(self):
        if self.mutateFunction == 'random':
            self.population = self._mutateRandom(self.population)
        elif callable(self.mutateFunction):
            self.population = self.mutateFunction(self.population)
        
    def _mate(self):
        if self.mutateFunction == 'top50':
            self.population = self._mateTop50(self.population)
        elif callable(self.mutateFunction):
            self.population = self.mateFunction(self.population)
        
    def run(self, tolerance=0.1):
        while (self.generation < self.max_generation) and (self.error > tolerance):
            self._processPopulation()
            populationStatus = self._testTolerance(tolerance)
            if True in populationStatus:
                return (self.generation, self.population)
            self._mutate()
            self._mate()
            self.generation = self.generation + 1
        
    def _mutateRandom(self, population):
        pass
    
    def _mateTop50(self, population):
        pass
    
