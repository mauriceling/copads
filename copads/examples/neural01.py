import sys, os
sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'src'))

import neural as n

names = ['A', 'B', 'C', 'D', 'E']
brain = n.Brain(list_of_neuron_names=names)

print brain.neuron_pool['A'], brain.neuron_pool['B']
brain.connect_neurons('B', 'C')

#print 'Weights for A:', brain.neuron_pool['A'].weights
#print 'Weights for B:', brain.neuron_pool['B'].weights
#print 'Weights for C:', brain.neuron_pool['C'].weights
#print 'Weights for D:', brain.neuron_pool['D'].weights
#print 'Weights for E:', brain.neuron_pool['E'].weights
#
#print 'Weights for A:', hex(id(brain.neuron_pool['A'].weights))
#print 'Weights for B:', hex(id(brain.neuron_pool['B'].weights))
#print 'Weights for C:', brain.neuron_pool['C'].weights
#print 'Weights for D:', brain.neuron_pool['D'].weights
#print 'Weights for E:', brain.neuron_pool['E'].weights

print brain.synapses

brain.connect_neurons('A', 'C')
brain.connect_neurons('C', 'D')

print brain.synapses

brain.disconnect_neurons('C', 'D')

print brain.synapses