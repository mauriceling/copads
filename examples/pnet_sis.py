import sys, os
sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'copads'))

import pnet

infection = 0.01
recovery = 0.005

net = pnet.PNet()

net.add_places('susceptible', {'susceptible': 100})
net.add_places('infected', {'infected': 0})

def susceptible_infected(places): 
    #susceptible = places['susceptible'].attributes['susceptible']
    susceptible = 1000
    return infection * susceptible
    
def infected_susceptible(places):
    infected = places['infected'].attributes['infected']
    return recovery * infected
    
net.add_rules('infection', 'function', 
              ['susceptible.susceptible -> infected.infected', 
               susceptible_infected, 
               'susceptible.susceptible > 0'])
net.add_rules('recovery', 'function', 
              ['infected.infected -> susceptible.susceptible', 
               infected_susceptible, 
               'infected.infected > 0'])

net.simulate(500, 1, 1)

from pprint import pprint
pprint(net.rules)

data = net.report_tokens()
headers = ['timestep'] + data[0][1]

f = open('sis.csv', 'w')
f.write(','.join(headers) + '\n')
for tdata in data:
    tdata = [tdata[0]] + [str(x) for x in tdata[2]]
    f.write(','.join(tdata) + '\n')
f.close()
