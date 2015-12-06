'''
Framework for Neural Network Applications
Date created: 15th June 2015
License: Python Software Foundation License version 2
'''

import math
import sqlite3 as s
from random import random

class brainbase(object):
    '''
    Class to represent data structure of the neuronal network (also known as 
    the brain), using SQLite database.
    '''

    def __init__(self, path):
        '''
        Constructor method - initialize a new brain, or connect to an existing 
        brain.
        
        @param path: full path name of the brain file (implemented as an SQLite 
        database.
        @type path: string
        '''
        self.conn = s.connect(path)
        self.cur = self.conn.cursor()
        braincheck = self._check_brain()
        if True not in braincheck:
            self._format_brain()
        elif False in braincheck:
            self._repair_brain(braincheck)

    def close_brain(self):
        '''
        Closing the brain file.
        '''
        self.conn.commit()
        self.conn.close()
            
    def _check_brain(self):
        '''
        Private method - Checks for the presence of tables in the brain file, 
        as a proxy for checking whether the supplied brain file (in 
        constructor) is a new file or an existing file. If it is new brain, 
        then the tables need to be created.
        '''
        results = [True, True, True, True]
        try:
            self.cur.execute('select max(ID) from neuron')
        except:
            results[0] = False
        try:
            self.cur.execute('select max(ID) from neuron_internal_states')
        except:
            results[1] = False
        try:
            self.cur.execute('select max(ID) from neuron_input_states')
        except:
            results[2] = False
        try:
            self.cur.execute('select max(source) from connectome')
        except:
            results[3] = False
        return results
        
    def _format_brain(self):
        '''
        Private method - Setting up the tables needed for a new brain file.
        '''
        try: 
            self.cur.execute('drop table logfile')
        except s.OperationalError: 
            pass
        self.cur.execute('''
            create table if not exists logfile (
                ID integer primary key autoincrement,
                event text not null)''')
        try: 
            self.cur.execute('drop table neuron')
        except s.OperationalError: 
            pass
        self.cur.execute('''
            create table if not exists neuron (
                ID integer primary key autoincrement,
                name text not null,
                status text not null default 'alive')''')
        try: 
            self.cur.execute('drop table neuron_internal_states')
        except s.OperationalError: 
            pass
        self.cur.execute('''
            create table if not exists neuron_internal_states (
                ID integer not null,
                key text not null,
                value text not null,
                primary key (ID, key))''')
        try: 
            self.cur.execute('drop table neuron_input_states')
        except s.OperationalError: 
            pass
        self.cur.execute('''
            create table if not exists neuron_input_states (
                ID integer not null,
                sourceID text not null,
                value text not null,
                primary key (ID, sourceID))''')
        try: 
            self.cur.execute('drop table connectome')
        except s.OperationalError: 
            pass
        self.cur.execute('''
            create table if not exists connectome (
                source integer not null,
                destination integer not null,
                key text not null default 'weight',
                value text not null,
                primary key (source, destination, key))''')
        self.conn.commit()
    
    def _repair_brain(self, braincheck):
        pass
        
    def log(self, message):
        '''
        Method to insert logging message.
        
        @param message: message to be logged.
        @type message: string
        '''
        self.cur.execute('insert into logfile (event) values (?)', (message,))
        self.conn.commit()
        
    def add_neuron(self, **kwargs):
        '''
        Method to add a new neuron into the brain.
        
        Logging messages::
            - add neuron: ADDNEURON:<ID of new neuron>:<name of new neuron> 
            - set initial neuron internal data: SETININED:<ID of new neuron>:
            <initial neuronal data in dictionary string format>
            
        @param kwargs: initial neuronal data (as dictionary). The following 
        mandatory fields will be added for each neuron::
            - name: user-defined name for the neuron. Default = no_name.
            - summation: type of summation functions. Allowable values are 
            'summation' (averaged input values). Default = summation.
            - transfer: type of transfer / activation functions, which will 
            generate the output value of the neuron. Allowable values are 
            'linear' (neuron output = output from summation function), 
            'sigmoid' (sigmoid curve output). Default = linear.
            - threshold: theshold value of the neuron. Default = 0.5.
            - pstate: initial output value of the neuron. Default = generated 
            random value between 0-1.
        @type kwargs: dictionary
        @return: ID of the new neuron
        '''
        if 'name' not in kwargs:
            name = 'no_name'
        else: 
            name = str(kwargs['name'])
            del kwargs['name']
        if 'summation' not in kwargs:
            kwargs['summation'] = 'summation'
        if 'transfer' not in kwargs:
            kwargs['transfer'] = 'linear'
        if 'threshold' not in kwargs:
            kwargs['threshold'] = '0.5'
        if 'pstate' not in kwargs:
            kwargs['pstate'] = str(random())
        self.cur.execute('insert into neuron (name) values (?)', (name,))
        ID = str(self.cur.lastrowid)
        for key in kwargs:
            self.cur.execute('''
                insert into neuron_internal_states (ID, key, value) 
                values (?,?,?)''', (ID, str(key), str(kwargs[key])))
        self.log('ADDNEURON:' + ID + ':' + name)
        self.log('SETININED:' + ID + ':' + str(kwargs))
        self.conn.commit()
        return ID
        
    def delete_neuron(self, ID):
        '''
        Method to delete a neuron from the brain and all associated synapses.
        
        Logging messages::
            - delete source synapses: DELNES:<ID of neuron to delete>
            - delete destination synapses: DELNED:<ID of neuron to delete>
            - delete internal states: DELNIS:<ID of neuron to delete>
            - delete input states: DELNIN:<ID of neuron to delete>
            - delete neuron: DELNEU:<ID of neuron to delete>
        
        @param ID: ID of neuron to delete
        @type ID: string
        '''
        self.cur.execute('''delete from connectome where source=:ID''', 
                         {'ID': str(ID)})
        self.log('DELNES:' + ID)
        self.cur.execute('''delete from connectome where destination=:ID''',
                         {'ID': str(ID)})
        self.log('DELNED:' + ID)
        self.cur.execute('''delete from neuron_internal_states where ID=:ID''',
                         {'ID': str(ID)})
        self.log('DELNIS:' + ID)
        self.cur.execute('''delete from neuron_input_states where ID=:ID''',
                         {'ID': str(ID)})
        self.log('DELNIN:' + ID)
        self.cur.execute('''delete from neuron where ID=:ID''',
                         {'ID': str(ID)})
        self.log('DELNEU:' + ID)
        self.conn.commit()

    def _check_neuron_presence(self, ID):
        '''
        Private method - Check whether a neuron is present (in existence).
        
        @param ID: ID of the neuron to check.
        @type ID: string
        @return: False if neuron is not found; True if neuron is found.
        '''
        self.cur.execute('select name from neuron where ID=:ID',
                         {'ID': str(ID)})
        if self.cur.fetchone() == None:
            return False
        else:
            return True
                         
    def add_synapse(self, sourceID, destinationID):
        '''
        Method to add a new synapse (connection between 2 neurons) into the 
        brain. When either of the neurons are not present in the brain, 1 or 2 
        neurons (depending whether 1 or both neurons are not found) will be 
        created; however, the ID(s) of the neuron(s) will not be the same as 
        provided. A random weight between 0 to 1 (as synaptic state) will be 
        added.
        
        Logging messages::
            - add synapse: ADDSYN:<ID of source / originating neuron>:<ID of 
            destination / sink neuron>:<initial synaptic weight in dictionary 
            string format>
            
        @param sourceID: ID of source / originating neuron.
        @type sourceID: string
        @param destinationID: ID of destination / sink neuron.
        @type destinationID: string
        '''
        if self._check_neuron_presence(sourceID) == False:
            sourceID = self.add_neuron()
        if self._check_neuron_presence(destinationID) == False:
            destinationID = self.add_neuron()
        kwargs = {'weight': random()}
        for key in kwargs:
            self.cur.execute('''
                insert into connectome (source, destination, key, value) 
                values (?,?,?,?)''',
                (sourceID, destinationID, str(key), str(kwargs[key])))
        self.log('ADDSYN:' + sourceID + ':' + destinationID + ':' + str(kwargs))
        self.conn.commit()
        
    def delete_synapse(self, sourceID, destinationID):
        '''
        Method to delete a synapse (connection between 2 neurons) in the brain.
        
        Logging messages::
            - delete synapse: DELSYN:<ID of source / originating neuron>:<ID of 
            destination / sink neuron>
            
        @param sourceID: ID of source / originating neuron.
        @type sourceID: string
        @param destinationID: ID of destination / sink neuron.
        @type destinationID: string
        '''
        self.cur.execute('''
            delete from connectome where 
            source=:source and destination=:destination''',
            {'source': str(sourceID),
             'destination': str(destinationID)})
        self.log('DELSYN:' + sourceID + ':' + destinationID)
        self.conn.commit()

    def set_synapse_state(self, sourceID, destinationID, 
                          value, state='weight'):
        '''
        Method to set a state in a synapse.
        
        Logging messages::
            - set synaptic state: SETSYNST:<ID of source / originating neuron>:
            <ID of destination / sink neuron>:<state>:<value>
        
        @param sourceID: ID of source / originating neuron.
        @type sourceID: string
        @param destinationID: ID of destination / sink neuron.
        @type destinationID: string
        @param value: value of the state.
        @type value: string
        @param state: state name to set or update.
        @type state: string
        '''
        self.cur.execute('''select value from connectome
                            where source=:sourceID and 
                            destination=:destinationID and 
                            key=:key''', 
                         {'sourceID': str(sourceID),
                          'destinationID': str(destinationID),
                          'key': str(state)})
        if self.cur.fetchone() == None:
            self.cur.execute('''insert into connectome 
                                (source, destination, key, value) values 
                                (?,?,?,?)''',
                             (str(sourceID), str(destinationID), 
                              str(state), value))
        else: 
            self.cur.execute('''update connectome
                                set value=:value
                                where source=:sourceID and 
                                destination=:destinationID and
                                key=:key''',
                             {'value': value,
                              'sourceID': str(sourceID),
                              'destinationID': str(destinationID),
                              'key': str(state)})
        self.log('SETSYNST:' + sourceID + ':' + destinationID + ':' + \
                 str(state) + ':' + str(value))
        self.conn.commit()
        
    def get_synapse_state(self, sourceID, destinationID, state='weight'):
        '''
        Method to get value of a synaptic state.
        
        @type sourceID: string
        @param destinationID: ID of destination / sink neuron.
        @type destinationID: string
        @param state: state name to set or update. Default = weight.
        @type state: string
        @return: value of the synaptic state (if found), or None (if state is 
        not found)
        '''
        self.cur.execute('''select value from connectome
                            where source=:sourceID and 
                            destination=:destinationID and 
                            key=:key''', 
                         {'sourceID': str(sourceID),
                          'destinationID': str(destinationID),
                          'key': str(state)})
        value = self.cur.fetchone()
        if value == None:
            return None
        else:
            return str(value[0])
        
    def get_summation(self, ID):
        '''
        Method to get the summation function type of a neuron.
        
        @param ID: ID of neuron.
        @type ID: string
        @return: summation function type of a neuron (as string).
        '''
        self.cur.execute('''select value from neuron_internal_states
                            where ID=:ID and key=:key''',
                         {'ID': str(ID),
                          'key': 'summation'})
        return self.cur.fetchone()

    def get_transfer(self, ID):
        '''
        Method to get the transfer / activation function type of a neuron.
        
        @param ID: ID of neuron.
        @type ID: string
        @return: transfer / activation function type of a neuron (as string).
        '''
        self.cur.execute('''select value from neuron_internal_states
                            where ID=:ID and key=:key''',
                         {'ID': str(ID),
                          'key': 'transfer'})
        return self.cur.fetchone()

    def get_input_values(self, ID):
        '''
        Method to get the input values vector of a neuron.
        
        @param ID: ID of neuron.
        @type ID: string
        @return: list of input values.
        '''
        self.cur.execute('''select value from neuron_input_states
                            where ID=:ID''',
                         {'ID': str(ID)})
        return [float(str(x[0])) for x in self.cur.fetchall()]

    def set_neuron_state(self, ID, state, value):
        '''
        Method to set a specific state of a neuron.
        
        Logging messages::
            - set neuron internals: SNINTERNAL:<ID of neuron>:<state type of 
            neuron>:<value of the state>
        
        @param ID: ID of neuron.
        @type ID: string
        @param state: type of state to set.
        @type state: string
        @param value: value to set for the state.
        '''
        self.cur.execute('''select value from neuron_internal_states
                            where ID=:ID and key=:key''', 
                         {'ID': str(ID),
                          'key': str(state)})
        if self.cur.fetchone() == None:
            self.cur.execute('''insert into neuron_internal_states 
                                (ID, key, value) values (?,?,?)''',
                             (str(ID), str(state), value))
        else: 
            self.cur.execute('''update neuron_internal_states
                                set value=:value
                                where ID=:ID and key=:key''',
                             {'value': value,
                              'ID': str(ID),
                              'key': str(state)})
        self.log('SNINTERNAL:' + ID + ':' + str(state) + ':' + str(value))
        self.conn.commit()
        
    def get_neuron_state(self, ID, state='pstate'):
        '''
        Method to get a specific state of a neuron.
        
        @param ID: ID of neuron.
        @type ID: string
        @param state: type of state to get. Default = pstate.
        @type state: string
        @return: state value (if present); None (if state is not found).
        '''
        self.cur.execute('''select value from neuron_internal_states
                            where ID=:ID and key=:key''',
                         {'ID': str(ID),
                          'key': str(state)})
        value = self.cur.fetchone()
        if value == None:
            return None
        else:
            return str(value[0])

    def get_next_neurons(self, ID, stype='weight'):
        '''
        Method to get a set of next connected neurons (the destination neurons) 
        from a source neuron.
        
        @param ID: ID of source neuron.
        @type ID: string
        @param stype: type of synaptic state of the synapse (connection) to get. 
        Default = weight.
        @type stype: string
        @return: list of tuples (<ID of destination neuron>, <value of stype>)
        '''
        self.cur.execute('''select destination, value 
                            from connectome
                            where source=:source and key=:stype''',
                         {'source': str(ID),
                          'stype': stype})
        return [(str(x[0]), float(str(x[1])))
                for x in self.cur.fetchall()]

    def set_input_states(self, sourceID, destinationID, value):
        '''
        Method to set an input value of a neuron. It is not mandatory to have 
        established a prior input channel, though recommended.
        
        Logging messages::
            - set neuron input: SNINPUT:<ID of source / originating neuron>:<ID 
            of destination / sink neuron>:<value of input>
            
        @param sourceID: ID of source / originating neuron.
        @type sourceID: string
        @param destinationID: ID of destination / sink neuron.
        @type destinationID: string
        @param value: value of the input.
        '''
        self.cur.execute('''select sourceID, ID 
                            from neuron_input_states
                            where sourceID=:sourceID and
                            ID=:destinationID''',
                         {'sourceID': str(sourceID),
                          'destinationID': str(destinationID)})
        if self.cur.fetchone() == None:
            self.cur.execute('''insert into neuron_input_states
                                (ID, sourceID, value) values (?,?,?)''', 
                             (destinationID, sourceID, value))
        else:
            self.cur.execute('''update neuron_input_states
                                set value=:value
                                where sourceID=:sourceID and
                                ID=:destinationID''',
                             {'value': value,
                              'sourceID': str(sourceID),
                              'destinationID': str(destinationID)})
        self.log('SNINPUT:' + str(sourceID) + ':' + str(destinationID) + \
                 ':' + str(value))
        self.conn.commit()

    def add_external_input(self, source, destinationID, value):
        '''
        Method to set add an external input channel for a neuron or set an 
        external input value into a neuron.
        
        Logging messages::
            - add external input: AEXTIN:<ID of source / originating neuron>:
            <ID of destination / sink neuron>:<value of input>
            
        @param source: ID of source / originating neuron.
        @type source: string
        @param destinationID: ID of destination / sink neuron.
        @type destinationID: string
        @param value: value of the input.
        '''
        self.cur.execute('''select sourceID, ID 
                            from neuron_input_states
                            where sourceID=:source and
                            ID=:destinationID''',
                         {'source': str(source),
                          'destinationID': str(destinationID)})
        if self.cur.fetchone() == None:
            self.cur.execute('''insert into neuron_input_states
                                (ID, sourceID, value) values (?,?,?)''', 
                             (destinationID, source, value))
        else:
            self.cur.execute('''update neuron_input_states
                                set value=:value
                                where sourceID=:sourceID and
                                ID=:destinationID''',
                             {'value': value,
                              'sourceID': str(source),
                              'destinationID': str(destinationID)})
        self.log('AEXTIN:' + str(source) + ':' + str(destinationID) + \
                 ':' + str(value))
        self.conn.commit()
        
    def get_neurons(self, status='alive'):
        '''
        Method to get a list of neurons in the brain according to status.
        
        @param status: status of neurons to get. Default = alive.
        @type status: string
        @return: list of neuron IDs.
        '''
        self.cur.execute('select ID from neuron where status=:status',
                         {'status': str(status)})
        return [str(x[0]) for x in self.cur.fetchall()]
        
    def get_synapses(self, source, stype='weight'):
        '''
        Method to get a list of neurons with a specific input / source type and 
        synaptic type.
        
        @param source: source type (can be ID of source neuron, or name of 
        external source)
        @type source: string
        @param stype: type of synapse. To get all types of synapse, stype = 
        'all'. Default = weight. 
        @type stype: string
        @return: list of destination neuron IDs
        '''
        if stype == 'all':
            self.cur.execute('''
                select destination from connectome 
                where source=:source''',
                {'source': str(source)})
        else:
            self.cur.execute('''
                select destination from connectome 
                where source=:source and key=:stype''',
                {'source': str(source),
                 'stype': str(stype)})
        return [str(x[0]) for x in self.cur.fetchall()]
        
    def get_all_synapses(self):
        '''
        Method to get all synapses.
        
        @return: list of all synapses in tuple of (<source ID>, <destination 
        ID>)
        '''
        self.cur.execute('select distinct source, destination from connectome')
        return [(str(x[0]), str(x[1])) for x in self.cur.fetchall()]
        
    def get_all_synaptic_states(self, stype='weight'):
        '''
        Method to get all synaptic states of a specific type.
        
        @param stype: type of synapse. Default = weight. 
        @type stype: string
        @return: list of synaptic values.
        '''
        self.cur.execute('''
            select value from connectome 
            where key=:key''',
            {'key': str(stype)})
        return [str(x[0]) for x in self.cur.fetchall()]
        
    def get_neuronID_from_name(self, name):
        '''
        Method to get neuron ID from its name.
        
        @param name: name of neuron.
        @type name: string
        @return: ID of neuron (if present); None (if not found).
        '''
        self.cur.execute('''select ID from neuron
                            where name=:name''',
                         {'name': str(name)})
        value = self.cur.fetchone()
        if value == None:
            return None
        else:
            return str(value[0])
            
    def get_name_from_neuronID(self, ID):
        '''
        Method to get neuron name from its ID.
        
        @param ID: ID of neuron.
        @type ID: string
        @return: name of neuron (if present); None (if not found).
        '''
        self.cur.execute('''select name from neuron
                            where ID=:ID''',
                         {'ID': str(ID)})
        value = self.cur.fetchone()
        if value == None:
            return None
        else:
            return str(value[0])
        

