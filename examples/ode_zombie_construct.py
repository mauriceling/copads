import sys, os
sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'copads'))

from ode import ODE_constructor

scriptfile = 'zombie_attack.py'
resultsfile = 'zombie_data.csv'
time = (0.0, 0.1, 100.0)
ODE_solver = 'RK4'
expressions = {'human': ['birth_rate',
                         '- (transmission_rate * human * zombie)',
                         '- (death_rate * human)'],
               'zombie': ['(transmission_rate * human * zombie)',
                          '(resurrection_rate * dead)',
                          '- (destroy_rate * human * zombie)'],
               'dead': ['(death_rate * human)',
                        '(destroy_rate * human * zombie)',
                        '- (resurrection_rate * dead)']}
parameters = {'birth_rate': 0.0,          # birth rate
              'transmission_rate': 0.0095,# transmission percent  (per day)
              'death_rate': 0.0001,       # natural death percent (per day)
              'resurrection_rate': 0.0002,# resurect percent (per day)
              'destroy_rate':0.0003       # destroy percent  (per day)
              }
initial_conditions = {'human': 500.0,
                      'zombie': 0.0, 
                      'dead': 0.0}
modifying_expressions = ['human = human + (5*step)']
lower_bound = {'human': [0.0, 0.0]}
upper_bound = {'zombie': [700, 700]}
overflow = 1e100
zerodivision = 1e100
                    
s = ODE_constructor(scriptfile, resultsfile, time, ODE_solver,
                    expressions, parameters, initial_conditions,
                    modifying_expressions,
                    lower_bound, upper_bound,
                    overflow, zerodivision)

