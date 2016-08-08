import sys, os
sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'copads'))

import ode

initial_nuclei = 10000.0
decay_constant = 0.2

def decay(t, y):
    return -decay_constant * y[0]

print('Solving using Euler method......')
for i in [x for x in ode.Euler([decay], 0.0, [initial_nuclei], 0.1, 50.0)]:
    print(','.join([str(x) for x in i]))
print('')

print('Solving using RK4 method......')
for i in [x for x in ode.RK4([decay], 0.0, [initial_nuclei], 0.1, 50.0)]:
    print(','.join([str(x) for x in i]))
print('')

print('Solving using RK3 method......') 
for i in [x for x in ode.RK3([decay], 0.0, [initial_nuclei], 0.1, 50.0)]:
    print(','.join([str(x) for x in i]))
print('')

print("Solving using Heun's method......")
for i in [x for x in ode.Heun([decay], 0.0, [initial_nuclei], 0.1, 50.0)]:
    print(','.join([str(x) for x in i]))
print('')

print('Solving using RK4 method with 3/8 rule......')
for i in [x for x in ode.RK38([decay], 0.0, [initial_nuclei], 0.1, 50.0)]:
    print(','.join([str(x) for x in i]))
print('')

print('Solving using CK4 method......')
for i in [x for x in ode.CK4([decay], 0.0, [initial_nuclei], 0.1, 50.0)]:
    print(','.join([str(x) for x in i]))
print('')

print('Solving using CK5 method......') 
for i in [x for x in ode.CK5([decay], 0.0, [initial_nuclei], 0.1, 50.0)]:
    print(','.join([str(x) for x in i]))
print('')

print('Solving using RKF4 method......')
for i in [x for x in ode.RKF4([decay], 0.0, [initial_nuclei], 0.1, 50.0)]:
    print(','.join([str(x) for x in i]))
print('')

print('Solving using RKF5 method......')
for i in [x for x in ode.RKF5([decay], 0.0, [initial_nuclei], 0.1, 50.0)]:
    print(','.join([str(x) for x in i]))
print('')

print('Solving using DP4 method......') 
for i in [x for x in ode.DP4([decay], 0.0, [initial_nuclei], 0.1, 50.0)]:
    print(','.join([str(x) for x in i]))
print('')

print('Solving using DP5 method......')
for i in [x for x in ode.DP5([decay], 0.0, [initial_nuclei], 0.1, 50.0)]:
    print(','.join([str(x) for x in i]))
print('')
