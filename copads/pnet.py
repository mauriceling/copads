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
    '''
    def __init__(self, name):
        '''
        Contructor method.
        
        @param name: name of the place/container
        @type name: string
        '''
        self.name = str(name)
        self.attributes = {}
        
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
        '''
        Private method which replaces Place.attributeA with the values in 
        Place.attributeB.
        
        @param place_name: name of the place/container
        @type place_name: string
        '''
        for k in self.places[place_name].attributesB.keys(): 
            self.places[place_name].attributesA[k] = \
            self.places[place_name].attributesB[k]
        
    def _step_rule(self, movement, value, interval):
        '''
        Private method which simulates a step rule action.
        
        @param movement: defines the movement of a token type. Each 
        movement is defined in the following format: <source 
        place>.<source token> -> <destination place>.<destination token>
        @type movement: string
        @param value: the number of tokens to move
        @type value: float
        @param interval: simulation time interval
        @type interval: integer
        '''
        source_place = self.places[movement[0].split('.')[0]]
        source_value = movement[0].split('.')[1]
        destination_place = self.places[movement[1].split('.')[0]]
        destination_value = movement[1].split('.')[1]
        if source_place.attributesA[source_value] < (value*interval):
            value = source_place.attributesA[source_value]
        source_place.attributesB[source_value] = \
            source_place.attributesA[source_value] - (value*interval)
        destination_place.attributesB[destination_value] = \
            destination_place.attributesB[destination_value] + \
            (value*interval)
        return [movement[0].split('.')[0], 
                movement[1].split('.')[0]]
    
    def _test_condition(self, place, token, operator, value):
        '''
        Private method used by rule processors for logical check of 
        condition. For example, the condition 'mixer.flour == 0' will be 
        written as 
        
        >>> _test_condition('mixer', 'flour', '==', 0)
        
        @param place: anme of place/container
        @type place: string
        @param token: name of token
        @type token: string
        @param operator: binary operator. Allowable values are '==' 
        (equals to), '>' (more than), '>=' (more than or equals to), '<' 
        (less than), '<=' (less than or equals to), and '!=' (not equals 
        to).
        @type operator: string
        @param value: value to be checked
        @return: 'passed' if test result is true, or 0 if test result is 
        false
        '''
        value = float(value)
        if operator == '==' and \
            self.places[place].attributes[token] == value:
            return 'passed'
        elif operator == '>' and \
            self.places[place].attributes[token] > value:
            return 'passed'
        elif operator == '>=' and \
            self.places[place].attributes[token] >= value:
            return 'passed'
        elif operator == '<' and \
            self.places[place].attributes[token] < value:
            return 'passed'
        elif operator == '<=' and \
            self.places[place].attributes[token] <= value:
            return 'passed'
        elif operator == '!=' and \
            self.places[place].attributes[token] != value:
            return 'passed'
        else:
            return 0
    
    def _incubate_rule(self, rule, interval):
        '''
        Private method which simulates an incubate rule action.
        
        @param rule: a dictionary representing the incubate rule
        @param interval: simulation time interval
        @type interval: integer
        @return: modified rule dictionary
        '''
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
    
    def _execute_rules(self, clock, interval):
        affected_places = []
        for rName in self.rules.keys():
            # Step rule
            if self.rules[rName]['type'] == 'step':
                movement = self.rules[rName]['movement']
                value = self.rules[rName]['value']
                self._step_rule(movement, value, interval)
            # Delay rule
            if self.rules[rName]['type'] == 'delay' and \
                (clock % self.rules[rName]['delay']) == 0:
                movement = self.rules[rName]['movement']
                value = self.rules[rName]['value']
                self._step_rule(movement, value, interval)
            # Incubate rule
            if self.rules[rName]['type'] == 'incubate':
                value = self.rules[rName]['value']
                rule = self._incubate_rule(self.rules[rName], interval)
                self.rules[rName] = rule
       
    def simulate(self, end_time, interval=1.0, report_frequency=1.0):
        '''
        Method to simulate the Petri Net. This method stores the generated 
        report in memory; hence, not suitable for extended simulations as 
        it can run out of memory. It is possible to conserve memory by 
        reducing the reporting frequency. Use simulate_yield method for 
        extended simulations.
        
        @param end_time: number of time steps to simulate. If end_time 
        = 1000, it can be 1000 seconds or 1000 days, depending on the 
        significance of each step
        @type end_time: integer
        @param interval: number of intervals between each time step. 
        Default = 1.0, simulate by time step interval
        @type interval: float
        @param report_frequency: number of time steps between each 
        reporting. Default = 1.0, each time step is reported
        @type report_frequency: float
        '''
        clock = 1
        end_time = int(end_time)
        while clock < end_time:
            self._execute_rules(clock, interval)
            if (clock % report_frequency) == 0: 
                self._generate_report(clock)
            clock = clock + interval

    def simulate_yield(self, end_time, interval=1.0):
        '''
        Method to simulate the Petri Net. This method runs as a generator, 
        making it suitable for extended simulation.
        
        @param end_time: number of time steps to simulate. If end_time 
        = 1000, it can be 1000 seconds or 1000 days, depending on the 
        significance of each step
        @type end_time: integer
        @param interval: number of intervals between each time step. 
        Default = 1.0, simulate by time step interval
        @type interval: float
        '''
        clock = 1
        end_time = int(end_time)
        while clock < end_time:
            self._execute_rules(clock, interval)
            self._generate_report(clock)
            rept = {}
            for k in self.report[str(clock)].keys():
                rept[k] = self.report[str(clock)][k]
            del self.report[str(clock)][k]
            yield (clock, rept)
            clock = clock + interval
                
    def _generate_report(self, clock):
        '''
        Private method to generate and store report in memory of each 
        token status (the value of each token) in every place/container.
        
        @param clock: step count of the current simulation
        @type clock: float
        '''
        rept = {}
        for pName in self.places.keys():
            for aName in self.places[pName].attributes.keys():
                value = self.places[pName].attributes[aName]
                name = '.'.join([pName, aName])
                rept[name] = value
        self.report[str(clock)] = rept
        
    def report_tokens(self, reportdict=None):
        '''
        Method to report the status of each token(s) from each place as a 
        list. This can be used in 2 different ways: to generate a list 
        representation of a status from one time step (such as from 
        simulate_yield method), or to generate a list representation of 
        a status from entire simulation (such as from simulate method). 
        
        >>> # from simulate method
        >>> net.simulate(65, 1, 1)
        >>> status = net.report_tokens()
        
        >>> # from simulate_yield method
        >>> status = [d for d in net.simulate_yield(65, 1)]
        >>> status = [(d[0], net.report_tokens(d[1])) for d in status]
        
        @param reportdict: status from one time step. Default = None. If 
        None, it will assume that simulate method had been executed and 
        all status are stored in memory, and this method will generate a 
        report from status stored in memory
        @type reportdict: dictionary
        @return: tuple of ([<place.token name>], [([<place.token value>]]) 
        if reportdict is given, or tuple of (time step, [<place.token 
        name>], [([<place.token value>]]) if reportdict is None.
        '''
        if reportdict:
            placetokens = reportdict.keys()
            tokenvalues = [reportdict[k] for k in placetokens]
            return (placetokens, tokenvalues)
        else:
            timelist = self.report.keys()
            datalist = [0] * len(timelist)
            for i in range(len(timelist)):
                placetokens = self.report[timelist[i]].keys()
                tokenvalues = [self.report[timelist[i]][k] 
                               for k in placetokens]
                datalist[i] = (timelist[i], placetokens, tokenvalues)
            return datalist
        