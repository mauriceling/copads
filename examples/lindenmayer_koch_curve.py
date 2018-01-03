import sys, os
sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'copads'))

import random
from lindenmayer import lindenmayer

axiom = 'F'
rules = [['F', 'FRFLFLFRF']]
start_position = (-300, 250)
iterations = 5
turtle_file = '19_lindenmayer_koch_turtle.py'
image_file = '19_lindenmayer_koch_turtle.svg'
mapping = {'set_angle': 90,
           'random_angle': 0,
           'set_distance': 2.5,
           'random_distance': 0,
           'background_colour': 'pale goldenrod',
           'F': 'forward',
           'R': 'right',
           'L': 'left'}

l = lindenmayer(1)
l.add_rules(rules)
l.generate(axiom, iterations)
l.turtle_generate(turtle_file, image_file, start_position, mapping)
