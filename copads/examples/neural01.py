import sys, os
sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'src'))

import neural as n

names = ['A', 'B', 'C', 'D', 'E']
brain = n.Brain(list_of_neuron_names=names)

brain.connect_neurons('A', 'B')
brain.connect_neurons('A', 'C')

print brain.synapses