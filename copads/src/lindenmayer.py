'''
Lindenmayer System (L-System)

Copyright (c) Maurice H.T. Ling <mauriceling@acm.org>

Date created: 4th January 2015
'''
import random

class lindenmayer(object):
    '''
    '''
    def __init__(self, command_length=1, rules=[]):
        '''
        '''
        self.command_length = command_length
        self.rules = []
        if len(rules) > 0:
            self.add_rules(rules)
    
    def add_rules(self, rules):
        '''
        '''
        for x in rules:
            if len(x) == 2:
                # [predicate, replacement]
                self.rules.append([x[0], x[1], 1, 'replacement', None])
            elif len(x) == 3:
                # [predicate, replacement, priority]
                self.rules.append([x[0], x[1], int(x[2]), 'replacement', None])
            elif len(x) == 4 and (x[3] not in ['probability', 
                                               'replacement', 
                                               'function']):
                # [predicate, replacement, priority, '<something_else>']
                print('''Warning: Rule type can only be 'probabilistic', \          
                'replacement' or 'function'. Rule, %s, is not added into \ 
                system.''' % str(x))
            elif len(x) == 4 and x[3] == 'replacement':
                # [predicate, replacement, priority, 'replacement']
                self.rules.append([x[0], x[1], int(x[2]), x[3], None])
             elif len(x) == 4 and x[3] == 'probabilistic':
                # [predicate, replacement, priority, 'probability']
                print('''Warning: Function rule will require a \ 
                probability. Rule, %s, is added into system as a \
                replacement rule (100% activation probability).''' % str(x))
                self.rules.append([x[0], x[1], int(x[2]), 'replacement', None])
            elif len(x) == 5 and x[3] == 'probability':
                # [predicate, replacement, priority, 'probability', probability]
                self.rules.append([x[0], x[1], int(x[2]), x[3], float(x[4])])
            elif len(x) == 4 and x[3] == 'function':
                print('''Warning: Function rule will require a \ 
                bounded-function. Rule, %s, is not added into \
                system.''' % str(x))
            elif len(x) == 5 and x[3] == 'function':
                # [predicate, replacement, priority, 'function', func]
                self.rules.append([x[0], x[1], int(x[2]), x[3], x[4]])
        self.priority_levels = [x[2] for x in self.rules][-1]
         
    def _apply_priority_rules(self, priority, data):
        '''
        '''
        rules = [x for x in self.rules if x[2] == int(priority)]
        ndata = ''
        pointer = 0
        while pointer < len(data):
            cmd = data[pointer:pointer+self.command_length]
            for rule in rules:
                if cmd == rule[0] and rule[3] == 'replacement':
                    cmd = rule[1]
                    break
                if cmd == rule[0] and rule[3] == 'probability' \
                and random.random() < x[4]:
                    cmd = rule[1]
                    break
                if cmd == rule[0] and rule[3] == 'function':
                    cmd = rule[4](data)
                    break
            ndata = ndata + cmd
            pointer = pointer + self.command_length
        return ndata
            
    def apply_rules(self, data):
        '''
        '''
        for priority in list(range(1, self.priority_levels+1)):
            data = self._apply_priority_rules(priority, data)
        return data
        

if __name__=='__main__':
    print('Case 1')
    s = lindenmayer(1)
    r = [['A', 'B'],
         ['B', 'AB']]
    s.add_rules(r)
    axiom = 'A'
    for i in range(10):
        print(i, axiom)
        axiom = s.apply_rules(axiom)
    print('Case 2')
    s = lindenmayer(2)
    r = [['AA', 'AB'],
         ['AB', 'AAB']]
    s.add_rules(r)
    axiom = 'AA'
    for i in range(15):
        print(i, axiom)
        axiom = s.apply_rules(axiom)
        
    