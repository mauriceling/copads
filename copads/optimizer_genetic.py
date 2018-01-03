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

    def setMate(self, name='top50'):
        '''
        Method to set mating scheme. Allowable mating schemes are:
            - top50

        @param name: name of mating scheme (Default = top50).
        @type name: string
        '''
        availableMates = ['top50']
        if str(name) in availableMates:
            self.mateFunction = str(name)
        elif callable(name):
            self.mateFunction = name
        else:
            self.mateFunction = 'top50'

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

        @return: (generation count, population dictionary)
        '''
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
        '''
        Private method - random mutation scheme (mutation scheme = random).

        @param population: population to mutate
        @type population: dictionary
        '''
        pass

    def _mateTop50(self, population):
        '''
        Private method - top 50% mating scheme (mating scheme = top50).

        @param population: population to mutate
        @type population: dictionary
        '''
        pass

