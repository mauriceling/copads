'''
Framework for Neural Network Applications
Date created: 15th June 2015
License: Python Software Foundation License version 2
'''

import sqlite3 as s
from random import random

class brainbase(object):

    def __init__(self, path):
        self.conn = s.connect(path)
        self.cur = self.conn.cursor()
        braincheck = self._check_brain()
        if True not in braincheck:
            self._format_brain()
        elif False in braincheck:
            self._repair_brain(braincheck)

    def close_brain(self):
        self.conn.commit()
        self.conn.close()
            
    def _check_brain(self):
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
        self.cur.execute('''
            create table if not exists neuron (
                ID integer primary key autoincrement,
                name text not null,
                status text not null default 'alive')''')
        self.cur.execute('''
            create table if not exists neuron_internal_states (
                ID integer not null,
                key text not null,
                value text not null,
                primary key (ID, key))''')
        self.cur.execute('''
            create table if not exists neuron_input_states (
                ID integer not null,
                sourceID text not null,
                value text not null,
                primary key (ID, sourceID))''')
        self.cur.execute('''
            create table if not exists connectome (
                source integer not null,
                destination integer not null,
                key text not null default 'weight',
                value text not null,
                primary key (source, destination, key))''')
    
    def _repair_brain(self, braincheck):
        pass
        
    def add_neuron(self, **kwargs):
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
            kwargs['pstate'] = '0.0'
        self.cur.execute('insert into neuron (name) values (?)', (name,))
        ID = str(self.cur.lastrowid)
        for key in kwargs:
            self.cur.execute('''
                insert into neuron_internal_states (ID, key, value) 
                values (?,?,?)''', (ID, str(key), str(kwargs[key])))
        self.conn.commit()
        return ID

    def _check_neuron_presence(self, ID):
        self.cur.execute('select name from neuron where ID=:ID',
                         {'ID': str(ID)})
        if self.cur.fetchone() == None:
            return False
        else:
            return True
                         
    def add_synapse(self, sourceID, destinationID, **kwargs):
        if self._check_neuron_presence(sourceID) == False:
            sourceID = self.add_neuron()
        if self._check_neuron_presence(destinationID) == False:
            destinationID = self.add_neuron()
        if 'weight' not in kwargs:
            kwargs['weight'] = random()
        for key in kwargs:
            self.cur.execute('''
                insert into connectome (source, destination, key, value) 
                values (?,?,?,?)''',
                (sourceID, destinationID, str(key), str(kwargs[key])))
        self.conn.commit()

    def get_summation(self, ID):
        self.cur.execute('''select value from neuron_internal_states
                            where ID=:ID and key=:key''',
                         {'ID': str(ID),
                          'key': 'summation'})
        return self.cur.fetchone()

    def get_transfer(self, ID):
        self.cur.execute('''select value from neuron_internal_states
                            where ID=:ID and key=:key''',
                         {'ID': str(ID),
                          'key': 'transfer'})
        return self.cur.fetchone()

    def get_input(self, ID):
        self.cur.execute('''select value from neuron_input_states
                            where ID=:ID''',
                         {'ID': str(ID)})
        return [float(str(x[0])) for x in self.cur.fetchall()]

    def set_pstate(self, ID, pstate):
        self.cur.execute('''update neuron_internal_states
                            set value=:pstate
                            where ID=:ID and key=:key''',
                         {'pstate': pstate,
                          'ID': str(ID),
                          'key': 'pstate'})
        self.conn.commit()

    def get_next_neurons(self, ID, stype='weight'):
        self.cur.execute('''select destination, value 
                            from neuron_input_states
                            where source=:source and key=:stype''',
                         {'source': str(ID),
                          'stype': stype})
        return [(str(x[0]), float(str(x[1])))
                for x in self.cur.fetchall()]

    def set_input_states(self, sourceID, destinationID, key, value):
        self.cur.execute('''update neuron_input_states
                            set value=:value
                            where source=:sourceID and
                            destinationID=:destinationID and
                            key=:key''',
                         {'value': value,
                          'sourceID': str(sourceID),
                          'destinationID': str(destinationID),
                          'key': 'pstate'})
        self.conn.commit()
        

class brain(object):

    def __init__(self, path):
        self.base = brainbase(path)
        self.sequence = []

    def _neuron_summation(self, ID):
        sum_func = self.base.get_summation(ID)
        if sum_func == None:
            return 0.0
        sum_func = str(sum_func[0])
        neuron_input = self.base.get_input(ID)
        if sum_func == 'summation':
            return sum(neuron_input) / len(neuron_input)

    def _neuron_transfer(self, ID, neuron_input):
        transfer = self.base.get_transfer(ID)
        if transfer == None:
            return 0.0
        transfer = str(transfer[0])
        if transfer == 'linear':
            return neuron_input

    def synaptic_activation(self, ID, stype='weight'):
        sourceID = ID
        for n in self.base.get_next_neurons(ID, stype):
            destinationID = n[0]
            value = n[1]
            self.base.set_input_states(sourceID, destinationID,
                                       stype, value)

    def execute_neuron(self, ID, stype='weight'):
        neuron_input = self._neuron_summation(ID)
        pstate = self._neuron_transfer(ID, neuron_input)
        self.base.set_pstate(ID, pstate)
        self.synaptic_activation(ID, stype)
        
