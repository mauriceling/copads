import sys, os
sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'copads'))

import ode

birth = 0               # birth rate
death = 0.0001          # natural death percent (per day)
transmission = 0.0095   # transmission percent  (per day)
resurect = 0.0002       # resurect percent (per day)
destroy = 0.0003        # destroy percent  (per day)

              
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

def modifying_expression(y, step):
    y[0] = y[0] + (5 * step)
    return y
  
lower_bound = {'2': [0.0, 0.0]} 
upper_bound = {'0': [700, 700]} 

f = [human, zombie, dead]   # system of ODEs

y = [500.0, 0, 0]  # initial human, zombie, death population respectively
print('Solving using 4th order Runge Kutta method ......')
for i in [x for x in ode.RK4(f, 0.0, y, 0.1, 100.0, modifying_expression,
                             lower_bound, upper_bound)]:
    print(','.join([str(z) for z in i]))
print('')

