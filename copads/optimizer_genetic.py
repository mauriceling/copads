'''
Optimizer using Genetic Algorithm
Date created: 27th December 2017
Licence: Python Software Foundation License version 2
'''

import random
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
    targetResults and comparatorData to generate a fitnessScore. The higher
    the fitness score, the fitter the organism and the higher chances it
    gets into the next generation.

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
        achieves the required fitness score. The higher the fitness
        score, the fitter the organism and the higher chances it
        gets into the next generation.
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
    '''
    Genetic algorithm (GA) optimizer class.

    This class takes an OptimizationTarget object (which represents an
    individual organism) and replicates it to the required population size
    and store them in population dictionary (where the keys represents the
    sample IDs). These sample IDs will be reused over generations; hence,
    have to take account of population count to be unique. Two functions
    needs to be defined - mutate (which mutates the chromosomes in
    population[ID].chromosomes and are bounded by population[ID].
    chromosomes_lower_bounds and population[ID].chromosomes_upper_bounds
    for lower and upper value boundaries respectively), and mate (which
    eliminates unfit organisms and mates fit organisms for the next
    generation). There is a defined set of mating and mutation methods
    pre-defined but these can be overrode. The run method performs GA
    optimization on the population.
    '''
    def __init__(self, optTarget, population_size=10, max_generations=100):
        '''
        Constructor method.

        @param optTarget: object to optimize.
        @type optTarget: optimizer_genetic.OptimizationTarget object
        @param population_size: number of organisms in population (Default
        = 10).
        @type population_size: integer
        @param max_generations: maximum number of generations to optimize
        (Default = 10).
        @type max_generations: integer
        '''
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
        '''
        Method to set mutation scheme. Allowable mutation schemes are:
            - random

        @param name: name of mutation scheme (Default = random).
        @type name: string
        '''
        availableMutates = ['random']
        if str(name) in availableMutates:
            self.mutateFunction = str(name)
        elif callable(name):
            self.mutateFunction = name
        else:
            self.mutateFunction = 'random'

    def _mutate(self):
        '''
        Private method to run a specific mutation scheme based on the value in
        self.mutateFunction.
        '''
        if self.mutateFunction == 'random':
            self.population = self._mutateRandom(self.population)
        elif callable(self.mutateFunction):
            self.population = self.mutateFunction(self.population)

    def setMate(self, name='top50fission'):
        '''
        Method to set mating scheme. Allowable mating schemes are:
            - top50fission

        @param name: name of mating scheme (Default = top50fission).
        @type name: string
        '''
        availableMates = ['top50fission']
        if str(name) in availableMates:
            self.mateFunction = str(name)
        elif callable(name):
            self.mateFunction = name
        else:
            self.mateFunction = 'top50fission'

    def _mate(self):
        '''
        Private method to run a specific mating scheme based on the value in
        self.mateFunction.
        '''
        if self.mateFunction == 'top50':
            self.population = self._mateTop50(self.population)
        elif callable(self.mateFunction):
            self.population = self.mateFunction(self.population)

    def run(self):
        '''
        Method to run the GA optimizer, which will execute the following steps
        until one of the organism is fitted (OptimizationTarget.fitted == True)
        or the maximum generation is reached:
            - for each organism, execute runnerFunction()
            - for each organism, execute dataFunction()
            - for each organism, execute comparatorFunction()
            - if none of the organisms is fitted, execute mutate function and
            mate function

        However, all organisms in the population will undergo mutation before
        the first execution. This is to prevent all organisms from getting the
        same fitness score at the first generation as all organisms are clones
        of each other at instantiation.

        @return: (generation count, population dictionary)
        '''
        if self.generations == 0:
            self._mutate()
        while (self.generations < self.max_generations):
            for i in range(len(self.population)):
                self.population[i].runnerFunction()
                self.population[i].dataFunction()
                self.population[i].comparatorFunction()
            if True in [self.population[i].fitted
                        for i in range(len(self.population))]:
                return (self.generation, self.population)
            self._mutate()
            self._mate()
            self.generations = self.generations + 1

    def _mutateRandom(self, population):
        '''
        Private method - random mutation scheme (mutation scheme = random). In
        this scheme, each of the chromosome is randomly mutated. A random float
        (multiplier) between 0 and 2 will be generated for each element on the
        chromosome. If the multiplier is lower than 1, then the data value of
        the element on the chromosome will be reduced. if the multipler is more
        than 1, then the data value of the element on the chromosome will be
        increased.

        @param population: population to mutate
        @type population: dictionary
        @return: mutated population
        '''
        def mutateChromosome(chr, lower, upper):
            for i in range(len(chr)):
                multiplier = random.randint(0, 2000) / float(1000)
                if multiplier < 1:
                    gap = chr[i] - lower[i]
                    chr[i] = chr[i] - (gap * multiplier)
                else:
                    multiplier = multiplier - 1
                    gap = upper[i] - chr[i]
                    chr[i] = chr[i] + (gap * multiplier)
            return chr
        def mutate(organism):
            for k in organism.chromosomes.keys():
                chr = organism.chromosomes[k]
                lower = organism.chromosomes_lower_bounds[k]
                upper = organism.chromosomes_upper_bounds[k]
                organism.chromosomes[k] = mutateChromosome(chr, lower, upper)
            return organism
        for k in population.keys():
            population[k] = mutate(population[k])
        return population

    def _mateTop50Fission(self, population):
        '''
        Private method - top 50% Fission mating scheme (mating scheme =
        top50fission). In this scheme, organisms with fitness score lower than
        thhe average fitness score of the population will be removed. The
        remaining organisms will be randomly selected for cloning / duplication
        to fill up the population.

        @param population: population to mutate
        @type population: dictionary
        @return: mated population
        '''
        def kill(population):
            meanfitness = [population[k].fitnessScore
                           for k in self.population.keys()]
            meanfitness = sum(meanfitness) / len(meanfitness)
            for k in self.population.keys():
                if population[k].fitnessScore < meanfitness:
                    del population[k]
            newpop = {}
            count = 0
            for k in self.population.keys():
                newpop[count] = population[k]
                count = count + 1
            return newpop
        def generate(population):
            fitOrg = population.keys()
            count = max(fitOrg)
            while len(population) < self.population_size:
                ID = random.choice(fitOrg)
                population[count] = deepcopy(population[ID])
                count = count + 1
            return population
        population = kill(population)
        population = generate(population)
        return population