class brain(object):
    '''
    Class to represent a neuronal network (also known as the brain), using 
    SQLite database.
    '''

    def __init__(self, path):
        '''
        Constructor method - initialize a new brain, or connect to an existing 
        brain.
        
        @param path: full path name of the brain file (implemented as an SQLite 
        database.
        @type path: string
        '''
        self.base = brainbase(path)
        self.sequence = {}
        for ID in self.base.get_neurons('alive'):
            self.sequence[ID] = None

    def format(self):
        self.base._format_brain()
        
    def add_neuron(self, **kwargs):
        '''
        Method to add a new neuron into the brain.
            
        @param kwargs: initial neuronal data (as dictionary). The following 
        mandatory fields will be added for each neuron::
            - name: user-defined name for the neuron. Default = no_name.
            - summation: type of summation functions. Allowable values are 
            'summation' (averaged input values). Default = summation.
            - transfer: type of transfer / activation functions, which will 
            generate the output value of the neuron. Allowable values are 
            'linear' (neuron output = output from summation function), 
            'sigmoid' (sigmoid curve output). Default = linear.
            - threshold: theshold value of the neuron. Default = 0.5.
            - pstate: initial output value of the neuron. Default = generated 
            random value between 0-1.
        @type kwargs: dictionary
        @return: ID of the new neuron
        '''
        ID = self.base.add_neuron(**kwargs)
        self.sequence[ID] = None
        return ID

    def add_synapse(self, sourceID, destinationID):
        '''
        Method to add a new synapse (connection between 2 neurons) into the 
        brain. When either of the neurons are not present in the brain, 1 or 2 
        neurons (depending whether 1 or both neurons are not found) will be 
        created; however, the ID(s) of the neuron(s) will not be the same as 
        provided. A random weight between 0 to 1 (as synaptic state) will be 
        added.
        
        @param sourceID: ID of source / originating neuron.
        @type sourceID: string
        @param destinationID: ID of destination / sink neuron.
        @type destinationID: string
        '''
        self.base.add_synapse(sourceID, destinationID)
        
    def delete_neuron(self, ID):
        '''
        Method to delete a neuron from the brain and all associated synapses.
        
        @param ID: ID of neuron to delete
        @type ID: string
        '''
        self.base.delete_neuron(ID)
        del self.sequence[ID]
        
    def delete_synapse(self, sourceID, destinationID):
        '''
        Method to delete a synapse (connection between 2 neurons) in the brain.
        
        @param sourceID: ID of source / originating neuron.
        @type sourceID: string
        @param destinationID: ID of destination / sink neuron.
        @type destinationID: string
        '''
        self.base.delete_synapse(sourceID, destinationID)
        
    def _neuron_summation(self, ID):
        '''
        Private method - Calculate a single input (to be used as input for 
        transfer / activation function) from a set of input vectors. If there 
        is no summation function for the neuron or if the calculation returns 
        an error (exception), 0.0 will be returned.
        
        @param ID: ID of neuron to calculate.
        @type ID: string
        @return: calculated input.
        '''
        sum_func = self.base.get_summation(ID)
        if sum_func == None:
            return 0.0
        sum_func = str(sum_func[0])
        neuron_input = self.base.get_input_values(ID)
        try:
            if sum_func == 'summation':
                return sum(neuron_input) / len(neuron_input)
        except: 
            return 0.0

    def _neuron_transfer(self, ID, neuron_input):
        '''
        Private method - Calculate the neuron output, using the transfer / 
        activation function, from the calculated input of the summation 
        function. If there is no transfer / activation function for the neuron 
        or if the calculation returns an error (exception), 0.0 will be 
        returned.
        
        @param ID: ID of neuron to calculate.
        @type ID: string
        @param neuron_input: output from _neuron_summation(), to be used as 
        input for transfer / activation function.
        @type neuron_input: float
        @return: output of transfer / activation function.
        '''
        transfer = self.base.get_transfer(ID)
        if transfer == None:
            return 0.0
        transfer = str(transfer[0])
        try:
            if transfer == 'linear':
                return neuron_input
            elif transfer == 'sigmoid':
                return 1.0 / (1.0 + math.exp(-1.0 * neuron_input))
        except: 
            return 0.0

    def _synaptic_activation(self, ID, state='pstate', stype='weight'):
        '''
        Private method - Calculate each synaptic activation from a source ID 
        and log the values into the respective input vectors of the destination 
        neurons.
        
        @param ID: ID of source neuron.
        @type ID: string
        @param state: state name of neuron as input for synaptic activation. 
        Default = weight.
        @type state: string
        @param stype: name of synaptic state for activation. 
        @type stype: string
        '''
        sourceID = ID
        source_pstate = self.base.get_neuron_state(ID, state)
        for n in self.base.get_next_neurons(ID, stype):
            destinationID = n[0]
            weight = n[1]
            value = weight * float(source_pstate)
            self.base.set_input_states(sourceID, destinationID, value)

    def execute_neuron(self, ID, state='pstate', stype='weight'):
        '''
        Method to execute a neuron. 
        
        The following tasks will be executed for a neuron::
            1. calculate a value from the set of input value vectors
            2. calculate the neuronal output value from (1) using the transfer / 
            activation function
            3. set a neuronal state as the neuronal output value from (2)
            4. activate synapses (using _synaptic_activation function) to 
            generate input vector(s) for destination neuron(s).
        
        @param ID: ID of the neuron to execute.
        @type ID: string
        @param state: state of neuron to store output from transfer / 
        activation function. Default = pstate.
        @type state: string
        @param stype: type of synapse for synaptic activation. Default = weight.
        @type stype: string
        '''
        neuron_input = self._neuron_summation(ID)
        pstate = self._neuron_transfer(ID, neuron_input)
        self.base.set_neuron_state(ID, 'pstate', pstate)
        self._synaptic_activation(ID, state, stype)

    def add_input_channel(self, source, destinationID):
        '''
        Method to add an input channel into a neuron from external source. A 
        random value will be added as the synaptic weight.
        
        @param source: name of external source
        @type source: string
        @param destinationID: ID of target neuron.
        @type destinationID: string
        '''
        self.base.add_external_input(source, destinationID, random())
        
    def get_neurons(self, status='alive'):
        '''
        Method to get a list of neurons in the brain according to status.
        
        @param status: status of neurons to get. Default = alive.
        @type status: string
        @return: list of neuron IDs.
        '''
        return self.base.get_neurons(status)
        
    def get_synapses(self, source, stype='weight'):
        '''
        Method to get a list of neurons with a specific input / source type and 
        synaptic type.
        
        @param source: source type (can be ID of source neuron, or name of 
        external source)
        @type source: string
        @param stype: type of synapse. To get all types of synapse, stype = 
        'all'. Default = weight. 
        @type stype: string
        @return: list of destination neuron IDs
        '''
        return self.base.get_synapses(source, stype)
    
    def get_all_synapses(self):
        '''
        Method to get all synapses.
        
        @return: list of all synapses in tuple of (<source ID>, <destination 
        ID>)
        '''
        return self.base.get_all_synapses()
        
    def get_input_values(self, ID):
        '''
        Method to get the input values vector of a neuron.
        
        @param ID: ID of neuron.
        @type ID: string
        @return: list of input values.
        '''
        return self.base.get_input_values(ID)
    
    def set_neuron_state(self, ID, state, value):
        '''
        Method to set a specific state of a neuron.
        
        Logging messages::
            - set neuron internals: SNINTERNAL:<ID of neuron>:<state type of 
            neuron>:<value of the state>
        
        @param ID: ID of neuron.
        @type ID: string
        @param state: type of state to set.
        @type state: string
        @param value: value to set for the state.
        '''
        self.base.set_neuron_state(ID, state, value)
        
    def get_neuron_state(self, ID, state='pstate'):
        '''
        Method to get a specific state of a neuron.
        
        @param ID: ID of neuron.
        @type ID: string
        @param state: type of state to get. Default = pstate.
        @type state: string
        @return: state value (if present); None (if state is not found).
        '''
        return self.base.get_neuron_state(ID, state)
        
    def set_synapse_state(self, sourceID, destinationID, 
                          value, state='weight'):
        '''
        Method to set a state in a synapse.
        
        @param sourceID: ID of source / originating neuron.
        @type sourceID: string
        @param destinationID: ID of destination / sink neuron.
        @type destinationID: string
        @param value: value of the state.
        @type value: string
        @param state: state name to set or update.
        @type state: string
        '''
        self.base.set_synapse_state(sourceID, destinationID, 
                                    value, state)
        
    def get_synapse_state(self, sourceID, destinationID, state='weight'):
        '''
        Method to get value of a synaptic state.
        
        @type sourceID: string
        @param destinationID: ID of destination / sink neuron.
        @type destinationID: string
        @param state: state name to set or update. Default = weight.
        @type state: string
        @return: value of the synaptic state (if found), or None (if state is 
        not found)
        '''
        return self.base.get_synapse_state(sourceID, destinationID, state)
        
    def get_all_synaptic_states(self, stype='weight'):
        '''
        Method to get all synaptic states of a specific type.
        
        @param stype: type of synapse. Default = weight. 
        @type stype: string
        @return: list of synaptic values.
        '''
        return self.base.get_all_synaptic_states(stype)
        
    def set_input(self, source, inputstates):
        '''
        Method to set input values (from external) into neurons.
        
        @param source: name of external source.
        @type source: string
        @param inputstates: input values from the external source in 
        dictionary; where key is the neuron ID to set the input value, and 
        value is the value. For example, {'1': 0.9, '2': 0.5} means set input 
        for neuron ID 1 as 0.9 and input for neuron ID 2 as 0.5.
        @type inputstates: dictionary
        '''
        for destinationID in inputstates:
            self.base.set_input_states(source, destinationID, 
                                       inputstates[destinationID])
            
    def get_neuronID_from_name(self, name):
        '''
        Method to get neuron ID from its name.
        
        @param name: name of neuron.
        @type name: string
        @return: ID of neuron (if present); None (if not found).
        '''
        return self.base.get_neuronID_from_name(name)
        
    def get_name_from_neuronID(self, ID):
        '''
        Method to get neuron name from its ID.
        
        @param ID: ID of neuron.
        @type ID: string
        @return: name of neuron (if present); None (if not found).
        '''
        return self.base.get_name_from_neuronID(ID)
        
    def delete_orphaned_neurons(self):
        '''
        Method to delete orphaned neurons (neurons without any synapses).
        '''
        synapses = self.get_all_synapses()
        connected_synapses = set([x[0] for x in synapses])
        connected_synapses = connected_synapses | set([x[1] for x in synapses])
        connected_synapses = list(connected_synapses)
        orphans = [x for x in self.sequence if x not in connected_synapses]
        for ID in orphans:
            self.delete_neuron(ID)
            
    def delete_synapse_by_state(self, threshold=0.1, mode='lowest', 
                                stype='weight'):
        '''
        Method to delete synapse(s) by thresholding on synaptic states. There 
        are a number of ways (criterion) to select synapses for deletion. The 
        criterion is determined by the 'mode' parameter. 
        
        The following criteria (modes) are allowed::
            - lowest: select the lowest percentage of synapses, by state value, 
            for deletion. Threshold will determine the ratio. For example, if 
            threshold = 0.1, means the lowest decile of the synapses, by state 
            value, will be deleted.
            - below: select the synapses with state value below the threshold 
            value for deletion. For example, if threshold = 0.1, means that 
            synapses with state value lower than 0.1, will be deleted.
        
        @param threshold: threshold for use in deletion (as ratio). Default = 
        lowest.
        @type threshold: float
        @param mode: criteria for deletion. Default = lowest.
        @type mode: string
        @param stype: synaptic state for use in deletion criterion. Default = 
        weight.
        @type stype: float
        '''
        states = [float(x) for x in self.get_all_synaptic_states(stype)]
        states.sort()
        if mode == 'lowest':
            states = states[:int(len(states)*float(threshold))]
        elif mode == 'below':
            states = [x for x in states if x < float(threshold)]
        for value in states:
            self.base.cur.execute('''
                select source, destination from connectome where 
                key=:key and value=:value''',
                {'key': str(stype),
                 'value': str(value)})
            result = self.base.cur.fetchone()
            sourceID = str(result[0])
            destinationID = str(result[1])
            self.delete_synapse(sourceID, destinationID)
            
    def generate_random_synapses(self, count):
        '''
        '''
        nIDs = self.get_neurons('alive')
        
