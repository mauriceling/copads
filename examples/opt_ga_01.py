import sys, os
sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'copads'))
import optimizer_genetic as opt

states = {'A': 5000, 'B': 0, 'C': 0, 'D': 0, 'E': 0,
          'F': 5000, 'G': 0, 'H': 0, 'I': 0, 'J': 0}
transitions = {0: ('J', 'H'), 1: ('E', 'G'), 2: ('A', 'F'), 3: ('I', 'J'),
               4: ('D', 'C'), 5: ('B', 'J'), 6: ('F', 'B'), 7: ('A', 'D'),
               8: ('A', 'E'), 9: ('I', 'E'), 10: ('D', 'J'), 11: ('C', 'A'),
               12: ('J', 'G'), 13: ('E', 'F'), 14: ('G', 'A'), 15: ('A', 'H'),
               16: ('G', 'H'), 17: ('B', 'D'), 18: ('D', 'B'), 19: ('I', 'A'),
               20: ('E', 'H'), 21: ('F', 'H'), 22: ('H', 'A'), 23: ('F', 'A'),
               24: ('G', 'C'), 25: ('C', 'J'), 26: ('A', 'B'), 27: ('C', 'B'),
               28: ('B', 'I'), 29: ('I', 'B'), 30: ('H', 'B'), 31: ('D', 'I'),
               32: ('G', 'B'), 33: ('D', 'A'), 34: ('B', 'A'), 35: ('C', 'G'),
               36: ('D', 'G'), 37: ('H', 'F'), 38: ('G', 'I'), 39: ('F', 'D'),
               40: ('H', 'G'), 41: ('F', 'C'), 42: ('B', 'C'), 43: ('E', 'B'),
               44: ('C', 'F'), 45: ('I', 'C'), 46: ('I', 'H'), 47: ('H', 'D'),
               48: ('C', 'H'), 49: ('J', 'F'), 50: ('G', 'D'), 51: ('F', 'G'),
               52: ('E', 'I'), 53: ('H', 'J'), 54: ('F', 'J'), 55: ('A', 'G'),
               56: ('I', 'D'), 57: ('A', 'I'), 58: ('E', 'A'), 59: ('E', 'D'),
               60: ('F', 'E'), 61: ('I', 'F'), 62: ('C', 'D'), 63: ('F', 'I'),
               64: ('A', 'C'), 65: ('J', 'D'), 66: ('J', 'I'), 67: ('G', 'F'),
               68: ('I', 'G'), 69: ('E', 'J'), 70: ('A', 'J'), 71: ('H', 'I'),
               72: ('D', 'F'), 73: ('C', 'I'), 74: ('J', 'C'), 75: ('E', 'C'),
               76: ('H', 'E'), 77: ('B', 'G'), 78: ('G', 'E'), 79: ('H', 'C'),
               80: ('B', 'F'), 81: ('J', 'B'), 82: ('B', 'H'), 83: ('D', 'E'),
               84: ('B', 'E'), 85: ('D', 'H'), 86: ('J', 'A'), 87: ('G', 'J'),
               88: ('C', 'E'), 89: ('J', 'E')}
rates = [50] * 90

def operation(states, transitions, rates, cycles=1000):
    count = 0
    while count < cycles:
        for t in transitions.keys():
            origin = transitions[t][0]
            destination = transitions[t][1]
            quantity = min(states[origin], rates[t])
            states[origin] = states[origin] - quantity
            states[destination] = states[destination] + quantity
        count = count + 1
    return states

class target(opt.OptimizationTarget):
    def __init__(self):
        super().__init__()
    def runnerFunction(self):
        states = operation(self.states, self.transitions,
                           self.chromosomes['rates'], 1000)
        self.executionResults = states
    def dataFunction(self):
        places = list(self.executionResults.keys())
        places.sort()
        self.comparatorData = [self.executionResults[p] for p in places]
    def comparatorFunction(self):
        differences = [abs(self.targetResults[i]-self.comparatorData[i])
                       for i in range(len(self.targetResults))]
        differences = [(-1)*x for x in differences]
        self.fitnessScore = sum(differences)

t = target()
t.states = states
t.transitions = transitions
t.chromosomes['rates'] = rates
t.chromosomes_lower_bounds['rates'] = [0] * 90
t.chromosomes_upper_bounds['rates'] = [99] * 90
t.targetResults = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
t.fitnessScore = 0
t.fitted = False

t.runnerFunction()
t.dataFunction()
t.comparatorFunction()

optimizer = opt.OptimizerGA(t, 10, 1000000)
optimizer.setMutate('random')
optimizer.setMate('topfission')
optimizer.run()
