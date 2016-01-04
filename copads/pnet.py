'''
Framework for Petri Nets Typed Applications
Date created: 3rd January 2016
License: Python Software Foundation License version 2
'''

class Place(object):
    '''
    Class to represent a place or container in petri nets. The tokens are 
    represented as a dictionary where each token is represented as a 
    key-value pair. The key represents the type of token and the value 
    represents the number of such tokens. This enables more than one type 
    of tokens to be represented.
    
    The tokens are represented in 2 dictionaries - attributeA and 
    attributeB, where attributeA is the state of one or more tokens at the 
    start of time t, and attributeB, which is the state of one or more 
    tokens after time t. Before the start of time t+1, attributeA is 
    replaced with attributeB. This is prevent simulation errors resulting 
    from the firing order or rules, also known as transition rules.
    '''
    def __init__(self, name):
        '''
        Contructor method.
        
        @param name: name of the place/container
        @type name: string
        '''
        self.name = str(name)
        self.attributesA = {}
        self.attributesB = {}
        
class PNet(object):
    '''
    Class to represent a Petri Net or Petri Net typed object.
    
    The places and transition rules are represented as dictionary objects. 
    Places dictionary will have the name of place as key and the Place 
    (pnet.Place object) as value. Transition rules dictionary will have 
    the name of rule appended with a number (in the format of <rule name>_
    <number> in order to ensure uniqueness) as key and the value is a 
    dictionary to represent the transition rule (the structure of the 
    transition rule dictionary is dependent on the type of rules).
    '''
    def __init__(self):
        '''
        Contructor method.
        '''
        self.places = {}
        self.rules = {}
        self.report = {}
    
    def add_places(self, place_name, tokens):
        '''
        '''
        self.places[place_name] = Place(place_name)
        self.places[place_name].attributesA = tokens
        d = {}
        for k in tokens: d[k] = 0
        self.places[place_name].attributesB = d
    
    def add_rules(self, rule_name, rule_type, triggers):
        count = 1
        for t in triggers:
            t = [x.strip() for x in t.split(';')]
            d = {'type': rule_type,
                 'movement': None}
            if rule_type == 'step': 
                d['movement'] = [x.strip() for x in t[0].split('->')]
                d['value'] = float(t[1])
            if rule_type == 'delay': 
                d['movement'] = [x.strip() for x in t[0].split('->')]
                d['value'] = float(t[1])
                d['delay'] = int(t[2])
            if rule_type == 'incubate':
                d['value'] = float(t[0])
                d['movement'] = [x.strip() for x in t[1].split('->')]
                d['conditions'] = [cond for cond in t[2:]]
                d['timer'] = 0
            self.rules[rule_name + '_' + str(count)] = d
            count = count + 1
    
    def _attribute_swap(self, place_name):
        d = {}
        for k in self.places[place_name].attributesB.keys(): 
            d[k] = self.places[place_name].attributesB[k]
        self.places[place_name].attributesA = d
        
    def _step_rule(self, movement, value, interval):
        source_place = self.places[movement[0].split('.')[0]]
        source_value = movement[0].split('.')[1]
        destination_place = self.places[movement[1].split('.')[0]]
        destination_value = movement[1].split('.')[1]
        if source_place.attributesA[source_value] < (value*interval):
            value = source_place.attributesA[source_value]
        source_place.attributesB[source_value] = \
            source_place.attributesA[source_value] - (value*interval)
        destination_place.attributesB[destination_value] = \
            destination_place.attributesB[destination_value] + (value*interval)
        return [movement[0].split('.')[0], 
                movement[1].split('.')[0]]
    
    def _test_condition(self, source_place, source_value, operator, criterion):
        criterion = float(criterion)
        if operator == '==' and \
            self.places[source_place].attributesA[source_value] == criterion:
            return 'passed'
        elif operator == '>' and \
            self.places[source_place].attributesA[source_value] > criterion:
            return 'passed'
        elif operator == '>=' and \
            self.places[source_place].attributesA[source_value] >= criterion:
            return 'passed'
        elif operator == '<' and \
            self.places[source_place].attributesA[source_value] < criterion:
            return 'passed'
        elif operator == '<=' and \
            self.places[source_place].attributesA[source_value] <= criterion:
            return 'passed'
        elif operator == '!=' and \
            self.places[source_place].attributesA[source_value] != criterion:
            return 'passed'
        else:
            return 0
    
    def _incubate_rule(self, rule, interval):
        value = rule['value']
        timer = rule['timer']
        conditions = rule['conditions']
        movement = rule['movement']
        test = [0] * len(conditions)
        for i in range(len(conditions)):
            cond = conditions[i]
            if len(cond.split('==')) == 2:
                operator = '=='
                cond = [c.strip() for c in cond.split('==')]
            elif len(cond.split('>')) == 2:
                operator = '>'
                cond = [c.strip() for c in cond.split('>')]
            elif len(cond.split('>=')) == 2:
                operator = '>='
                cond = [c.strip() for c in cond.split('>=')]
            elif len(cond.split('<')) == 2:
                operator = '<'
                cond = [c.strip() for c in cond.split('<')]
            elif len(cond.split('<=')) == 2:
                operator = '<='
                cond = [c.strip() for c in cond.split('<=')]
            elif len(cond.split('!=')) == 2:
                operator = '!='
                cond = [c.strip() for c in cond.split('!=')]
            source_place = cond[0].split('.')[0]
            source_value = cond[0].split('.')[1]
            criterion = cond[1]
            test[i] = self._test_condition(source_place, source_value, 
                                           operator, criterion)
        if len([0 for t in test if t == 0]) == 0:
            if (timer + interval) < value:
                rule['timer'] = timer + interval
            else:
                source_place = self.places[movement[0].split('.')[0]]
                source_value = movement[0].split('.')[1]
                destination_place = self.places[movement[1].split('.')[0]]
                destination_value = movement[1].split('.')[1]
                destination_place.attributesB[destination_value] = \
                    source_place.attributesA[source_value]
                destination_place.attributesA[destination_value] = 0
                source_place.attributesA[source_value] = 0
                source_place.attributesB[source_value] = 0
                rule['timer'] = 0
        return (rule, [movement[0].split('.')[0], 
                       movement[1].split('.')[0]])
        
    def simulate(self, end_time, interval=1, report_frequency=1):
        affected_places = []
        clock = 1
        while clock < end_time:
            for rName in self.rules.keys():
                # Step rule
                if self.rules[rName]['type'] == 'step':
                    movement = self.rules[rName]['movement']
                    value = self.rules[rName]['value']
                    affected = self._step_rule(movement, value, interval)
                    affected_places = affected_places + affected
                # Delay rule
                if self.rules[rName]['type'] == 'delay' and \
                    (clock % self.rules[rName]['delay']) == 0:
                    movement = self.rules[rName]['movement']
                    value = self.rules[rName]['value']
                    affected = self._step_rule(movement, value, interval)
                    affected_places = affected_places + affected
                # Incubate rule
                if self.rules[rName]['type'] == 'incubate':
                    value = self.rules[rName]['value']
                    (rule, affected) = self._incubate_rule(self.rules[rName],
                                                           interval)
                    self.rules[rName] = rule
                    affected_places = affected_places + affected
            for pName in affected_places: self._attribute_swap(pName)
            clock = clock + interval
            if (clock % report_frequency) == 0: self.generate_report(clock)
            
    def generate_report(self, clock):
        rept = {}
        for pName in self.places.keys():
            for aName in self.places[pName].attributesA.keys():
                value = self.places[pName].attributesA[aName]
                name = '.'.join([pName, aName])
                rept[name] = value
        self.report[str(clock)] = rept
        