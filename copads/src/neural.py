'''
Framework for Neural Network Applications
Date created: 10th May 2013
License: Python Software Foundation License version 2
'''
import random
import copy

# -------------------------------------------------------------------
# Transfer functions and its inverse and derivative
# -------------------------------------------------------------------
def tf_linear(x): 
    '''Linear transfer function.
    Equation: y = x'''
    y = x
    return y
    
def itf_linear(y): 
    '''Linear transfer function - inverse.
    Equation: x = y'''
    x = y
    return x
    
def dtf_linear(x): 
    '''Linear transfer function - derivative.
    Equation: df = 1.0'''
    df = 1.0
    return df
# -------------------------------------------------------------------
# END - Transfer functions and its inverse and derivative
# -------------------------------------------------------------------


class Neuron:
    '''
    Class for a Neuron.
    
    1. Each neuron is identified by a unique name, which will be used 
    for mapping between different neurons.
    2. The synaptic weights to modulate incoming signals are given in
    "weights" dictionary.
    3. A dictionary, named "cellbody", is provided to contain any other
    information needed. For example, it can be used to contain a timer
    for time-delayed neuron activation or it can be used for neuronal
    memory.
    '''
    name = None
    weights = {}
    cellbody = {}
    transfer_function = None
    itransfer_function = None
    dtransfer_function = None
    
    def __init__(self, transfer_function=tf_linear,
                 itransfer_function=itf_linear,
                 dtransfer_function=dtf_linear, name=None):
        '''
        Constructor method for Neuron class.
        
        @param transfer_function: a function to convert the consolidated
        weighted input for the neuron and generate an output signal. 
        Default = tf_linear; that is, output signal = consolidated 
        weighted input.
        @type transfer_function: function
        @param itransfer_function: inverse of transfer_function, 
        used by some learning algorithms, Default = itf_linear
        @type itransfer_function: function
        @param dtransfer_function: differential of transfer_function, 
        used by some learning algorithms, Default = dtf_linear
        @type dtransfer_function: function
        @param name: unique name of the neuron. Default = a string of
        60 to 75 numbers.
        @type name: string
        '''
        self.transfer_function = transfer_function
        self.dtransfer_function = dtransfer_function
        if name != None:
            self.name = str(name)
        else:
            name = str(int(random.random() * 1e15))
            name = name + str(int(random.random() * 1e15))
            name = name + str(int(random.random() * 1e15))
            name = name + str(int(random.random() * 1e15))
            self.name = name + str(int(random.random() * 1e15))
            
    def generate_name(self):
        '''
        Generate a new random name (a string of 60 to 75 numbers) for
        the current neuron.
        
        @return: new name of neuron.
        '''
        self.name = str(int(random.random() * 1e15)) + \
                    str(int(random.random() * 1e15)) + \
                    str(int(random.random() * 1e15)) + \
                    str(int(random.random() * 1e15)) + \
                    str(int(random.random() * 1e15))
        return self.name
            
    def connect(self, incoming_neuron):
        '''
        Connects a neuron to the current neuron - by designating an 
        initial synaptic weight of 0.01 on the input of the incoming 
        neuron. The incoming neuron must not been previously connected. 
        Use set_synaptic_weight method to set/reset existing synaptic 
        weight.
        
        @param incoming_neuron: name of incoming neuron to be connected.
        @type incoming_neuron: string
        '''
        incoming_neuron = str(incoming_neuron)
        if incoming_neuron in self.weights:
            raise AttributeError('Neuron name, %s, had been previously \
            connected. Unable to reconnect neuron as this operation \
            will reset the synaptic weight from this neuron. Use \
            set_synaptic_weight method instead.' % incoming_neuron)
        else:
            self.weights[incoming_neuron] = 0.01
            
    def set_synaptic_weight(self, incoming_neuron, weight=0.01):
        '''
        Set or reset synaptic weight of existing connected neuron.
        
        @param incoming_neuron: name of incoming neuron to be set.
        @type incoming_neuron: string
        @param weight: synaptic weight, default = 0.01
        @type weight: float
        '''
        incoming_neuron = str(incoming_neuron)
        if incoming_neuron in self.weights:
            self.weights[incoming_neuron] = float(weight)
        else:
            raise AttributeError('Incoming neuron name, %s, had NOT \
            been previously connected. Unable to set synaptic weight \
            of unconnected neuron. Use connect method to establish \
            a connection from incoming neuron.' % incoming_neuron)
            
    def set_transfer_functions(self, transfer_function,
                              itransfer_function=None,
                              dtransfer_function=None):
        '''
        Set transfer function, its inverse and differential functions.
        
        @param transfer_function: a function to convert the consolidated
        weighted input for the neuron and generate an output signal. 
        @type transfer_function: function
        @param itransfer_function: inverse of transfer_function, 
        used by some learning algorithms, Default = None
        @type itransfer_function: function
        @param dtransfer_function: differential of transfer_function, 
        used by some learning algorithms, Default = None
        @type dtransfer_function: function
        '''
        self.transfer_function = transfer_function
        self.itransfer_function = itransfer_function
        self.dtransfer_function = dtransfer_function
        
    def execute(self, activations):
        '''
        Execute/activate the neuron into action.
        
        @param activations: a dictionary of current activations of the 
        entire network where keys are the names of neurons and values 
        are the activation state or current output signal.
        @type activations: dictionary
        @return: activations dictionary with the updated output signal 
        or activation state from the current neuron.
        '''
        synaptic_input = 0.0
        for key in self.weights.keys():
            try: 
                synaptic_input = synaptic_input + \
                    (self.weights[key] * float(activations[key]))
            except KeyError: pass
        synaptic_input = float(synaptic_input)
        signal = self.transfer_function(synaptic_input)
        activations[self.name] = signal
        return activations
        
 
