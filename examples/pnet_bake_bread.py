import sys, os
sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'copads'))

import pnet

net = pnet.PNet()

# The ingredients
net.add_places('flour', {'flour': 1000})
net.add_places('water', {'water': 500})
net.add_places('sugar', {'sugar': 20})
net.add_places('yeast', {'yeast': 1})

# The "utensils"
net.add_places('mixer', {'flour': 0, 'water': 0, 'sugar': 0, 
                         'yeast': 0, 'dough': 0})
net.add_places('pan', {'dough': 0})
net.add_places('oven', {'dough': 0, 'bread': 0})
net.add_places('table', {'bread': 0, 'temperature': 400})
net.add_places('air', {'heat': 0})

# The steps
net.add_rules('add_flour', 'step', ['flour.flour -> mixer.flour; 100'])
net.add_rules('add_water', 'step', ['water.water -> mixer.water; 50'])
net.add_rules('add_sugar', 'step', ['sugar.sugar -> mixer.sugar; 2'])
net.add_rules('add_yeast', 'delay', ['yeast.yeast -> mixer.yeast; 0.5; 5'])
net.add_rules('blend', 'step', ['mixer.flour -> mixer.dough; 80',
                                'mixer.water -> mixer.dough; 40',
                                'mixer.sugar -> mixer.dough; 1.5',
                                'mixer.yeast -> mixer.dough; 1'])
net.add_rules('rise', 'incubate', ['10; mixer.dough -> pan.dough; \
                                    mixer.flour == 0; mixer.water == 0; \
                                    mixer.sugar == 0; mixer.yeast == 0'])
net.add_rules('set', 'incubate', ['10; pan.dough -> oven.dough; \
                                   pan.dough > 0'])
net.add_rules('bake', 'ratio', ['oven.dough -> oven.bread; 0.3; \
                                 oven.dough < 1; 0'])
net.add_rules('transfer', 'incubate', ['1; oven.bread -> table.bread; \
                                        oven.dough == 0'])
def cooling(places): 
    temp = places['table'].attributes['temperature']
    if temp <= 30.0: return 0.0
    else: return 0.1 * temp
net.add_rules('cool', 'function', ['table.temperature -> air.heat', 
                                    cooling, 
                                   'table.bread > 0'])

# Bake the bread !!!
net.simulate(90, 1, 1)

from pprint import pprint
pprint(net.rules)

data = net.report_tokens()
headers = ['timestep'] + data[0][1]

f = open('bread.csv', 'w')
f.write(','.join(headers) + '\n')
for tdata in data:
    tdata = [tdata[0]] + [str(x) for x in tdata[2]]
    f.write(','.join(tdata) + '\n')
f.close()


