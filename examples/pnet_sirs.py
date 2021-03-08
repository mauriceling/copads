import sys, os
sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'copads'))

import pnet

infection = 0.01
recovery = 0.005
resusceptible = 0.01

net = pnet.PNet()

net.add_places('susceptible', {'susceptible': 100})
net.add_places('infected', {'infected': 0})
net.add_places('recovered', {'recovered': 0})

def susceptible_infected(places): 
    place = places['susceptible']
    susceptible = place.attributes['susceptible']
    return infection * susceptible
    
def infected_recovered(places):
    place = places['infected']
    infected = place.attributes['infected']
    return recovery * infected
    
def recovered_susceptible(places):
    place = places['recovered']
    recovered = place.attributes['recovered']
    return resusceptible * recovered
    
net.add_rules('infection', 'function', 
              ['susceptible.susceptible -> infected.infected', 
               susceptible_infected, 
               'susceptible.susceptible > 0'])
net.add_rules('recovery', 'function', 
              ['infected.infected -> recovered.recovered', 
               infected_recovered, 
               'infected.infected > 0'])
net.add_rules('resusceptible', 'function', 
              ['recovered.recovered -> susceptible.susceptible', 
               recovered_susceptible, 
               'recovered.recovered > 0'])

net.simulate(500, 1, 1)

from pprint import pprint
pprint(net.rules)

data = net.report_tokens()
headers = ['timestep'] + data[0][1]

f = open('sirs.csv', 'w')
f.write(','.join(headers) + '\n')
for tdata in data:
    tdata = [tdata[0]] + [str(x) for x in tdata[2]]
    f.write(','.join(tdata) + '\n')
f.close()
