import random

import sys, os
sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'copads'))

import ode

birth = 0               # birth rate
death = 0.0001          # natural death percent (per day)
transmission = 0.0095   # transmission percent  (per day)
resurect = 0.0001       # resurect percent (per day)
destroy = 0.0001        # destroy percent  (per day)

def human(t, y):
    infected = transmission*y[0]*y[1]
    dead = death*y[0]
    return birth - infected - dead
def zombie(t, y):
    newly_infected = transmission*y[0]*y[1]
    resurrected = resurect*y[2]
    destroyed = destroy*y[0]*y[1]
    return newly_infected + resurrected - destroyed
def dead(t, y):
    natural_death = death*y[0]
    destroyed_zombies = destroy*y[0]*y[1]
    created_zombies = resurect*y[2]
    return natural_death + destroyed_zombies - created_zombies

def influx(y, step):
    y[0] = y[0] + (5*step)
    return y
    
f = [human, zombie, dead]   # system of ODEs
# initial human, zombie, death population, and total respectively
y = [500.0, 0, 0]  

print('Solving using 5th order Dormand-Prince method ......')
noinflux = [x for x in ode.DP5(f, 0.0, y, 0.1, 50.0)]
influx = [x for x in ode.DP5(f, 0.0, y, 0.1, 50.0, influx)]

for i in range(len(noinflux)):
    consolidated = noinflux[i] + influx[i][1:]
    print ','.join([str(x) for x in consolidated])
