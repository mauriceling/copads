import sys
import os
import copy
import unittest

sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'src'))
import neural as n


class testNeuron(unittest.TestCase):
    def setUp(self):
        self.cell = n.Neuron('nA')
    def testName(self):
        self.assertEqual(self.cell.name, 'nA')
    def testGenerate_Name(self):
        name1 = self.cell.generate_name()
        self.assertEqual(self.cell.name, name1)
        name2 = self.cell.generate_name()
        self.assertEqual(self.cell.name, name2)
        self.assertNotEqual(name1, name2)
#    def testExecute1(self):
#        self.cell.connect('nB')
#        self.cell.connect('nC')
#        self.cell.connect('nD')
#        activations = {'nA': 0.0, 'nB': 1, 'nC': 2, 'nD': 3}
#        activations = self.cell.execute(activations)
#        self.assertEqual(self.cell.weights, 
#                         {'nB': 0.01, 'nC': 0.01, 'nD': 0.01})
#        result = 1*0.01 + 2*0.01 + 3*0.01
#        self.assertEqual(activations['nA'], result)
#        self.assertEqual(activations['nB'], 1)
#        self.assertEqual(activations['nC'], 2)
#        self.assertEqual(activations['nD'], 3)
#        self.cell.disconnect_all()
#    def testExecute2(self):
#        self.cell.connect('nB')
#        self.cell.connect('nC')
#        self.cell.connect('nD')
#        activations = {'nA': 0.0, 'nB': 1, 'nC': 2, 'nD': 3}
#        self.cell.set_synaptic_weight('nC', 0.5)
#        activations = self.cell.execute(activations)
#        self.assertEqual(self.cell.weights, 
#                         {'nB': 0.01, 'nC': 0.5, 'nD': 0.01})
#        result = 1*0.01 + 2*0.5 + 3*0.01
#        self.assertEqual(activations['nA'], result)
#        self.assertEqual(activations['nB'], 1)
#        self.assertEqual(activations['nC'], 2)
#        self.assertEqual(activations['nD'], 3)
#        self.cell.disconnect_all()
#    def testExecute3(self):
#        self.cell.connect('nB')
#        self.cell.connect('nC')
#        self.cell.connect('nD')
#        self.cell.disconnect('nB')
#        activations = {'nA': 0.0, 'nB': 1, 'nC': 2, 'nD': 3}
#        self.assertEqual(self.cell.weights, {'nC': 0.01, 'nD': 0.01})
#        activations = self.cell.execute(activations)
#        result = 2*0.01 + 3*0.01
#        self.assertEqual(activations['nA'], result)
#        self.assertEqual(activations['nB'], 1)
#        self.assertEqual(activations['nC'], 2)
#        self.assertEqual(activations['nD'], 3)
#        self.cell.disconnect_all()
        
        
#class testBrain(unittest.TestCase):
#    def testInit1(self):
#        brain = n.Brain(5)
#        names = brain.activations.keys()
#        self.assertEqual(brain.neuron_pool.keys(), names)
#        self.assertEqual(brain.synapses.keys(), names)
#        self.assertEqual(brain.activations[names[1]], 0.0)
#        self.assertEqual(brain.synapses[names[1]], [])
#        brain.remove_all_neurons()
#        self.assertEqual(brain.neuron_pool, {})
#    def testInit2(self):
#        names = ['nA', 'nB', 'nC']
#        brain = n.Brain(list_of_neuron_names=names)
#        self.assertEqual(brain.neuron_pool.keys(), names)
#        self.assertEqual(brain.synapses.keys(), names)
#        self.assertEqual(brain.activations[names[1]], 0.0)
#        self.assertEqual(brain.synapses[names[1]], [])
#        brain.remove_all_neurons()
#        self.assertEqual(brain.neuron_pool, {})
        
        
if __name__ == '__main__':
    unittest.main()