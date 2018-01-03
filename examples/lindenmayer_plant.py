import sys, os
sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'copads'))

import random
from lindenmayer import lindenmayer

axiom = 'X'
rules = [['X', '0FL[2[X]R3X]R1F[3RFX]LX'],
         ['F', 'FF']]
start_position = (0, -200)
iterations = 6
turtle_file = '19_lindenmayer_plant_turtle.py'
image_file = '19_lindenmayer_plant_turtle.svg'
mapping = {'set_angle': 25,
           'random_angle': 0,
           'set_distance': 2.5,
           'random_distance': 0,
           'set_heading': 90,
           'background_colour': 'azure',
           'F': 'forward',
           'R': 'right',
           'L': 'left',
           '[': 'push',
           ']': 'pop',
           '0': 'brown',
           '1': 'dark green',
           '2': 'forest green'
           }

l = lindenmayer(1)
l.add_rules(rules)
l.generate(axiom, iterations)
l.turtle_generate(turtle_file, image_file, start_position, mapping)
