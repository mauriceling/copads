import sys, os
sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'copads'))

import ode

# --------------------------
# Case 1: Bounded Variables
# --------------------------

# birth rate
birth = 0    
# natural death percent (per day)    
death = 0.0001 
# transmission percent  (per day)
transmission = 0.0095  
# resurect percent (per day) 
resurrect = 0.0001    
# destroy percent  (per day)   
destroy = 0.0001        

def human1(t, y):
    infected = transmission * y[0] * y[1]
    dead = death * y[0]
    return birth - infected - dead
def zombie1(t, y):
    newly_infected = transmission * \
        y[0] * y[1]
    resurrected = resurrect * y[2]
    destroyed = destroy * y[0] * y[1]
    return newly_infected + resurrected - \
           destroyed
def dead1(t, y):
    natural_death = death * y[0]
    destroyed_zombies = destroy * \
        y[0] * y[1]
    created_zombies = resurrect * y[2]
    return natural_death + \
           destroyed_zombies - \
           created_zombies

# system of ODEs
bounded = [human1, zombie1, dead1]   

# initial human, zombie, death population 
# respectively
y = [500.0, 0, 0]  
print('''Solving using 5th order Dormand-Prince method with \
bounded variables......''')
for i in [x for x in 
          ode.DP5(bounded, 0.0, y, 0.1, 50.0)]:
    print(','.join([str(z) for z in i]))
    
# -----------------------------
# Case 2: Un-Bounded Variables
# -----------------------------

def human2(t, y):
    infected = y[5] * y[0] * y[1]
    dead = y[4] * y[0]
    return y[3] - infected - dead
def zombie2(t, y):
    newly_infected = y[5] * y[0] * y[1]
    resurrected = y[6] * y[2]
    destroyed = y[7] * y[0] * y[1]
    return newly_infected + resurrected - \
           destroyed
def dead2(t, y):
    natural_death = y[4] * y[0]
    destroyed_zombies = y[7] * y[0] * y[1]
    created_zombies = y[6] * y[2]
    return natural_death + \
           destroyed_zombies - \
           created_zombies

unbounded = range(8)
unbounded[0] = human2
unbounded[1] = zombie2
unbounded[2] = dead2

y = range(8)
y[0] = 500.0 # initial human population
y[1] = 0.0   # initial zombie population
y[2] = 0.0   # initial death population
y[3] = 0     # birth rate             
y[4] = 0.0001 # natural death percent / day
y[5] = 0.0095 # transmission percent  / day
y[6] = 0.0001  # resurrect percent / day
y[7] = 0.0001  # destroy percent / day

print('''Solving using 5th order Dormand-Prince method \
with un-bounded variables......''')
for i in [x for x in 
          ode.DP5(unbounded, 0.0, y, 0.1, 50.0)]:
    print(','.join([str(z) for z in i]))

