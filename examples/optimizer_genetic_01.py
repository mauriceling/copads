import sys, os
sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'copads'))
import optimizer_target as T
import optimizer_genetic as ga

states = [0] * 100

def operation(chromosome):
    value = sum(chromosome)
    return value

def report(generation, population):
  popFitness = [population[k].fitnessScore for k in population.keys()]
  worstFitness = min(popFitness)
  bestFitness = max(popFitness)
  averageFitness = sum(popFitness) / float(len(popFitness))
  print('%s, %.2f, %.2f %.2f' % (generation+1, worstFitness, 
                                 averageFitness, bestFitness))

class target(T.OptimizationTarget):
    def __init__(self):
        super().__init__()
    def runnerFunction(self):
        value = operation(self.states['value'])
        self.executionResults = value
    def dataFunction(self):
        self.comparatorData = self.executionResults
    def comparatorFunction(self):
        self.fitnessScore = 1000 - abs(self.comparatorData - self.targetResults)
    def modifierFunction(self):
        pass

t = target()
t.states['value'] = states
t.states_lower_bounds['value'] = [0] * 100
t.states_upper_bounds['value'] = [9] * 100
t.targetResults = 1000
t.fitnessScore = 0
t.fitted = False

t.runnerFunction()
t.dataFunction()
t.comparatorFunction()
print('Basal Fitness Score: %.7f' % t.fitnessScore)

optimizer = ga.OptimizerGA(t, 100, 100)
optimizer.mutationRate = 0.05
optimizer.setMutate('random')
optimizer.setMate('top50fission')
optimizer.verbose = 0
optimizer.reportFunction = report
optimizer.run()

print(optimizer.bestOrganism.states['value'])
