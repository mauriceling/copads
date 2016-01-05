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
    
    The following types of transition rules are allowed: 
        - step rule
        - delay rule
        - incubate rule
        
    Step rule is to be executed at each time step. For example, if 20g of 
    flour is to be transferred from flour bowl to mixer bowl at each time 
    step, this 'add_flour' rule can be defined as:
    
    >>> net.add_rules('add_flour', 'step', 
                      ['flour.flour -> mixer.flour; 20'])
    
    A single step rule can trigger more than one token movement. For 
    example, the following step rule simulates the mixing of ingredients 
    into a flour dough:
    
    >>> net.add_rules('blend', 'step', 
                      ['mixer.flour -> mixer.dough; 15',
                       'mixer.water -> mixer.dough; 10',
                       'mixer.sugar -> mixer.dough; 0.9',
                       'mixer.yeast -> mixer.dough; 1'])
                       
    Delay rule acts as a time delay between each token movement. For 
    example, the following rule simulates the transfer of 0.5g of yeast 
    into the mixer bowl:
    
    >>> net.add_rules('add_yeast', 'delay', 
                      ['yeast.yeast -> mixer.yeast; 0.5; 10'])
                      
    Incubate rule is a variation of delay rule. While delay rule is not 
    condition dependent, incubate rule starts a time delay when one or 
    more conditions are met. For example,
    
    >>> net.add_rules('rise', 'incubate', 
                      ['10; mixer.dough -> pan.dough; \
                       mixer.flour == 0; mixer.water == 0; \
                       mixer.sugar == 0; mixer.yeast == 0'])
                       
    sets a 10 time step delay when all flour, water, sugar, and yeast in 
    the mixer bowl are used up, which simulates the completemixing into a 
    bread dough. The 10 time step then simulates the time needed for the 
    dough to rise. After 10 time steps, dough in the mixer is transferred 
    into the pan.
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
        Method to add a place/container into the Petri Net.
        
        For example, the following adds a "flour" place containing 1000 
        tokens of flour, which can be seen as a bowl of 1000g of flour:
        
        >>> net.add_places('flour', {'flour': 1000})
        
        @param place_name: name of the place/container
        @type place_name: string
        @param tokens: token(s) for the place/container where key is the 
        name/type of token and value is the number of tokens for the specific 
        type
        @type tokens: dictionary
        '''
        self.places[place_name] = Place(place_name)
        self.places[place_name].attributesA = tokens
        for k in tokens:
            self.places[place_name].attributesB[k] = 0
    
    def add_rules(self, rule_name, rule_type, triggers):
        '''
        Method to add a transition rule into the Petri Net.
        
        @param rule_name: name of the transition rule
        @type rule_name: string
        @param rule_type: type of rule. Allowable types are 'step' for 
        step rule, 'delay' for delay rule, and 'incubate' for incubate 
        rule. Please see module documentation for the description of 
        rules.
        @type rule_type: string
        @param triggers: description of the trigger rule
        @type triggers: list
        '''
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
        
    def simulate(self, end_time, interval=1, report_frequency=1, 
                 yielding=False):
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
            if (clock % report_frequency) == 0: 
                self.generate_report(clock)
            if yielding:
                rept = {}
                for k in self.report[str(clock)].keys():
                    rept[k] = self.report[str(clock)][k]
                del self.report[str(clock)][k]
                yield rept
            
    def generate_report(self, clock):
        rept = {}
        for pName in self.places.keys():
            for aName in self.places[pName].attributesA.keys():
                value = self.places[pName].attributesA[aName]
                name = '.'.join([pName, aName])
                rept[name] = value
        self.report[str(clock)] = rept
        