class Brain:
    '''
    Class for the neural network.
    '''
    activations = {}
    neuron_pool = {}
    activation_sequence = []
    learning_algorithm = None
    
    def __init__(self, number_of_neurons=0,
                 original_neuron=None,
                 list_of_neuron_names=[],
                 learning_algorithm=None):
        '''
        Constructor method for Brain class.
        
        A brain or neural network can be constructed by a predefined 
        list of unique names for neurons or by stating the number of
        neurons required. In both cases, a pre-created neuron may be 
        used but is not mandatory. However, in event where both the 
        list of unique names for neurons and the number of neurons 
        required are given, the list of unique names for neurons takes
        precedence - for example, if 5 neuron names but 10 neurons are
        required, then only 5 neurons (which are named) will be created.
        
        @param number_of_neurons: number of neurons requested (takes a 
        lower precedence than the names of neurons), default = 0.
        @type number_of_neurons: integer
        @param original_neuron: a pre-created neuron to duplicate, 
        default = None
        @type original_neuron: Neuron object
        @param list_of_neuron_names: names for neurons to be created
        (takes a higher precedence than the number of neurons requested), 
        default = [] (empty list).
        @type list_of_neuron_names: list
        @param learning_algorithm: learning mechanism for brain
        @type learning_algorithm: function
        '''
        self.learning_algorithm = learning_algorithm
        if len(list_of_neuron_names) > 0:
            number_of_neurons = len(list_of_neuron_names)
        else:
            number_of_neurons = int(number_of_neurons)
        if (original_neuron == None) and (len(list_of_neuron_names) == 0):
            for x in range(number_of_neurons):
                new_neuron = Neuron()
                self.neuron_pool[new_neuron.name] = new_neuron
                self.activations[new_neuron.name] = 0.0
        elif (original_neuron == None) and (len(list_of_neuron_names) > 0):
            for name in list_of_neuron_names:
                new_neuron = Neuron()
                new_neuron.name = name
                self.neuron_pool[name] = new_neuron
                self.activations[name] = 0.0
        elif (original_neuron != None) and (len(list_of_neuron_names) == 0):
            for x in range(number_of_neurons):
                new_neuron = copy.deepcopy(original_neuron)
                self.neuron_pool[new_neuron.name] = new_neuron
                self.activations[new_neuron.name] = 0.0
        else: # (original_neuron != None) and (len(list_of_neuron_names) > 0)
            for name in list_of_neuron_names:
                new_neuron = copy.deepcopy(original_neuron)
                new_neuron.name = name
                self.neuron_pool[name] = new_neuron
                self.activations[name] = 0.0
        