import sys, os
sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'copads'))

import random
from lindenmayer import lindenmayer

axiom = 'F'
rules = [['F', '0FFL[1LFRFRF]R[2RFLFLF]']]
start_position = (0, -200)
iterations = 5
turtle_file = '19_lindenmayer_tree_turtle.py'
image_file = '19_lindenmayer_tree_turtle.svg'
mapping = {'set_angle': 22,
           'random_angle': 0,
           'set_distance': 5,
           'random_distance': 0,
           'set_heading': 90,
           'background_colour': 'ivory',
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
